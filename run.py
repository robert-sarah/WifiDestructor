 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎣 ULTIMATE PHISHING TOOL v4.0 - LAUNCHER
Cross-Platform: Windows, Linux, macOS
"""

import os
import sys
import platform
import subprocess
from colorama import init, Fore, Back, Style

# Initialisation des couleurs
init(autoreset=True)

def print_banner():
    """Affiche la bannière"""
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║              🎣 ULTIMATE PHISHING TOOL v4.0                    ║
║                                                                      ║
║  {Fore.GREEN}Cross-Platform: Windows, Linux, macOS{Fore.CYAN}                        ║
║  {Fore.YELLOW}Gray/Black Hat - Multi-Attack - WiFi - Advanced Pentest{Fore.CYAN}      ║
║  {Fore.RED}50+ Templates - WiFi Attacks - Network Scanner{Fore.CYAN}              ║
║  {Fore.MAGENTA}Payload Generator - Backdoor Creator - Tunnel Manager{Fore.CYAN}          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def detect_os():
    """Détecte le système d'exploitation"""
    os_name = platform.system().lower()
    print(f"{Fore.YELLOW}[*] Système détecté: {os_name}{Style.RESET_ALL}")
    return os_name

def check_python_version():
    """Vérifie la version de Python"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"{Fore.RED}[!] Python 3.7+ requis. Version actuelle: {version.major}.{version.minor}{Style.RESET_ALL}")
        return False
    print(f"{Fore.GREEN}[+] Python {version.major}.{version.minor}.{version.micro} - OK{Style.RESET_ALL}")
    return True

def install_dependencies():
    """Installe les dépendances"""
    print(f"{Fore.YELLOW}[*] Installation des dépendances...{Style.RESET_ALL}")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print(f"{Fore.GREEN}[+] Dépendances installées avec succès!{Style.RESET_ALL}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[!] Erreur installation: {e}{Style.RESET_ALL}")
        return False

def create_directories():
    """Crée les dossiers nécessaires"""
    directories = [
        'templates', 'cloned_sites', 'exports', 'logs',
        'captures', 'payloads', 'backdoors', 'screenshots'
    ]
    
    print(f"{Fore.YELLOW}[*] Création des dossiers...{Style.RESET_ALL}")
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"{Fore.GREEN}[+] Dossier {directory} créé{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}[*] Dossier {directory} existe déjà{Style.RESET_ALL}")

def check_modules():
    """Vérifie les modules requis"""
    required_modules = [
        'tkinter', 'flask', 'requests', 'user_agents', 'geocoder',
        'beautifulsoup4', 'paramiko', 'python-nmap', 'qrcode', 'PIL', 'colorama'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            if module == 'python-nmap':
                import nmap
            elif module == 'PIL':
                from PIL import Image
            else:
                __import__(module.replace('-', '_'))
            print(f"{Fore.GREEN}✅ {module}{Style.RESET_ALL}")
        except ImportError:
            print(f"{Fore.RED}❌ {module}{Style.RESET_ALL}")
            missing_modules.append(module)
    
    return missing_modules

def launch_gui():
    """Lance l'interface graphique"""
    print(f"{Fore.GREEN}[+] Lancement de l'interface graphique...{Style.RESET_ALL}")
    
    try:
        # Import avec gestion d'erreurs
        try:
            from ultimate_phishing_gui import UltimatePhishingGUI
        except ImportError as e:
            print(f"{Fore.RED}[!] Erreur import GUI: {e}{Style.RESET_ALL}")
            return False
        
        # Créer les dossiers
        create_directories()
        
        # Lancer l'application
        app = UltimatePhishingGUI()
        app.run()
        
        return True
        
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur lancement GUI: {e}{Style.RESET_ALL}")
        return False

def show_menu():
    """Affiche le menu principal"""
    print(f"\n{Fore.CYAN}🎯 MENU PRINCIPAL{Style.RESET_ALL}")
    print("=" * 50)
    print(f"{Fore.GREEN}1. 🖥️  Interface Graphique (Recommandé){Style.RESET_ALL}")
    print(f"{Fore.GREEN}2. 📦 Installer/Mettre à jour les dépendances{Style.RESET_ALL}")
    print(f"{Fore.GREEN}3. 🔍 Vérifier l'installation{Style.RESET_ALL}")
    print(f"{Fore.GREEN}4. 📁 Ouvrir le dossier du projet{Style.RESET_ALL}")
    print(f"{Fore.RED}0. 🚪 Quitter{Style.RESET_ALL}")
    print("=" * 50)

def check_installation():
    """Vérifie l'installation complète"""
    print(f"{Fore.YELLOW}[*] Vérification de l'installation...{Style.RESET_ALL}")
    
    # Vérifier Python
    if not check_python_version():
        return False
    
    # Vérifier les modules
    missing_modules = check_modules()
    
    if missing_modules:
        print(f"\n{Fore.RED}[!] Modules manquants: {', '.join(missing_modules)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Utilisez l'option 2 pour installer les dépendances{Style.RESET_ALL}")
        return False
    
    # Vérifier les fichiers
    required_files = [
        'ultimate_phishing_gui.py',
        'requirements.txt',
        'core/phishing_core.py',
        'core/advanced_attacks.py',
        'core/site_cloner.py',
        'core/tunnel_manager.py',
        'core/wifi_attacks.py',
        'core/network_scanner.py',
        'core/payload_generator.py',
        'core/backdoor_creator.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
            print(f"{Fore.RED}❌ {file}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}✅ {file}{Style.RESET_ALL}")
    
    if missing_files:
        print(f"\n{Fore.RED}[!] Fichiers manquants: {', '.join(missing_files)}{Style.RESET_ALL}")
        return False
    
    print(f"\n{Fore.GREEN}[+] Installation complète et fonctionnelle!{Style.RESET_ALL}")
    return True

def open_project_folder():
    """Ouvre le dossier du projet"""
    import subprocess
    
    project_path = os.path.abspath(".")
    
    try:
        if platform.system() == "Windows":
            subprocess.run(["explorer", project_path])
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", project_path])
        else:  # Linux
            subprocess.run(["xdg-open", project_path])
        
        print(f"{Fore.GREEN}[+] Dossier ouvert: {project_path}{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur ouverture dossier: {e}{Style.RESET_ALL}")

def main():
    """Fonction principale"""
    try:
        print_banner()
        
        # Détecter l'OS
        os_type = detect_os()
        
        while True:
            show_menu()
            choice = input(f"{Fore.YELLOW}[?] Votre choix: {Style.RESET_ALL}")
            
            if choice == "1":
                # Vérifier l'installation d'abord
                if check_installation():
                    launch_gui()
                else:
                    print(f"{Fore.RED}[!] Installation incomplète. Utilisez l'option 2.{Style.RESET_ALL}")
                    
            elif choice == "2":
                if install_dependencies():
                    print(f"{Fore.GREEN}[+] Dépendances installées. Vous pouvez maintenant lancer l'interface.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[!] Échec de l'installation des dépendances.{Style.RESET_ALL}")
                    
            elif choice == "3":
                check_installation()
                
            elif choice == "4":
                open_project_folder()
                
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