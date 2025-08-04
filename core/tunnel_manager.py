#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🚇 TUNNEL MANAGER - Module de gestion des tunnels
Ngrok, Cloudflare, LocalTunnel pour le pentest
"""

import os
import subprocess
import threading
import requests
import json
import time
from urllib.parse import urlparse

class TunnelManager:
    def __init__(self):
        self.active_tunnels = {}
        self.tunnel_processes = {}
        
    def start_ngrok(self, local_port=8080, region="us"):
        """Démarre un tunnel Ngrok"""
        print(f"🚇 Démarrage Ngrok sur le port {local_port}")
        
        try:
            # Vérifier si ngrok est installé
            result = subprocess.run(['ngrok', 'version'], capture_output=True, text=True)
            if result.returncode != 0:
                print("❌ Ngrok non installé. Installation...")
                self.install_ngrok()
                
            # Démarrer ngrok
            cmd = ['ngrok', 'http', str(local_port), '--region', region]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Attendre que ngrok démarre
            time.sleep(3)
            
            # Récupérer l'URL publique
            try:
                response = requests.get('http://localhost:4040/api/tunnels')
                tunnels = response.json()['tunnels']
                
                if tunnels:
                    public_url = tunnels[0]['public_url']
                    self.active_tunnels['ngrok'] = {
                        'type': 'ngrok',
                        'local_port': local_port,
                        'public_url': public_url,
                        'process': process
                    }
                    
                    print(f"✅ Ngrok tunnel: {public_url}")
                    return public_url
                    
            except Exception as e:
                print(f"❌ Erreur Ngrok: {e}")
                process.terminate()
                
        except Exception as e:
            print(f"❌ Erreur démarrage Ngrok: {e}")
            
        return None
        
    def install_ngrok(self):
        """Installe Ngrok automatiquement"""
        print("📦 Installation de Ngrok...")
        
        # Détection du système
        import platform
        system = platform.system().lower()
        
        if system == "windows":
            # Télécharger et installer ngrok pour Windows
            os.system("curl -O https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip")
            os.system("tar xvzf ngrok-stable-windows-amd64.zip")
        elif system == "linux":
            # Installation pour Linux
            os.system("curl -O https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
            os.system("unzip ngrok-stable-linux-amd64.zip")
            os.system("sudo mv ngrok /usr/local/bin")
        elif system == "darwin":
            # Installation pour macOS
            os.system("brew install ngrok/ngrok/ngrok")
            
        print("✅ Ngrok installé")
        
    def start_cloudflare_tunnel(self, local_port=8080):
        """Démarre un tunnel Cloudflare"""
        print(f"☁️ Démarrage Cloudflare Tunnel sur le port {local_port}")
        
        try:
            # Vérifier si cloudflared est installé
            result = subprocess.run(['cloudflared', 'version'], capture_output=True, text=True)
            if result.returncode != 0:
                print("❌ Cloudflared non installé")
                return None
                
            # Démarrer le tunnel
            cmd = ['cloudflared', 'tunnel', '--url', f'http://localhost:{local_port}']
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Attendre et récupérer l'URL
            time.sleep(5)
            
            # Lire la sortie pour récupérer l'URL
            output, error = process.communicate(timeout=10)
            
            if "https://" in str(output):
                public_url = str(output).split("https://")[1].split()[0]
                public_url = "https://" + public_url
                
                self.active_tunnels['cloudflare'] = {
                    'type': 'cloudflare',
                    'local_port': local_port,
                    'public_url': public_url,
                    'process': process
                }
                
                print(f"✅ Cloudflare tunnel: {public_url}")
                return public_url
                
        except Exception as e:
            print(f"❌ Erreur Cloudflare: {e}")
            
        return None
        
    def start_localtunnel(self, local_port=8080):
        """Démarre un tunnel LocalTunnel"""
        print(f"🌐 Démarrage LocalTunnel sur le port {local_port}")
        
        try:
            # Vérifier si npx est disponible
            result = subprocess.run(['npx', '--version'], capture_output=True, text=True)
            if result.returncode != 0:
                print("❌ Node.js/npx non installé")
                return None
                
            # Démarrer localtunnel
            cmd = ['npx', 'localtunnel', '--port', str(local_port)]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Attendre et récupérer l'URL
            time.sleep(3)
            
            output, error = process.communicate(timeout=10)
            
            if "https://" in str(output):
                public_url = str(output).split("https://")[1].split()[0]
                public_url = "https://" + public_url
                
                self.active_tunnels['localtunnel'] = {
                    'type': 'localtunnel',
                    'local_port': local_port,
                    'public_url': public_url,
                    'process': process
                }
                
                print(f"✅ LocalTunnel: {public_url}")
                return public_url
                
        except Exception as e:
            print(f"❌ Erreur LocalTunnel: {e}")
            
        return None
        
    def start_proxy_server(self, local_port=8080, proxy_port=9090):
        """Démarre un serveur proxy"""
        print(f"🔄 Démarrage proxy sur le port {proxy_port}")
        
        try:
            # Créer un script proxy simple
            proxy_script = f"""
import socket
import threading
import requests

def handle_client(client_socket):
    try:
        request = client_socket.recv(4096)
        if request:
            # Transférer la requête vers le serveur local
            response = requests.get('http://localhost:{local_port}', 
                                 headers={{'Host': 'localhost'}})
            client_socket.send(response.content)
    except:
        pass
    finally:
        client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', {proxy_port}))
server.listen(5)

print(f"🔄 Proxy démarré sur le port {{proxy_port}}")

while True:
    client, addr = server.accept()
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
"""
            
            # Sauvegarder et exécuter le script
            with open('proxy_server.py', 'w') as f:
                f.write(proxy_script)
                
            process = subprocess.Popen(['python', 'proxy_server.py'])
            
            self.active_tunnels['proxy'] = {
                'type': 'proxy',
                'local_port': local_port,
                'proxy_port': proxy_port,
                'process': process
            }
            
            print(f"✅ Proxy démarré sur le port {proxy_port}")
            return f"http://localhost:{proxy_port}"
            
        except Exception as e:
            print(f"❌ Erreur proxy: {e}")
            
        return None
        
    def stop_tunnel(self, tunnel_type):
        """Arrête un tunnel spécifique"""
        if tunnel_type in self.active_tunnels:
            tunnel = self.active_tunnels[tunnel_type]
            if 'process' in tunnel:
                tunnel['process'].terminate()
                print(f"⏹️ Tunnel {tunnel_type} arrêté")
            del self.active_tunnels[tunnel_type]
            
    def stop_all_tunnels(self):
        """Arrête tous les tunnels"""
        for tunnel_type in list(self.active_tunnels.keys()):
            self.stop_tunnel(tunnel_type)
            
    def get_active_tunnels(self):
        """Retourne les tunnels actifs"""
        return self.active_tunnels
        
    def create_qr_code(self, url):
        """Crée un QR code pour l'URL du tunnel"""
        try:
            import qrcode
            from PIL import Image
            
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            img.save("tunnel_qr.png")
            
            print(f"📱 QR code créé: tunnel_qr.png")
            return "tunnel_qr.png"
            
        except ImportError:
            print("❌ Module qrcode non installé")
            return None
        except Exception as e:
            print(f"❌ Erreur QR code: {e}")
            return None
            
    def generate_phishing_link(self, tunnel_url, template_name):
        """Génère un lien de phishing avec le tunnel"""
        if tunnel_url:
            phishing_url = f"{tunnel_url}"
            print(f"🎣 Lien de phishing: {phishing_url}")
            return phishing_url
        return None 