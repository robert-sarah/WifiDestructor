#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎣 ULTIMATE PHISHING TOOL v4.0 - GUI
Interface Tkinter moderne pour le pentest avancé
"""

import tkinter as tk
from tkinter import BOTH, X, ttk, messagebox, filedialog, scrolledtext, simpledialog
import threading
import os
import json
import time
from datetime import datetime
import webbrowser

# Import des modules avec gestion d'erreurs cross-platform
import sys
import platform
import subprocess

def check_system_dependencies():
    """Vérifie les dépendances système selon l'OS"""
    os_type = platform.system().lower()
    missing_tools = []
    optional_tools = []
    
    # Outils CRITIQUES selon l'OS (nécessaires pour le bon fonctionnement)
    critical_tools = {
        'linux': ['nmap'],  # Seul nmap est critique
        'darwin': ['nmap'],  # macOS - seul nmap est critique
        'windows': ['nmap']  # Windows - seul nmap est critique
    }
    
    # Outils OPTIONNELS selon l'OS (améliorent les fonctionnalités)
    optional_tools_list = {
        'linux': ['aircrack-ng', 'masscan'],
        'darwin': ['aircrack-ng', 'masscan'],
        'windows': ['aircrack-ng', 'masscan']  # Optionnel sur Windows
    }
    
    critical_to_check = critical_tools.get(os_type, [])
    optional_to_check = optional_tools_list.get(os_type, [])
    
    print("🔍 Vérification des outils critiques...")
    
    # Vérifier les outils critiques
    for tool in critical_to_check:
        if check_tool_availability(tool, "critique"):
            pass  # Outil disponible
        else:
            missing_tools.append(tool)
    
    print("\n🔍 Vérification des outils optionnels...")
    
    # Vérifier les outils optionnels
    for tool in optional_to_check:
        if check_tool_availability(tool, "optionnel"):
            pass  # Outil disponible
        else:
            optional_tools.append(tool)
    
    # Afficher un résumé
    if missing_tools:
        print(f"\n⚠️ Outils critiques manquants: {', '.join(missing_tools)}")
        print("💡 Ces outils sont nécessaires pour le bon fonctionnement")
    else:
        print("\n✅ Tous les outils critiques sont disponibles")
    
    if optional_tools:
        print(f"📋 Outils optionnels non disponibles: {', '.join(optional_tools)}")
        print("💡 Ces outils améliorent les fonctionnalités mais ne sont pas critiques")
    
    return missing_tools, optional_tools

def check_tool_availability(tool, tool_type):
    """Vérifie si un outil est disponible avec plusieurs méthodes"""
    # Essayer différentes commandes de vérification
    version_commands = [
        [tool, '--version'],
        [tool, '-V'],
        [tool, '--help'],
        [tool, 'version'],
        [tool, '--v'],
        [tool, '-h']
    ]
    
    for cmd in version_commands:
        try:
            result = subprocess.run(cmd, 
                                 capture_output=True, 
                                 check=True, 
                                 timeout=3)
            print(f"✅ {tool} disponible ({tool_type})")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            continue
    
    # Si aucune commande n'a fonctionné, essayer avec 'which' (Linux/macOS)
    if platform.system().lower() in ['linux', 'darwin']:
        try:
            result = subprocess.run(['which', tool], 
                                 capture_output=True, 
                                 check=True, 
                                 timeout=2)
            print(f"✅ {tool} disponible ({tool_type})")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            pass
    
    # Si aucune méthode n'a fonctionné
    if tool_type == "critique":
        print(f"❌ {tool} manquant (CRITIQUE)")
    else:
        print(f"⚠️ {tool} non disponible (optionnel)")
    
    return False

def install_dependencies():
    """Installe les dépendances manquantes"""
    try:
        # Vérifier les dépendances système
        missing_critical, missing_optional = check_system_dependencies()
        
        # Seulement signaler les outils critiques manquants
        if missing_critical:
            print(f"⚠️ Outils critiques manquants: {', '.join(missing_critical)}")
            print("📦 Installation des dépendances Python...")
        
        # Installer les dépendances Python
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dépendances Python installées avec succès")
        
        # Instructions pour les outils critiques manquants
        if missing_critical:
            os_type = platform.system().lower()
            print("\n📋 Instructions d'installation des outils critiques:")
            
            if os_type in ['linux', 'darwin']:
                print("  Debian/Ubuntu: sudo apt-get install nmap")
                print("  macOS: brew install nmap")
            elif os_type == 'windows':
                print("  Windows: Téléchargez nmap depuis https://nmap.org/download.html")
        
        # Instructions pour les outils optionnels (informatives seulement)
        if missing_optional:
            os_type = platform.system().lower()
            print(f"\n📋 Outils optionnels non disponibles: {', '.join(missing_optional)}")
            print("💡 Ces outils améliorent les fonctionnalités mais ne sont pas critiques")
            
            if os_type in ['linux', 'darwin']:
                print("  Pour installer les outils optionnels:")
                print("  Debian/Ubuntu: sudo apt-get install aircrack-ng masscan")
                print("  macOS: brew install aircrack-ng masscan")
            elif os_type == 'windows':
                print("  Windows: Ces outils sont optionnels sur Windows")
        
    except Exception as e:
        print(f"❌ Erreur installation: {e}")
        print("💡 Essayez d'exécuter: bash install.sh")

# Import des modules avec gestion d'erreurs
try:
    from core.phishing_core import PhishingCore
    from core.advanced_attacks import AdvancedAttacks
    from core.site_cloner import SiteCloner
    from core.tunnel_manager import TunnelManager
    from core.wifi_attacks import WifiAttacks
    from core.network_scanner import NetworkScanner
    from core.payload_generator import PayloadGenerator
    from core.backdoor_creator import BackdoorCreator
    from core.exploit_framework import ExploitFramework
    from core.social_engineering import SocialEngineering
    from core.stealth_operations import StealthOperations
    from core.advanced_malware import AdvancedMalware
    from core.zero_day_exploits import ZeroDayExploits
    from core.advanced_persistence import AdvancedPersistence
    from core.web_exploitation import WebExploitation
    from core.osint_framework import OSINTFramework
    from core.active_directory import ActiveDirectoryAttacks
except ImportError as e:
    print(f"❌ Erreur import: {e}")
    print("📦 Installation des modules manquants...")
    install_dependencies()
    # Réessayer l'import
    try:
        from core.phishing_core import PhishingCore
        from core.advanced_attacks import AdvancedAttacks
        from core.site_cloner import SiteCloner
        from core.tunnel_manager import TunnelManager
        from core.wifi_attacks import WifiAttacks
        from core.network_scanner import NetworkScanner
        from core.payload_generator import PayloadGenerator
        from core.backdoor_creator import BackdoorCreator
        from core.exploit_framework import ExploitFramework
        from core.social_engineering import SocialEngineering
        from core.stealth_operations import StealthOperations
        from core.advanced_malware import AdvancedMalware
        from core.zero_day_exploits import ZeroDayExploits
        from core.advanced_persistence import AdvancedPersistence
        from core.web_exploitation import WebExploitation
        from core.osint_framework import OSINTFramework
        from core.active_directory import ActiveDirectoryAttacks
    except ImportError:
        print("❌ Impossible de charger les modules. Vérifiez l'installation.")
        sys.exit(1)

class UltimatePhishingGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎣 ULTIMATE PHISHING TOOL v4.0")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1e1e1e')
        
        # Détection du système d'exploitation
        self.os_type = platform.system().lower()
        print(f"🖥️ Système détecté: {self.os_type}")
        
        # Vérification des permissions et dépendances
        self.check_permissions_and_dependencies()
        
        # Initialisation des modules avec gestion d'erreurs
        try:
            self.phishing = PhishingCore()
            self.attacks = AdvancedAttacks()
            self.cloner = SiteCloner()
            self.tunnels = TunnelManager()
            self.wifi = WifiAttacks()
            self.scanner = NetworkScanner()
            self.payload = PayloadGenerator()
            self.backdoor = BackdoorCreator()
            self.exploit = ExploitFramework()
            self.social = SocialEngineering()
            self.stealth = StealthOperations()
            self.malware = AdvancedMalware()
            self.zero_day = ZeroDayExploits()
            self.persistence = AdvancedPersistence()
            self.web_exploit = WebExploitation()
            self.osint = OSINTFramework()
            self.ad_attacks = ActiveDirectoryAttacks()
        except Exception as e:
            print(f"❌ Erreur initialisation modules: {e}")
            messagebox.showerror("Erreur", f"Erreur initialisation: {e}")
        
        # Variables
        self.server_running = False
        self.selected_template = None
        self.current_tunnel = None
        
        # Style moderne
        self.setup_styles()
        
        # Interface
        self.setup_ui()
        
        # Démarrer les mises à jour
        self.update_stats()
        
    def check_permissions_and_dependencies(self):
        """Vérifie les permissions et dépendances selon l'OS"""
        print("🔍 Vérification des permissions et dépendances...")
        
        # Vérifier les permissions selon l'OS
        if self.os_type in ['linux', 'darwin']:
            # Vérifier si on peut exécuter des commandes système
            try:
                result = subprocess.run(['whoami'], capture_output=True, text=True, timeout=5)
                current_user = result.stdout.strip()
                print(f"👤 Utilisateur actuel: {current_user}")
                
                # Vérifier les permissions WiFi
                if self.os_type == 'linux':
                    try:
                        # Vérifier si l'utilisateur est dans le groupe netdev
                        result = subprocess.run(['groups'], capture_output=True, text=True, timeout=5)
                        groups = result.stdout.strip()
                        if 'netdev' in groups:
                            print("✅ Permissions WiFi configurées")
                        else:
                            print("⚠️ Permissions WiFi limitées - certaines fonctionnalités nécessitent sudo")
                    except Exception as e:
                        print(f"⚠️ Impossible de vérifier les groupes: {e}")
                        
            except Exception as e:
                print(f"⚠️ Erreur vérification utilisateur: {e}")
                
        elif self.os_type == 'windows':
            # Vérifier les permissions Windows
            try:
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin()
                if is_admin:
                    print("✅ Exécution en tant qu'administrateur")
                else:
                    print("⚠️ Exécution en tant qu'utilisateur normal - certaines fonctionnalités peuvent être limitées")
            except Exception as e:
                print(f"⚠️ Impossible de vérifier les permissions Windows: {e}")
        
        # Vérifier les dépendances système
        missing_critical, missing_optional = check_system_dependencies()
        if missing_critical:
            print(f"⚠️ Outils critiques manquants: {', '.join(missing_critical)}")
            print("💡 Ces outils sont nécessaires pour le bon fonctionnement")
            print("💡 Exécutez 'bash install.sh' pour installer automatiquement")
        else:
            print("✅ Tous les outils critiques sont disponibles")
        
        if missing_optional:
            print(f"📋 Outils optionnels non disponibles: {', '.join(missing_optional)}")
            print("💡 Ces outils améliorent les fonctionnalités mais ne sont pas critiques")
        
    def setup_styles(self):
        """Configure les styles modernes"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Couleurs
        self.colors = {
            'bg': '#1e1e1e',
            'fg': '#ffffff',
            'accent': '#00ff88',
            'secondary': '#2d2d2d',
            'danger': '#ff4444',
            'warning': '#ffaa00',
            'success': '#00ff88'
        }
        
        # Configuration des styles
        style.configure('Title.TLabel', 
                       background=self.colors['bg'], 
                       foreground=self.colors['accent'],
                       font=('Arial', 16, 'bold'))
        
        style.configure('Card.TFrame', 
                       background=self.colors['secondary'],
                       relief='raised',
                       borderwidth=2)
        
        style.configure('Success.TButton',
                       background=self.colors['success'],
                       foreground='black')
        
        style.configure('Danger.TButton',
                       background=self.colors['danger'],
                       foreground='white')
        
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Titre
        title_label = tk.Label(main_frame, 
                              text="🎣 ULTIMATE PHISHING TOOL v4.0",
                              font=('Arial', 20, 'bold'),
                              bg=self.colors['bg'],
                              fg=self.colors['accent'])
        title_label.pack(pady=(0, 20))
        
        # Notebook pour les onglets
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill='both', expand=True)
        
        # Onglets
        self.setup_phishing_tab()
        self.setup_clone_tab()
        self.setup_wifi_tab()
        self.setup_network_tab()
        self.setup_payload_tab()
        self.setup_backdoor_tab()
        self.setup_attacks_tab()
        self.setup_tunnels_tab()
        self.setup_stats_tab()
        self.setup_settings_tab()
        self.setup_exploit_tab()
        self.setup_social_tab()
        self.setup_stealth_tab()
        self.setup_malware_tab()
        self.setup_zero_day_tab()
        self.setup_persistence_tab()
        self.setup_web_exploitation_tab()
        self.setup_osint_tab()
        self.setup_ad_tab()
        
    def setup_phishing_tab(self):
        """Onglet phishing classique"""
        phishing_frame = ttk.Frame(self.notebook)
        self.notebook.add(phishing_frame, text="🎯 Phishing")
        
        # Frame gauche - Templates
        left_frame = ttk.Frame(phishing_frame)
        left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        # Titre templates
        tk.Label(left_frame, text="📋 Templates Disponibles", 
                font=('Arial', 14, 'bold'),
                bg=self.colors['bg'], fg=self.colors['fg']).pack(pady=(0, 10))
        
        # Liste des templates
        self.template_listbox = tk.Listbox(left_frame, 
                                          bg=self.colors['secondary'],
                                          fg=self.colors['fg'],
                                          selectbackground=self.colors['accent'],
                                          height=15)
        self.template_listbox.pack(fill='both', expand=True)
        
        # Boutons templates
        template_buttons_frame = tk.Frame(left_frame, bg=self.colors['bg'])
        template_buttons_frame.pack(fill='x', pady=10)
        
        tk.Button(template_buttons_frame, text="🔄 Actualiser", 
                 command=self.refresh_templates,
                 bg=self.colors['accent'], fg='black').pack(side='left', padx=5)
        
        tk.Button(template_buttons_frame, text="📁 Ouvrir Dossier", 
                 command=self.open_templates_folder,
                 bg=self.colors['secondary'], fg=self.colors['fg']).pack(side='left', padx=5)
        
        # Frame droite - Serveur
        right_frame = ttk.Frame(phishing_frame)
        right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        
        # Configuration serveur
        server_frame = ttk.LabelFrame(right_frame, text="⚙️ Configuration Serveur")
        server_frame.pack(fill='x', pady=(0, 10))
        
        # Host
        tk.Label(server_frame, text="Host:", bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w')
        self.host_entry = tk.Entry(server_frame, bg=self.colors['secondary'], fg=self.colors['fg'])
        self.host_entry.insert(0, "0.0.0.0")
        self.host_entry.pack(fill='x', pady=(0, 10))
        
        # Port
        tk.Label(server_frame, text="Port:", bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w')
        self.port_entry = tk.Entry(server_frame, bg=self.colors['secondary'], fg=self.colors['fg'])
        self.port_entry.insert(0, "8080")
        self.port_entry.pack(fill='x', pady=(0, 10))
        
        # Boutons serveur
        server_buttons_frame = tk.Frame(server_frame, bg=self.colors['bg'])
        server_buttons_frame.pack(fill='x', pady=10)
        
        self.start_server_btn = tk.Button(server_buttons_frame, text="🚀 Démarrer Serveur",
                                         command=self.start_server,
                                         bg=self.colors['success'], fg='black')
        self.start_server_btn.pack(side='left', padx=5)
        
        self.stop_server_btn = tk.Button(server_buttons_frame, text="⏹️ Arrêter Serveur",
                                        command=self.stop_server,
                                        bg=self.colors['danger'], fg='white',
                                        state='disabled')
        self.stop_server_btn.pack(side='left', padx=5)
        
        # URL du serveur
        self.server_url_label = tk.Label(server_frame, text="URL: Non démarré",
                                        bg=self.colors['bg'], fg=self.colors['warning'])
        self.server_url_label.pack(pady=10)
        
        # Charger les templates
        self.refresh_templates()
         
    def setup_wifi_tab(self):
        """Onglet attaques WiFi"""
        wifi_frame = ttk.Frame(self.notebook)
        self.notebook.add(wifi_frame, text="📡 WiFi")
        
        # Frame principale
        main_wifi_frame = tk.Frame(wifi_frame, bg=self.colors['bg'])
        main_wifi_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Titre
        tk.Label(main_wifi_frame, text="📡 Attaques WiFi Avancées",
                font=('Arial', 16, 'bold'),
                bg=self.colors['bg'], fg=self.colors['accent']).pack(pady=(0, 20))
        
        # Configuration WiFi
        wifi_config_frame = ttk.LabelFrame(main_wifi_frame, text="⚙️ Configuration WiFi")
        wifi_config_frame.pack(fill='x', pady=(0, 20))
        
        # Interface WiFi
        tk.Label(wifi_config_frame, text="Interface WiFi:", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10)
        
        self.wifi_interface_entry = tk.Entry(wifi_config_frame, bg=self.colors['secondary'], fg=self.colors['fg'])
        self.wifi_interface_entry.pack(fill='x', padx=10, pady=5)
        self.wifi_interface_entry.insert(0, "wlan0" if self.os_type != "windows" else "Wi-Fi")
        
        # Boutons WiFi
        wifi_buttons_frame = tk.Frame(main_wifi_frame, bg=self.colors['bg'])
        wifi_buttons_frame.pack(fill='x', pady=(0, 20))
        
        wifi_buttons = [
            ("📡 Scan Réseaux", self.scan_wifi_networks),
            ("💀 Deauth Attack", self.deauth_attack),
            ("🤝 Capture Handshake", self.capture_handshake),
            ("🔓 Crack Handshake", self.crack_handshake),
            ("📡 Fake AP", self.create_fake_ap),
            ("👿 Evil Twin", self.evil_twin_attack),
            ("🔑 WPS Attack", self.wps_attack)
        ]
        
        for i, (text, command) in enumerate(wifi_buttons):
            btn = tk.Button(wifi_buttons_frame, text=text, command=command,
                           bg=self.colors['accent'], fg='black',
                           font=('Arial', 10, 'bold'))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5, sticky='ew')
        
        wifi_buttons_frame.grid_columnconfigure(0, weight=1)
        wifi_buttons_frame.grid_columnconfigure(1, weight=1)
        wifi_buttons_frame.grid_columnconfigure(2, weight=1)
        
        # Log WiFi
        wifi_log_frame = ttk.LabelFrame(main_wifi_frame, text="📋 Log WiFi")
        wifi_log_frame.pack(fill='both', expand=True)
        
        self.wifi_log = scrolledtext.ScrolledText(wifi_log_frame, 
                                                 bg=self.colors['secondary'],
                                                 fg=self.colors['fg'],
                                                 height=10)
        self.wifi_log.pack(fill='both', expand=True, padx=10, pady=10)
         
    def setup_network_tab(self):
        """Onglet scan réseau"""
        network_frame = ttk.Frame(self.notebook)
        self.notebook.add(network_frame, text="🌐 Network")
         
        # Frame principale
        main_network_frame = tk.Frame(network_frame, bg=self.colors['bg'])
        main_network_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Titre
        tk.Label(main_network_frame, text="🌐 Scanner Réseau Avancé",
                font=('Arial', 16, 'bold'),
                bg=self.colors['bg'], fg=self.colors['accent']).pack(pady=(0, 20))
        
        # Configuration réseau
        network_config_frame = ttk.LabelFrame(main_network_frame, text="🎯 Configuration")
        network_config_frame.pack(fill='x', pady=(0, 20))
        
        # Cible
        tk.Label(network_config_frame, text="Cible (IP/réseau):", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10)
        
        self.network_target_entry = tk.Entry(network_config_frame, bg=self.colors['secondary'], fg=self.colors['fg'])
        self.network_target_entry.pack(fill='x', padx=10, pady=5)
        self.network_target_entry.insert(0, "192.168.1.0/24")
        
        # Boutons réseau
        network_buttons_frame = tk.Frame(main_network_frame, bg=self.colors['bg'])
        network_buttons_frame.pack(fill='x', pady=(0, 20))
        
        network_buttons = [
            ("🔍 Quick Scan", self.quick_network_scan),
            ("🔍 Full Scan", self.full_network_scan),
            ("⚡ Masscan", self.masscan_scan),
            ("🔍 Service Enum", self.service_enumeration),
            ("🌐 Web Enum", self.web_enumeration),
            ("🔍 DNS Enum", self.dns_enumeration),
            ("🔍 Subdomain Enum", self.subdomain_enumeration),
            ("🔍 Vuln Scan", self.vulnerability_scan)
        ]
        
        for i, (text, command) in enumerate(network_buttons):
            btn = tk.Button(network_buttons_frame, text=text, command=command,
                           bg=self.colors['accent'], fg='black',
                           font=('Arial', 10, 'bold'))
            btn.grid(row=i//4, column=i%4, padx=5, pady=5, sticky='ew')
        
        for i in range(4):
            network_buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Log réseau
        network_log_frame = ttk.LabelFrame(main_network_frame, text="📋 Log Réseau")
        network_log_frame.pack(fill='both', expand=True)
        
        self.network_log = scrolledtext.ScrolledText(network_log_frame, 
                                                    bg=self.colors['secondary'],
                                                    fg=self.colors['fg'],
                                                    height=10)
        self.network_log.pack(fill='both', expand=True, padx=10, pady=10)
         
    def setup_payload_tab(self):
        """Onglet génération de payloads"""
        payload_frame = ttk.Frame(self.notebook)
        self.notebook.add(payload_frame, text="💣 Payloads")
         
        # Frame principale
        main_payload_frame = tk.Frame(payload_frame, bg=self.colors['bg'])
        main_payload_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Titre
        tk.Label(main_payload_frame, text="💣 Générateur de Payloads",
                font=('Arial', 16, 'bold'),
                bg=self.colors['bg'], fg=self.colors['accent']).pack(pady=(0, 20))
        
        # Configuration payload
        payload_config_frame = ttk.LabelFrame(main_payload_frame, text="⚙️ Configuration")
        payload_config_frame.pack(fill='x', pady=(0, 20))
        
        # LHOST
        tk.Label(payload_config_frame, text="LHOST:", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10)
        
        self.lhost_entry = tk.Entry(payload_config_frame, bg=self.colors['secondary'], fg=self.colors['fg'])
        self.lhost_entry.pack(fill='x', padx=10, pady=5)
        self.lhost_entry.insert(0, "192.168.1.100")
        
        # LPORT
        tk.Label(payload_config_frame, text="LPORT:", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10)
        
        self.lport_entry = tk.Entry(payload_config_frame, bg=self.colors['secondary'], fg=self.colors['fg'])
        self.lport_entry.pack(fill='x', padx=10, pady=5)
        self.lport_entry.insert(0, "4444")
        
        # Boutons payload
        payload_buttons_frame = tk.Frame(main_payload_frame, bg=self.colors['bg'])
        payload_buttons_frame.pack(fill='x', pady=(0, 20))
        
        payload_buttons = [
            ("🖥️ Windows Reverse", lambda: self.generate_payload("windows_reverse")),
            ("🐧 Linux Reverse", lambda: self.generate_payload("linux_reverse")),
            ("📱 Android Reverse", lambda: self.generate_payload("android_reverse")),
            ("🖥️ Windows Bind", lambda: self.generate_payload("windows_bind")),
            ("🐧 Linux Bind", lambda: self.generate_payload("linux_bind")),
            ("🌐 PHP Web Shell", lambda: self.generate_payload("php_webshell")),
            ("💻 PowerShell", lambda: self.generate_payload("powershell")),
            ("🐍 Python", lambda: self.generate_payload("python"))
        ]
        
        for i, (text, command) in enumerate(payload_buttons):
            btn = tk.Button(payload_buttons_frame, text=text, command=command,
                           bg=self.colors['accent'], fg='black',
                           font=('Arial', 10, 'bold'))
            btn.grid(row=i//4, column=i%4, padx=5, pady=5, sticky='ew')
        
        for i in range(4):
            payload_buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Log payload
        payload_log_frame = ttk.LabelFrame(main_payload_frame, text="📋 Log Payloads")
        payload_log_frame.pack(fill='both', expand=True)
        
        self.payload_log = scrolledtext.ScrolledText(payload_log_frame, 
                                                    bg=self.colors['secondary'],
                                                    fg=self.colors['fg'],
                                                    height=10)
        self.payload_log.pack(fill='both', expand=True, padx=10, pady=10)
         
    def setup_backdoor_tab(self):
        """Onglet création de backdoors"""
        backdoor_frame = ttk.Frame(self.notebook)
        self.notebook.add(backdoor_frame, text="🚪 Backdoors")
        
        # Frame principale
        main_backdoor_frame = tk.Frame(backdoor_frame, bg=self.colors['bg'])
        main_backdoor_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Titre
        tk.Label(main_backdoor_frame, text="🚪 Créateur de Backdoors",
                 font=('Arial', 16, 'bold'),
                 bg=self.colors['bg'], fg=self.colors['accent']).pack(pady=(0, 20))
        
        # Configuration backdoor
        backdoor_config_frame = ttk.LabelFrame(main_backdoor_frame, text="⚙️ Configuration")
        backdoor_config_frame.pack(fill='x', pady=(0, 20))
        
        # LHOST
        tk.Label(backdoor_config_frame, text="LHOST:", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10)
        
        self.backdoor_lhost_entry = tk.Entry(backdoor_config_frame, bg=self.colors['secondary'], fg=self.colors['fg'])
        self.backdoor_lhost_entry.pack(fill='x', padx=10, pady=5)
        self.backdoor_lhost_entry.insert(0, "192.168.1.100")
        
        # LPORT
        tk.Label(backdoor_config_frame, text="LPORT:", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10)
        
        self.backdoor_lport_entry = tk.Entry(backdoor_config_frame, bg=self.colors['secondary'], fg=self.colors['fg'])
        self.backdoor_lport_entry.pack(fill='x', padx=10, pady=5)
        self.backdoor_lport_entry.insert(0, "4444")
        
        # Boutons backdoor
        backdoor_buttons_frame = tk.Frame(main_backdoor_frame, bg=self.colors['bg'])
        backdoor_buttons_frame.pack(fill='x', pady=(0, 20))
        
        backdoor_buttons = [
            ("🖥️ Windows Registry", lambda: self.create_backdoor("windows_registry")),
            ("🖥️ Windows Service", lambda: self.create_backdoor("windows_service")),
            ("🐧 Linux Cron", lambda: self.create_backdoor("linux_cron")),
            ("🐧 Linux Service", lambda: self.create_backdoor("linux_service")),
            ("🖥️ Windows Persistent", lambda: self.create_backdoor("windows_persistent")),
            ("🐧 Linux Persistent", lambda: self.create_backdoor("linux_persistent")),
            ("🐧 Linux Rootkit", lambda: self.create_backdoor("linux_rootkit"))
        ]
        
        for i, (text, command) in enumerate(backdoor_buttons):
            btn = tk.Button(backdoor_buttons_frame, text=text, command=command,
                           bg=self.colors['accent'], fg='black',
                           font=('Arial', 10, 'bold'))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5, sticky='ew')
        
        for i in range(3):
            backdoor_buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Log backdoor
        backdoor_log_frame = ttk.LabelFrame(main_backdoor_frame, text="📋 Log Backdoors")
        backdoor_log_frame.pack(fill='both', expand=True)
        
        self.backdoor_log = scrolledtext.ScrolledText(backdoor_log_frame, 
                                                     bg=self.colors['secondary'],
                                                     fg=self.colors['fg'],
                                                     height=10)
        self.backdoor_log.pack(fill='both', expand=True, padx=10, pady=10)
         
    # Méthodes WiFi
    def scan_wifi_networks(self):
        """Scan des réseaux WiFi"""
        def scan_thread():
            try:
                self.wifi_log.insert(tk.END, "📡 Scan des réseaux WiFi...\n")
                self.wifi_log.see(tk.END)
                networks = self.wifi.scan_wifi_networks()
                
                if networks:
                    self.wifi_log.insert(tk.END, f"✅ {len(networks)} réseaux trouvés:\n")
                    for network in networks:
                        self.wifi_log.insert(tk.END, f"  📶 {network.get('essid', 'Unknown')} - {network.get('encryption', 'Unknown')}\n")
                else:
                    self.wifi_log.insert(tk.END, "❌ Aucun réseau trouvé\n")
                    
                self.wifi_log.see(tk.END)
                
            except Exception as e:
                self.wifi_log.insert(tk.END, f"❌ Erreur: {e}\n")
                self.wifi_log.see(tk.END)
                
        threading.Thread(target=scan_thread, daemon=True).start()
         
    def deauth_attack(self):
        """Attaque de déauthentification"""
        target = tk.simpledialog.askstring("🎯 Cible", "Adresse MAC de la cible:")
        if target:
            def deauth_thread():
                try:
                    self.wifi_log.insert(tk.END, f"💀 Deauth attack sur {target}...\n")
                    self.wifi_log.see(tk.END)
                    
                    # Vérifier les permissions selon l'OS
                    if self.os_type in ['linux', 'darwin']:
                        try:
                            result = subprocess.run(['whoami'], capture_output=True, text=True, timeout=5)
                            if result.stdout.strip() != 'root':
                                self.wifi_log.insert(tk.END, "⚠️ Permissions insuffisantes - certaines fonctionnalités peuvent échouer\n")
                                self.wifi_log.insert(tk.END, "💡 Essayez d'exécuter en tant qu'administrateur\n")
                        except Exception:
                            pass
                    elif self.os_type == 'windows':
                        try:
                            import ctypes
                            if not ctypes.windll.shell32.IsUserAnAdmin():
                                self.wifi_log.insert(tk.END, "⚠️ Exécution en tant qu'utilisateur normal - fonctionnalités limitées\n")
                        except Exception:
                            pass
                    
                    interface = self.wifi_interface_entry.get()
                    result = self.wifi.deauth_attack(target, interface)
                    
                    if result:
                        self.wifi_log.insert(tk.END, "✅ Deauth attack lancée\n")
                    else:
                        self.wifi_log.insert(tk.END, "❌ Erreur deauth attack\n")
                        
                    self.wifi_log.see(tk.END)
                    
                except Exception as e:
                    self.wifi_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    if "Permission denied" in str(e) or "Operation not permitted" in str(e):
                        self.wifi_log.insert(tk.END, "💡 Essayez d'exécuter en tant qu'administrateur\n")
                    elif "No such device" in str(e):
                        self.wifi_log.insert(tk.END, "💡 Vérifiez que l'interface WiFi est correcte\n")
                    self.wifi_log.see(tk.END)
                    
            threading.Thread(target=deauth_thread, daemon=True).start()
             
    def capture_handshake(self):
        """Capture de handshake"""
        target = tk.simpledialog.askstring("🎯 Cible", "SSID de la cible:")
        if target:
            def capture_thread():
                try:
                    self.wifi_log.insert(tk.END, f"🤝 Capture handshake: {target}...\n")
                    self.wifi_log.see(tk.END)
                    
                    interface = self.wifi_interface_entry.get()
                    result = self.wifi.capture_handshake(target, interface)
                    
                    if result:
                        self.wifi_log.insert(tk.END, f"✅ Handshake capturé: {result}\n")
                    else:
                        self.wifi_log.insert(tk.END, "❌ Erreur capture handshake\n")
                        
                    self.wifi_log.see(tk.END)
                    
                except Exception as e:
                    self.wifi_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    self.wifi_log.see(tk.END)
                    
                threading.Thread(target=capture_thread, daemon=True).start()
             
    def crack_handshake(self):
        """Crack de handshake"""
        filename = filedialog.askopenfilename(title="📁 Sélectionner fichier handshake")
        if filename:
            def crack_thread():
                try:
                    self.wifi_log.insert(tk.END, f"🔓 Crack handshake: {filename}...\n")
                    self.wifi_log.see(tk.END)
                    
                    password = self.wifi.crack_wpa_handshake(filename)
                    
                    if password:
                        self.wifi_log.insert(tk.END, f"✅ Mot de passe trouvé: {password}\n")
                    else:
                        self.wifi_log.insert(tk.END, "❌ Mot de passe non trouvé\n")
                        
                    self.wifi_log.see(tk.END)
                    
                except Exception as e:
                    self.wifi_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    self.wifi_log.see(tk.END)
                    
            threading.Thread(target=crack_thread, daemon=True).start()
             
    def create_fake_ap(self):
        """Crée un point d'accès factice"""
        ssid = tk.simpledialog.askstring("📡 SSID", "Nom du point d'accès:")
        if ssid:
            def fake_ap_thread():
                try:
                    self.wifi_log.insert(tk.END, f"📡 Création AP factice: {ssid}...\n")
                    self.wifi_log.see(tk.END)
                    
                    interface = self.wifi_interface_entry.get()
                    result = self.wifi.create_fake_ap(ssid, interface)
                    
                    if result:
                        self.wifi_log.insert(tk.END, "✅ AP factice créé\n")
                    else:
                        self.wifi_log.insert(tk.END, "❌ Erreur création AP factice\n")
                        
                    self.wifi_log.see(tk.END)
                    
                except Exception as e:
                    self.wifi_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    self.wifi_log.see(tk.END)
                    
            threading.Thread(target=fake_ap_thread, daemon=True).start()
            
    def evil_twin_attack(self):
        """Attaque Evil Twin"""
        target = tk.simpledialog.askstring("🎯 Cible", "SSID de la cible:")
        if target:
            def evil_twin_thread():
                try:
                    self.wifi_log.insert(tk.END, f"👿 Evil Twin attack: {target}...\n")
                    self.wifi_log.see(tk.END)
                    
                    interface = self.wifi_interface_entry.get()
                    result = self.wifi.evil_twin_attack(target, interface)
                    
                    if result:
                        self.wifi_log.insert(tk.END, "✅ Evil Twin attack lancée\n")
                    else:
                        self.wifi_log.insert(tk.END, "❌ Erreur Evil Twin attack\n")
                        
                    self.wifi_log.see(tk.END)
                    
                except Exception as e:
                    self.wifi_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    self.wifi_log.see(tk.END)
                    
            threading.Thread(target=evil_twin_thread, daemon=True).start()
            
    def wps_attack(self):
        """Attaque WPS"""
        target = tk.simpledialog.askstring("🎯 Cible", "Adresse MAC de la cible:")
        if target:
            def wps_thread():
                try:
                    self.wifi_log.insert(tk.END, f"🔑 WPS attack: {target}...\n")
                    self.wifi_log.see(tk.END)
                    
                    interface = self.wifi_interface_entry.get()
                    result = self.wifi.wps_attack(target, interface)
                    
                    if result:
                        self.wifi_log.insert(tk.END, "✅ WPS attack lancée\n")
                    else:
                        self.wifi_log.insert(tk.END, "❌ Erreur WPS attack\n")
                        
                    self.wifi_log.see(tk.END)
                    
                except Exception as e:
                    self.wifi_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    self.wifi_log.see(tk.END)
                    
                threading.Thread(target=wps_thread, daemon=True).start()
         
    # Méthodes Network
    def quick_network_scan(self):
        """Scan réseau rapide"""
        target = self.network_target_entry.get()
        if target:
            def scan_thread():
                try:
                    self.network_log.insert(tk.END, f"🔍 Quick scan: {target}...\n")
                    self.network_log.see(tk.END)
                    
                    result = self.scanner.quick_scan(target)
                    
                    if result:
                        self.network_log.insert(tk.END, f"✅ Scan terminé - {len(result.get('hosts', []))} hôtes trouvés\n")
                    else:
                        self.network_log.insert(tk.END, "❌ Erreur scan\n")
                        
                    self.network_log.see(tk.END)
                    
                except Exception as e:
                    self.network_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    self.network_log.see(tk.END)
                    
            threading.Thread(target=scan_thread, daemon=True).start()
             
    def full_network_scan(self):
        """Scan réseau complet"""
        target = self.network_target_entry.get()
        if target:
            def scan_thread():
                try:
                    self.network_log.insert(tk.END, f"🔍 Full scan: {target}...\n")
                    self.network_log.see(tk.END)
                    
                    result = self.scanner.full_scan(target)
                    
                    if result:
                        self.network_log.insert(tk.END, f"✅ Scan complet terminé\n")
                    else:
                        self.network_log.insert(tk.END, "❌ Erreur scan complet\n")
                        
                    self.network_log.see(tk.END)
                    
                except Exception as e:
                    self.network_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    self.network_log.see(tk.END)
                    
            threading.Thread(target=scan_thread, daemon=True).start()
            
    def masscan_scan(self):
        """Scan avec masscan"""
        target = self.network_target_entry.get()
        if target:
            def scan_thread():
                try:
                    self.network_log.insert(tk.END, f"⚡ Masscan: {target}...\n")
                    self.network_log.see(tk.END)
                    
                    result = self.scanner.masscan_scan(target)
                    
                    if result:
                        self.network_log.insert(tk.END, "✅ Masscan terminé\n")
                    else:
                        self.network_log.insert(tk.END, "❌ Erreur masscan\n")
                        
                    self.network_log.see(tk.END)
                    
                except Exception as e:
                    self.network_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    self.network_log.see(tk.END)
                    
            threading.Thread(target=scan_thread, daemon=True).start()
            
    def service_enumeration(self):
        """Énumération des services"""
        target = tk.simpledialog.askstring("🎯 Cible", "Cible (IP:port):")
        if target:
            def enum_thread():
                try:
                    self.network_log.insert(tk.END, f"🔍 Service enum: {target}...\n")
                    self.network_log.see(tk.END)
                    
                    host, port = target.split(':')
                    result = self.scanner.service_enumeration(host, int(port))
                    
                    if result:
                        self.network_log.insert(tk.END, "✅ Service enum terminé\n")
                    else:
                        self.network_log.insert(tk.END, "❌ Erreur service enum\n")
                        
                    self.network_log.see(tk.END)
                    
                except Exception as e:
                    self.network_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    self.network_log.see(tk.END)
                    
                threading.Thread(target=enum_thread, daemon=True).start()
             
    def web_enumeration(self):
        """Énumération web"""
        target = self.network_target_entry.get()
        if target:
            def enum_thread():
                try:
                    self.network_log.insert(tk.END, f"🌐 Web enum: {target}...\n")
                    self.network_log.see(tk.END)
                    
                    result = self.scanner.web_enumeration(target)
                    
                    if result:
                        self.network_log.insert(tk.END, "✅ Web enum terminé\n")
                    else:
                        self.network_log.insert(tk.END, "❌ Erreur web enum\n")
                        
                    self.network_log.see(tk.END)
                    
                except Exception as e:
                    self.network_log.insert(tk.END, f"❌ Erreur: {e}\n")
                    self.network_log.see(tk.END)
                    
            threading.Thread(target=enum_thread, daemon=True).start()
             
    def dns_enumeration(self):
         """Énumération DNS"""
         domain = tk.simpledialog.askstring("🌐 Domaine", "Domaine à énumérer:")
         if domain:
             def enum_thread():
                 try:
                     self.network_log.insert(tk.END, f"🔍 DNS enum: {domain}...\n")
                     self.network_log.see(tk.END)
                     
                     result = self.scanner.dns_enumeration(domain)
                     
                     if result:
                         self.network_log.insert(tk.END, "✅ DNS enum terminé\n")
                     else:
                         self.network_log.insert(tk.END, "❌ Erreur DNS enum\n")
                         
                     self.network_log.see(tk.END)
                     
                 except Exception as e:
                     self.network_log.insert(tk.END, f"❌ Erreur: {e}\n")
                     self.network_log.see(tk.END)
                     
             threading.Thread(target=enum_thread, daemon=True).start()
             
    def subdomain_enumeration(self):
         """Énumération de sous-domaines"""
         domain = tk.simpledialog.askstring("🌐 Domaine", "Domaine pour sous-domaines:")
         if domain:
             def enum_thread():
                 try:
                     self.network_log.insert(tk.END, f"🔍 Subdomain enum: {domain}...\n")
                     self.network_log.see(tk.END)
                     
                     result = self.scanner.subdomain_enumeration(domain)
                     
                     if result:
                         self.network_log.insert(tk.END, "✅ Subdomain enum terminé\n")
                     else:
                         self.network_log.insert(tk.END, "❌ Erreur subdomain enum\n")
                         
                     self.network_log.see(tk.END)
                     
                 except Exception as e:
                     self.network_log.insert(tk.END, f"❌ Erreur: {e}\n")
                     self.network_log.see(tk.END)
                     
             threading.Thread(target=enum_thread, daemon=True).start()
             
    def vulnerability_scan(self):
         """Scan de vulnérabilités"""
         target = self.network_target_entry.get()
         if target:
             def scan_thread():
                 try:
                     self.network_log.insert(tk.END, f"🔍 Vuln scan: {target}...\n")
                     self.network_log.see(tk.END)
                     
                     result = self.scanner.vulnerability_scan(target)
                     
                     if result:
                         self.network_log.insert(tk.END, "✅ Vuln scan terminé\n")
                     else:
                         self.network_log.insert(tk.END, "❌ Erreur vuln scan\n")
                         
                     self.network_log.see(tk.END)
                     
                 except Exception as e:
                     self.network_log.insert(tk.END, f"❌ Erreur: {e}\n")
                     self.network_log.see(tk.END)
                     
             threading.Thread(target=scan_thread, daemon=True).start()
         
    # Méthodes Payload
    def generate_payload(self, payload_type):
        """Génère un payload"""
        lhost = self.lhost_entry.get()
        lport = self.lport_entry.get()
         
        if not lhost or not lport:
            messagebox.showerror("❌ Erreur", "Veuillez remplir LHOST et LPORT")
            return
            
        def generate_thread():
            try:
                 self.payload_log.insert(tk.END, f"💣 Génération payload {payload_type}...\n")
                 self.payload_log.see(tk.END)
                 
                 if payload_type == "windows_reverse":
                     result = self.payload.generate_reverse_shell("windows", lhost, int(lport))
                 elif payload_type == "linux_reverse":
                     result = self.payload.generate_reverse_shell("linux", lhost, int(lport))
                 elif payload_type == "android_reverse":
                     result = self.payload.generate_reverse_shell("android", lhost, int(lport))
                 elif payload_type == "windows_bind":
                     result = self.payload.generate_bind_shell("windows", int(lport))
                 elif payload_type == "linux_bind":
                     result = self.payload.generate_bind_shell("linux", int(lport))
                 elif payload_type == "php_webshell":
                     result = self.payload.generate_php_webshell()
                 elif payload_type == "powershell":
                     result = self.payload.generate_powershell_payload(lhost, int(lport))
                 elif payload_type == "python":
                     result = self.payload.generate_python_payload(lhost, int(lport))
                 else:
                     self.payload_log.insert(tk.END, "❌ Type de payload non supporté\n")
                     return
                     
                 if result:
                     self.payload_log.insert(tk.END, f"✅ Payload généré: {result}\n")
                 else:
                     self.payload_log.insert(tk.END, "❌ Erreur génération payload\n")
                     
                 self.payload_log.see(tk.END)
                 
            except Exception as e:
                 self.payload_log.insert(tk.END, f"❌ Erreur: {e}\n")
                 self.payload_log.see(tk.END)
                 
            threading.Thread(target=generate_thread, daemon=True).start()
         
    # Méthodes Backdoor
    def create_backdoor(self, backdoor_type):
        """Crée un backdoor"""
        lhost = self.backdoor_lhost_entry.get()
        lport = self.backdoor_lport_entry.get()
        
        if not lhost or not lport:
            messagebox.showerror("❌ Erreur", "Veuillez remplir LHOST et LPORT")
            return
             
        def create_thread():
             try:
                 self.backdoor_log.insert(tk.END, f"🚪 Création backdoor {backdoor_type}...\n")
                 self.backdoor_log.see(tk.END)
                 
                 if backdoor_type == "windows_registry":
                     payload_file = "payload.exe"  # À améliorer
                     result = self.backdoor.create_windows_registry_backdoor(lhost, int(lport), payload_file)
                 elif backdoor_type == "windows_service":
                     service_name = "SystemUpdate"
                     result = self.backdoor.create_windows_service_backdoor(service_name, "payload.exe")
                 elif backdoor_type == "linux_cron":
                     result = self.backdoor.create_linux_cron_backdoor(lhost, int(lport))
                 elif backdoor_type == "linux_service":
                     service_name = "systemd"
                     result = self.backdoor.create_linux_service_backdoor(service_name, lhost, int(lport))
                 elif backdoor_type == "windows_persistent":
                     result = self.backdoor.create_persistent_backdoor("windows", lhost, int(lport))
                 elif backdoor_type == "linux_persistent":
                     result = self.backdoor.create_persistent_backdoor("linux", lhost, int(lport))
                 elif backdoor_type == "linux_rootkit":
                     result = self.backdoor.create_rootkit_backdoor("linux")
                 else:
                     self.backdoor_log.insert(tk.END, "❌ Type de backdoor non supporté\n")
                     return
                     
                 if result:
                     self.backdoor_log.insert(tk.END, f"✅ Backdoor créé: {result}\n")
                 else:
                     self.backdoor_log.insert(tk.END, "❌ Erreur création backdoor\n")
                     
                 self.backdoor_log.see(tk.END)
                 
             except Exception as e:
                 self.backdoor_log.insert(tk.END, f"❌ Erreur: {e}\n")
                 self.backdoor_log.see(tk.END)
                 
                 threading.Thread(target=create_thread, daemon=True).start()
         
    def setup_clone_tab(self):
        """Onglet clonage de sites"""
        clone_frame = ttk.Frame(self.notebook)
        self.notebook.add(clone_frame, text="🌐 Cloner Site")
        
        # Frame principale
        main_clone_frame = tk.Frame(clone_frame, bg=self.colors['bg'])
        main_clone_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Titre
        tk.Label(main_clone_frame, text="🌐 Clonage de Sites Web",
                font=('Arial', 16, 'bold'),
                bg=self.colors['bg'], fg=self.colors['accent']).pack(pady=(0, 20))
        
        # URL à cloner
        url_frame = ttk.LabelFrame(main_clone_frame, text="🎯 URL Cible")
        url_frame.pack(fill='x', pady=(0, 20))
        
        self.clone_url_entry = tk.Entry(url_frame, bg=self.colors['secondary'], fg=self.colors['fg'],
                                       font=('Arial', 12))
        self.clone_url_entry.pack(fill='x', padx=10, pady=10)
        self.clone_url_entry.insert(0, "https://example.com")
        
        # Boutons clonage
        clone_buttons_frame = tk.Frame(main_clone_frame, bg=self.colors['bg'])
        clone_buttons_frame.pack(fill='x', pady=(0, 20))
        
        tk.Button(clone_buttons_frame, text="🌐 Cloner Site",
                 command=self.clone_site,
                 bg=self.colors['accent'], fg='black',
                 font=('Arial', 12, 'bold')).pack(side='left', padx=5)
        
        tk.Button(clone_buttons_frame, text="🎨 Template Personnalisé",
                 command=self.create_custom_template,
                 bg=self.colors['secondary'], fg=self.colors['fg'],
                 font=('Arial', 12)).pack(side='left', padx=5)
        
        # Log de clonage
        log_frame = ttk.LabelFrame(main_clone_frame, text="📋 Log de Clonage")
        log_frame.pack(fill='both', expand=True)
        
        self.clone_log = scrolledtext.ScrolledText(log_frame, 
                                                  bg=self.colors['secondary'],
                                                  fg=self.colors['fg'],
                                                  height=10)
        self.clone_log.pack(fill='both', expand=True, padx=10, pady=10)
        
    def setup_attacks_tab(self):
        """Onglet attaques avancées"""
        attacks_frame = ttk.Frame(self.notebook)
        self.notebook.add(attacks_frame, text="⚡ Attaques")
        
        # Frame principale
        main_attacks_frame = tk.Frame(attacks_frame, bg=self.colors['bg'])
        main_attacks_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Titre
        tk.Label(main_attacks_frame, text="⚡ Attaques Avancées",
                font=('Arial', 16, 'bold'),
                bg=self.colors['bg'], fg=self.colors['accent']).pack(pady=(0, 20))
        
        # Configuration d'attaque
        attack_config_frame = ttk.LabelFrame(main_attacks_frame, text="🎯 Configuration")
        attack_config_frame.pack(fill='x', pady=(0, 20))
        
        # Type d'attaque
        tk.Label(attack_config_frame, text="Type d'attaque:", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10)
        
        self.attack_type_var = tk.StringVar(value="scan")
        attack_types = [
            ("🔍 Scan Réseau", "scan"),
            ("🔐 SSH Brute Force", "ssh"),
            ("🌐 Web Enumeration", "web"),
            ("💉 SQL Injection", "sql"),
            ("🎯 XSS Test", "xss")
        ]
        
        for text, value in attack_types:
            tk.Radiobutton(attack_config_frame, text=text, variable=self.attack_type_var,
                          value=value, bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=20)
        
        # Cible
        tk.Label(attack_config_frame, text="Cible:", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10, pady=(10, 0))
        
        self.target_entry = tk.Entry(attack_config_frame, bg=self.colors['secondary'], fg=self.colors['fg'])
        self.target_entry.pack(fill='x', padx=10, pady=5)
        self.target_entry.insert(0, "192.168.1.1")
        
        # Boutons d'attaque
        attack_buttons_frame = tk.Frame(main_attacks_frame, bg=self.colors['bg'])
        attack_buttons_frame.pack(fill='x', pady=(0, 20))
        
        tk.Button(attack_buttons_frame, text="⚡ Lancer Attaque",
                 command=self.launch_attack,
                 bg=self.colors['danger'], fg='white',
                 font=('Arial', 12, 'bold')).pack(side='left', padx=5)
        
        tk.Button(attack_buttons_frame, text="📊 Voir Résultats",
                 command=self.show_attack_results,
                 bg=self.colors['secondary'], fg=self.colors['fg'],
                 font=('Arial', 12)).pack(side='left', padx=5)
        
        # Log d'attaques
        attack_log_frame = ttk.LabelFrame(main_attacks_frame, text="📋 Log d'Attaques")
        attack_log_frame.pack(fill='both', expand=True)
        
        self.attack_log = scrolledtext.ScrolledText(attack_log_frame, 
                                                   bg=self.colors['secondary'],
                                                   fg=self.colors['fg'],
                                                   height=10)
        self.attack_log.pack(fill='both', expand=True, padx=10, pady=10)
        
    def setup_tunnels_tab(self):
        """Onglet tunnels"""
        tunnels_frame = ttk.Frame(self.notebook)
        self.notebook.add(tunnels_frame, text="🚇 Tunnels")
        
        # Frame principale
        main_tunnels_frame = tk.Frame(tunnels_frame, bg=self.colors['bg'])
        main_tunnels_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Titre
        tk.Label(main_tunnels_frame, text="🚇 Gestionnaire de Tunnels",
                font=('Arial', 16, 'bold'),
                bg=self.colors['bg'], fg=self.colors['accent']).pack(pady=(0, 20))
        
        # Boutons tunnels
        tunnels_buttons_frame = tk.Frame(main_tunnels_frame, bg=self.colors['bg'])
        tunnels_buttons_frame.pack(fill='x', pady=(0, 20))
        
        tunnel_buttons = [
            ("🚇 Ngrok", self.start_ngrok),
            ("☁️ Cloudflare", self.start_cloudflare),
            ("🌐 LocalTunnel", self.start_localtunnel),
            ("🔄 Proxy", self.start_proxy)
        ]
        
        for i, (text, command) in enumerate(tunnel_buttons):
            btn = tk.Button(tunnels_buttons_frame, text=text, command=command,
                           bg=self.colors['accent'], fg='black',
                           font=('Arial', 12, 'bold'))
            btn.grid(row=i//2, column=i%2, padx=10, pady=10, sticky='ew')
        
        tunnels_buttons_frame.grid_columnconfigure(0, weight=1)
        tunnels_buttons_frame.grid_columnconfigure(1, weight=1)
        
        # Status des tunnels
        tunnel_status_frame = ttk.LabelFrame(main_tunnels_frame, text="📊 Status des Tunnels")
        tunnel_status_frame.pack(fill='x', pady=(0, 20))
        
        self.tunnel_status_text = scrolledtext.ScrolledText(tunnel_status_frame, 
                                                           bg=self.colors['secondary'],
                                                           fg=self.colors['fg'],
                                                           height=8)
        self.tunnel_status_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Boutons de contrôle
        control_buttons_frame = tk.Frame(main_tunnels_frame, bg=self.colors['bg'])
        control_buttons_frame.pack(fill='x')
        
        tk.Button(control_buttons_frame, text="🔄 Actualiser Status",
                 command=self.refresh_tunnel_status,
                 bg=self.colors['secondary'], fg=self.colors['fg']).pack(side='left', padx=5)
        
        tk.Button(control_buttons_frame, text="⏹️ Arrêter Tous",
                 command=self.stop_all_tunnels,
                 bg=self.colors['danger'], fg='white').pack(side='left', padx=5)
        
    def setup_stats_tab(self):
        """Onglet statistiques"""
        stats_frame = ttk.Frame(self.notebook)
        self.notebook.add(stats_frame, text="📊 Stats")
        
        # Frame principale
        main_stats_frame = tk.Frame(stats_frame, bg=self.colors['bg'])
        main_stats_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Titre
        tk.Label(main_stats_frame, text="📊 Statistiques en Temps Réel",
                font=('Arial', 16, 'bold'),
                bg=self.colors['bg'], fg=self.colors['accent']).pack(pady=(0, 20))
        
        # Stats principales
        stats_main_frame = tk.Frame(main_stats_frame, bg=self.colors['bg'])
        stats_main_frame.pack(fill='x', pady=(0, 20))
        
        # Labels de stats
        self.stats_labels = {}
        stats_data = [
            ("🎯 Victimes Totales", "total_victims"),
            ("✅ Attaques Réussies", "successful_attacks"),
            ("📝 Credentials Capturés", "captured_credentials"),
            ("🌍 Pays Différents", "countries")
        ]
        
        for i, (label, key) in enumerate(stats_data):
            frame = tk.Frame(stats_main_frame, bg=self.colors['secondary'])
            frame.grid(row=i//2, column=i%2, padx=10, pady=10, sticky='ew')
            
            tk.Label(frame, text=label, bg=self.colors['secondary'], fg=self.colors['fg'],
                    font=('Arial', 12, 'bold')).pack(pady=5)
            
            self.stats_labels[key] = tk.Label(frame, text="0", 
                                             bg=self.colors['secondary'], fg=self.colors['accent'],
                                             font=('Arial', 16, 'bold'))
            self.stats_labels[key].pack(pady=5)
        
        stats_main_frame.grid_columnconfigure(0, weight=1)
        stats_main_frame.grid_columnconfigure(1, weight=1)
        
        # Credentials récents
        creds_frame = ttk.LabelFrame(main_stats_frame, text="📋 Credentials Récents")
        creds_frame.pack(fill='both', expand=True)
        
        self.creds_text = scrolledtext.ScrolledText(creds_frame, 
                                                   bg=self.colors['secondary'],
                                                   fg=self.colors['fg'],
                                                   height=10)
        self.creds_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Boutons export
        export_buttons_frame = tk.Frame(main_stats_frame, bg=self.colors['bg'])
        export_buttons_frame.pack(fill='x', pady=10)
        
        tk.Button(export_buttons_frame, text="📤 Exporter Credentials",
                 command=self.export_credentials,
                 bg=self.colors['accent'], fg='black').pack(side='left', padx=5)
        
        tk.Button(export_buttons_frame, text="📊 Exporter Stats",
                 command=self.export_stats,
                 bg=self.colors['secondary'], fg=self.colors['fg']).pack(side='left', padx=5)
        
    def setup_settings_tab(self):
        """Onglet paramètres"""
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="⚙️ Settings")
        
        # Frame principale
        main_settings_frame = tk.Frame(settings_frame, bg=self.colors['bg'])
        main_settings_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Titre
        tk.Label(main_settings_frame, text="⚙️ Configuration",
                font=('Arial', 16, 'bold'),
                bg=self.colors['bg'], fg=self.colors['accent']).pack(pady=(0, 20))
        
        # Paramètres généraux
        general_frame = ttk.LabelFrame(main_settings_frame, text="🔧 Paramètres Généraux")
        general_frame.pack(fill='x', pady=(0, 20))
        
        # Auto-démarrage
        self.auto_start_var = tk.BooleanVar()
        tk.Checkbutton(general_frame, text="🚀 Auto-démarrage du serveur",
                      variable=self.auto_start_var,
                      bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10, pady=5)
        
        # Auto-ouverture navigateur
        self.auto_browser_var = tk.BooleanVar()
        tk.Checkbutton(general_frame, text="🌐 Auto-ouverture navigateur",
                      variable=self.auto_browser_var,
                      bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10, pady=5)
        
        # Sauvegarder automatiquement
        self.auto_save_var = tk.BooleanVar(value=True)
        tk.Checkbutton(general_frame, text="💾 Sauvegarde automatique",
                      variable=self.auto_save_var,
                      bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor='w', padx=10, pady=5)
        
        # Boutons d'action
        action_buttons_frame = tk.Frame(main_settings_frame, bg=self.colors['bg'])
        action_buttons_frame.pack(fill='x', pady=20)
        
        tk.Button(action_buttons_frame, text="💾 Sauvegarder Config",
                 command=self.save_config,
                 bg=self.colors['accent'], fg='black').pack(side='left', padx=5)
        
        tk.Button(action_buttons_frame, text="🔄 Réinitialiser",
                 command=self.reset_config,
                 bg=self.colors['warning'], fg='black').pack(side='left', padx=5)
        
        tk.Button(action_buttons_frame, text="📁 Ouvrir Dossier Logs",
                 command=self.open_logs_folder,
                 bg=self.colors['secondary'], fg=self.colors['fg']).pack(side='left', padx=5)
        
    def setup_exploit_tab(self):
        """Onglet exploits avancés"""
        exploit_frame = ttk.Frame(self.notebook)
        self.notebook.add(exploit_frame, text="💥 Exploits")
        
        # Frame principale
        main_frame = ttk.Frame(exploit_frame)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Section exploits personnalisés
        exploit_section = ttk.LabelFrame(main_frame, text="Exploits Personnalisés")
        exploit_section.pack(fill=X, pady=5)
        
        ttk.Label(exploit_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.exploit_os_var = tk.StringVar(value="linux")
        exploit_os_combo = ttk.Combobox(exploit_section, textvariable=self.exploit_os_var, 
                                       values=["linux", "windows", "android"])
        exploit_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(exploit_section, text="Type:").grid(row=1, column=0, padx=5, pady=5)
        self.exploit_type_var = tk.StringVar(value="buffer_overflow")
        exploit_type_combo = ttk.Combobox(exploit_section, textvariable=self.exploit_type_var,
                                         values=["buffer_overflow", "sql_injection", "xss", "rce"])
        exploit_type_combo.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(exploit_section, text="Payload:").grid(row=2, column=0, padx=5, pady=5)
        self.exploit_payload_var = tk.StringVar(value="reverse_shell")
        exploit_payload_entry = ttk.Entry(exploit_section, textvariable=self.exploit_payload_var, width=30)
        exploit_payload_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(exploit_section, text="Créer Exploit", 
                  command=self.create_custom_exploit).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Section escalade de privilèges
        escalation_section = ttk.LabelFrame(main_frame, text="Escalade de Privilèges")
        escalation_section.pack(fill=X, pady=5)
        
        ttk.Label(escalation_section, text="OS:").grid(row=0, column=0, padx=5, pady=5)
        self.escalation_os_var = tk.StringVar(value="linux")
        escalation_os_combo = ttk.Combobox(escalation_section, textvariable=self.escalation_os_var,
                                          values=["linux", "windows"])
        escalation_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(escalation_section, text="Méthode:").grid(row=1, column=0, padx=5, pady=5)
        self.escalation_method_var = tk.StringVar(value="suid_binaries")
        escalation_method_combo = ttk.Combobox(escalation_section, textvariable=self.escalation_method_var,
                                             values=["suid_binaries", "sudo_abuse", "capabilities", "cron_jobs"])
        escalation_method_combo.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(escalation_section, text="Créer Script Escalade", 
                  command=self.create_privilege_escalation).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Section virus polymorphe
        virus_section = ttk.LabelFrame(main_frame, text="Virus Polymorphe")
        virus_section.pack(fill=X, pady=5)
        
        ttk.Label(virus_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.virus_os_var = tk.StringVar(value="linux")
        virus_os_combo = ttk.Combobox(virus_section, textvariable=self.virus_os_var,
                                     values=["linux", "windows"])
        virus_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(virus_section, text="Créer Virus Polymorphe", 
                  command=self.create_polymorphic_virus).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Log des exploits
        log_frame = ttk.LabelFrame(main_frame, text="Log des Exploits")
        log_frame.pack(fill=BOTH, expand=True, pady=5)
        
        self.exploit_log = scrolledtext.ScrolledText(log_frame, height=10)
        self.exploit_log.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def setup_social_tab(self):
        """Onglet ingénierie sociale"""
        social_frame = ttk.Frame(self.notebook)
        self.notebook.add(social_frame, text="🧠 Social Engineering")
        
        # Frame principale
        main_frame = ttk.Frame(social_frame)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Section campagnes phishing
        campaign_section = ttk.LabelFrame(main_frame, text="Campagnes Phishing")
        campaign_section.pack(fill=X, pady=5)
        
        ttk.Label(campaign_section, text="Type:").grid(row=0, column=0, padx=5, pady=5)
        self.campaign_type_var = tk.StringVar(value="bank")
        campaign_type_combo = ttk.Combobox(campaign_section, textvariable=self.campaign_type_var,
                                          values=["bank", "tech_support", "social_media"])
        campaign_type_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(campaign_section, text="Prétexte:").grid(row=1, column=0, padx=5, pady=5)
        self.campaign_pretext_var = tk.StringVar(value="Suspension de compte bancaire")
        campaign_pretext_entry = ttk.Entry(campaign_section, textvariable=self.campaign_pretext_var, width=40)
        campaign_pretext_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(campaign_section, text="Créer Campagne", 
                  command=self.create_phishing_campaign).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Section prétextes
        pretext_section = ttk.LabelFrame(main_frame, text="Scénarios de Prétexte")
        pretext_section.pack(fill=X, pady=5)
        
        ttk.Label(pretext_section, text="Type:").grid(row=0, column=0, padx=5, pady=5)
        self.pretext_type_var = tk.StringVar(value="bank_official")
        pretext_type_combo = ttk.Combobox(pretext_section, textvariable=self.pretext_type_var,
                                         values=["bank_official", "tech_support", "government_official", "colleague"])
        pretext_type_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(pretext_section, text="Créer Scénario", 
                  command=self.create_pretext_scenario).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section vishing
        vishing_section = ttk.LabelFrame(main_frame, text="Scripts Vishing")
        vishing_section.pack(fill=X, pady=5)
        
        ttk.Label(vishing_section, text="Type:").grid(row=0, column=0, padx=5, pady=5)
        self.vishing_type_var = tk.StringVar(value="bank_security")
        vishing_type_combo = ttk.Combobox(vishing_section, textvariable=self.vishing_type_var,
                                         values=["bank_security", "tech_support"])
        vishing_type_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(vishing_section, text="Créer Script Vishing", 
                  command=self.create_vishing_script).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Log social engineering
        log_frame = ttk.LabelFrame(main_frame, text="Log Social Engineering")
        log_frame.pack(fill=BOTH, expand=True, pady=5)
        
        self.social_log = scrolledtext.ScrolledText(log_frame, height=10)
        self.social_log.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def setup_stealth_tab(self):
        """Onglet opérations furtives"""
        stealth_frame = ttk.Frame(self.notebook)
        self.notebook.add(stealth_frame, text="👻 Stealth")
        
        # Frame principale
        main_frame = ttk.Frame(stealth_frame)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Section payloads furtifs
        payload_section = ttk.LabelFrame(main_frame, text="Payloads Furtifs")
        payload_section.pack(fill=X, pady=5)
        
        ttk.Label(payload_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.stealth_os_var = tk.StringVar(value="linux")
        stealth_os_combo = ttk.Combobox(payload_section, textvariable=self.stealth_os_var,
                                       values=["linux", "windows"])
        stealth_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(payload_section, text="Niveau Évasion:").grid(row=1, column=0, padx=5, pady=5)
        self.stealth_level_var = tk.StringVar(value="medium")
        stealth_level_combo = ttk.Combobox(payload_section, textvariable=self.stealth_level_var,
                                          values=["low", "medium", "high"])
        stealth_level_combo.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(payload_section, text="Créer Payload Furtif", 
                  command=self.create_stealth_payload).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Section rootkits
        rootkit_section = ttk.LabelFrame(main_frame, text="Rootkits")
        rootkit_section.pack(fill=X, pady=5)
        
        ttk.Label(rootkit_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.rootkit_os_var = tk.StringVar(value="linux")
        rootkit_os_combo = ttk.Combobox(rootkit_section, textvariable=self.rootkit_os_var,
                                       values=["linux", "windows"])
        rootkit_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(rootkit_section, text="Créer Rootkit", 
                  command=self.create_rootkit).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section anti-forensics
        anti_forensics_section = ttk.LabelFrame(main_frame, text="Anti-Forensics")
        anti_forensics_section.pack(fill=X, pady=5)
        
        ttk.Button(anti_forensics_section, text="Créer Outil Anti-Forensics", 
                  command=self.create_anti_forensics_tool).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Log stealth
        log_frame = ttk.LabelFrame(main_frame, text="Log Stealth")
        log_frame.pack(fill=BOTH, expand=True, pady=5)
        
        self.stealth_log = scrolledtext.ScrolledText(log_frame, height=10)
        self.stealth_log.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def setup_malware_tab(self):
        """Onglet malware avancé"""
        malware_frame = ttk.Frame(self.notebook)
        self.notebook.add(malware_frame, text="🦠 Malware")
        
        # Frame principale
        main_frame = ttk.Frame(malware_frame)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Section keylogger
        keylogger_section = ttk.LabelFrame(main_frame, text="Keylogger")
        keylogger_section.pack(fill=X, pady=5)
        
        ttk.Label(keylogger_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.keylogger_os_var = tk.StringVar(value="linux")
        keylogger_os_combo = ttk.Combobox(keylogger_section, textvariable=self.keylogger_os_var,
                                         values=["linux", "windows"])
        keylogger_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(keylogger_section, text="Créer Keylogger", 
                  command=self.create_keylogger).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section ransomware
        ransomware_section = ttk.LabelFrame(main_frame, text="Ransomware")
        ransomware_section.pack(fill=X, pady=5)
        
        ttk.Label(ransomware_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.ransomware_os_var = tk.StringVar(value="linux")
        ransomware_os_combo = ttk.Combobox(ransomware_section, textvariable=self.ransomware_os_var,
                                          values=["linux", "windows"])
        ransomware_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(ransomware_section, text="Créer Ransomware", 
                  command=self.create_ransomware).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section cryptominer
        miner_section = ttk.LabelFrame(main_frame, text="Cryptominer")
        miner_section.pack(fill=X, pady=5)
        
        ttk.Label(miner_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.miner_os_var = tk.StringVar(value="linux")
        miner_os_combo = ttk.Combobox(miner_section, textvariable=self.miner_os_var,
                                     values=["linux", "windows"])
        miner_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(miner_section, text="Créer Cryptominer", 
                  command=self.create_cryptominer).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Log malware
        log_frame = ttk.LabelFrame(main_frame, text="Log Malware")
        log_frame.pack(fill=BOTH, expand=True, pady=5)
        
        self.malware_log = scrolledtext.ScrolledText(log_frame, height=10)
        self.malware_log.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def setup_zero_day_tab(self):
        """Onglet exploits zero-day"""
        zero_day_frame = ttk.Frame(self.notebook)
        self.notebook.add(zero_day_frame, text="🔥 Zero-Day")
        
        # Frame principale
        main_frame = ttk.Frame(zero_day_frame)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Section buffer overflow
        bof_section = ttk.LabelFrame(main_frame, text="Buffer Overflow")
        bof_section.pack(fill=X, pady=5)
        
        ttk.Label(bof_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.bof_os_var = tk.StringVar(value="linux")
        bof_os_combo = ttk.Combobox(bof_section, textvariable=self.bof_os_var,
                                    values=["linux", "windows"])
        bof_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(bof_section, text="Service:").grid(row=1, column=0, padx=5, pady=5)
        self.bof_service_var = tk.StringVar(value="http")
        bof_service_combo = ttk.Combobox(bof_section, textvariable=self.bof_service_var,
                                        values=["http", "ftp", "smtp", "ssh"])
        bof_service_combo.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(bof_section, text="Créer Exploit Buffer Overflow", 
                  command=self.create_buffer_overflow_exploit).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Section heap spraying
        heap_section = ttk.LabelFrame(main_frame, text="Heap Spraying")
        heap_section.pack(fill=X, pady=5)
        
        ttk.Label(heap_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.heap_os_var = tk.StringVar(value="linux")
        heap_os_combo = ttk.Combobox(heap_section, textvariable=self.heap_os_var,
                                    values=["linux", "windows"])
        heap_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(heap_section, text="Créer Exploit Heap Spraying", 
                  command=self.create_heap_spray_exploit).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section ROP chain
        rop_section = ttk.LabelFrame(main_frame, text="ROP Chain")
        rop_section.pack(fill=X, pady=5)
        
        ttk.Label(rop_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.rop_os_var = tk.StringVar(value="linux")
        rop_os_combo = ttk.Combobox(rop_section, textvariable=self.rop_os_var,
                                   values=["linux", "windows"])
        rop_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(rop_section, text="Architecture:").grid(row=1, column=0, padx=5, pady=5)
        self.rop_arch_var = tk.StringVar(value="x86")
        rop_arch_combo = ttk.Combobox(rop_section, textvariable=self.rop_arch_var,
                                     values=["x86", "x64"])
        rop_arch_combo.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(rop_section, text="Créer Exploit ROP Chain", 
                  command=self.create_rop_chain_exploit).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Section format string
        format_section = ttk.LabelFrame(main_frame, text="Format String")
        format_section.pack(fill=X, pady=5)
        
        ttk.Label(format_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.format_os_var = tk.StringVar(value="linux")
        format_os_combo = ttk.Combobox(format_section, textvariable=self.format_os_var,
                                      values=["linux", "windows"])
        format_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(format_section, text="Créer Exploit Format String", 
                  command=self.create_format_string_exploit).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Log zero-day
        log_frame = ttk.LabelFrame(main_frame, text="Log Zero-Day")
        log_frame.pack(fill=BOTH, expand=True, pady=5)
        
        self.zero_day_log = scrolledtext.ScrolledText(log_frame, height=10)
        self.zero_day_log.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def setup_persistence_tab(self):
        """Onglet persistance avancée"""
        persistence_frame = ttk.Frame(self.notebook)
        self.notebook.add(persistence_frame, text="🕷️ Persistance")
        
        # Frame principale
        main_frame = ttk.Frame(persistence_frame)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Section bootkits
        bootkit_section = ttk.LabelFrame(main_frame, text="Bootkits")
        bootkit_section.pack(fill=X, pady=5)
        
        ttk.Label(bootkit_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.bootkit_os_var = tk.StringVar(value="linux")
        bootkit_os_combo = ttk.Combobox(bootkit_section, textvariable=self.bootkit_os_var,
                                        values=["linux", "windows"])
        bootkit_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(bootkit_section, text="Créer Bootkit", 
                  command=self.create_bootkit).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section firmware persistence
        firmware_section = ttk.LabelFrame(main_frame, text="Persistance Firmware")
        firmware_section.pack(fill=X, pady=5)
        
        ttk.Label(firmware_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.firmware_os_var = tk.StringVar(value="linux")
        firmware_os_combo = ttk.Combobox(firmware_section, textvariable=self.firmware_os_var,
                                        values=["linux", "windows"])
        firmware_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(firmware_section, text="Créer Persistance Firmware", 
                  command=self.create_firmware_persistence).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section kernel rootkits
        kernel_section = ttk.LabelFrame(main_frame, text="Kernel Rootkits")
        kernel_section.pack(fill=X, pady=5)
        
        ttk.Label(kernel_section, text="OS Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.kernel_os_var = tk.StringVar(value="linux")
        kernel_os_combo = ttk.Combobox(kernel_section, textvariable=self.kernel_os_var,
                                      values=["linux", "windows"])
        kernel_os_combo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(kernel_section, text="Créer Kernel Rootkit", 
                  command=self.create_kernel_rootkit).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section hypervisor rootkits
        hypervisor_section = ttk.LabelFrame(main_frame, text="Hypervisor Rootkits")
        hypervisor_section.pack(fill=X, pady=5)
        
        ttk.Button(hypervisor_section, text="Créer Hypervisor Rootkit", 
                  command=self.create_hypervisor_rootkit).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Log persistance
        log_frame = ttk.LabelFrame(main_frame, text="Log Persistance")
        log_frame.pack(fill=BOTH, expand=True, pady=5)
        
        self.persistence_log = scrolledtext.ScrolledText(log_frame, height=10)
        self.persistence_log.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def setup_web_exploitation_tab(self):
        """Onglet exploitation web"""
        web_frame = ttk.Frame(self.notebook)
        self.notebook.add(web_frame, text="🌐 Web Exploitation")
        
        # Frame principale
        main_frame = ttk.Frame(web_frame)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Section SQL Injection
        sql_section = ttk.LabelFrame(main_frame, text="SQL Injection")
        sql_section.pack(fill=X, pady=5)
        
        ttk.Label(sql_section, text="URL Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.sql_url_var = tk.StringVar(value="http://target.com/page?id=1")
        sql_url_entry = ttk.Entry(sql_section, textvariable=self.sql_url_var, width=40)
        sql_url_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(sql_section, text="Points d'injection:").grid(row=1, column=0, padx=5, pady=5)
        self.sql_points_var = tk.StringVar(value="id,user,search")
        sql_points_entry = ttk.Entry(sql_section, textvariable=self.sql_points_var, width=40)
        sql_points_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(sql_section, text="Scanner SQL Injection", 
                  command=self.scan_sql_injection).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Section XSS
        xss_section = ttk.LabelFrame(main_frame, text="Cross-Site Scripting (XSS)")
        xss_section.pack(fill=X, pady=5)
        
        ttk.Label(xss_section, text="URL Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.xss_url_var = tk.StringVar(value="http://target.com/search?q=test")
        xss_url_entry = ttk.Entry(xss_section, textvariable=self.xss_url_var, width=40)
        xss_url_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(xss_section, text="Points d'injection:").grid(row=1, column=0, padx=5, pady=5)
        self.xss_points_var = tk.StringVar(value="q,search,param")
        xss_points_entry = ttk.Entry(xss_section, textvariable=self.xss_points_var, width=40)
        xss_points_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(xss_section, text="Scanner XSS", 
                  command=self.scan_xss).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Section CSRF
        csrf_section = ttk.LabelFrame(main_frame, text="Cross-Site Request Forgery (CSRF)")
        csrf_section.pack(fill=X, pady=5)
        
        ttk.Label(csrf_section, text="URL Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.csrf_url_var = tk.StringVar(value="http://target.com/")
        csrf_url_entry = ttk.Entry(csrf_section, textvariable=self.csrf_url_var, width=40)
        csrf_url_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(csrf_section, text="URL Action:").grid(row=1, column=0, padx=5, pady=5)
        self.csrf_action_var = tk.StringVar(value="http://target.com/delete")
        csrf_action_entry = ttk.Entry(csrf_section, textvariable=self.csrf_action_var, width=40)
        csrf_action_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(csrf_section, text="Générer Exploit CSRF", 
                  command=self.generate_csrf_exploit).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Section File Upload
        upload_section = ttk.LabelFrame(main_frame, text="File Upload Exploit")
        upload_section.pack(fill=X, pady=5)
        
        ttk.Label(upload_section, text="URL Upload:").grid(row=0, column=0, padx=5, pady=5)
        self.upload_url_var = tk.StringVar(value="http://target.com/upload")
        upload_url_entry = ttk.Entry(upload_section, textvariable=self.upload_url_var, width=40)
        upload_url_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(upload_section, text="Chemin Upload:").grid(row=1, column=0, padx=5, pady=5)
        self.upload_path_var = tk.StringVar(value="/uploads/")
        upload_path_entry = ttk.Entry(upload_section, textvariable=self.upload_path_var, width=40)
        upload_path_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(upload_section, text="Créer Exploit Upload", 
                  command=self.create_upload_exploit).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Log web exploitation
        log_frame = ttk.LabelFrame(main_frame, text="Log Web Exploitation")
        log_frame.pack(fill=BOTH, expand=True, pady=5)
        
        self.web_exploit_log = scrolledtext.ScrolledText(log_frame, height=10)
        self.web_exploit_log.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def setup_osint_tab(self):
        """Onglet OSINT"""
        osint_frame = ttk.Frame(self.notebook)
        self.notebook.add(osint_frame, text="🔍 OSINT")
        
        # Frame principale
        main_frame = ttk.Frame(osint_frame)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Section sous-domaines
        subdomain_section = ttk.LabelFrame(main_frame, text="Énumération Sous-domaines")
        subdomain_section.pack(fill=X, pady=5)
        
        ttk.Label(subdomain_section, text="Domaine Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.subdomain_target_var = tk.StringVar(value="example.com")
        subdomain_target_entry = ttk.Entry(subdomain_section, textvariable=self.subdomain_target_var, width=40)
        subdomain_target_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(subdomain_section, text="Énumérer Sous-domaines", 
                  command=self.enumerate_subdomains).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section récolte emails
        email_section = ttk.LabelFrame(main_frame, text="Récolte Emails")
        email_section.pack(fill=X, pady=5)
        
        ttk.Label(email_section, text="Domaine Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.email_target_var = tk.StringVar(value="example.com")
        email_target_entry = ttk.Entry(email_section, textvariable=self.email_target_var, width=40)
        email_target_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(email_section, text="Récolter Emails", 
                  command=self.harvest_emails).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section réseaux sociaux
        social_section = ttk.LabelFrame(main_frame, text="OSINT Réseaux Sociaux")
        social_section.pack(fill=X, pady=5)
        
        ttk.Label(social_section, text="Organisation:").grid(row=0, column=0, padx=5, pady=5)
        self.social_target_var = tk.StringVar(value="Example Corp")
        social_target_entry = ttk.Entry(social_section, textvariable=self.social_target_var, width=40)
        social_target_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(social_section, text="OSINT Réseaux Sociaux", 
                  command=self.social_media_osint).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section Certificate Transparency
        ct_section = ttk.LabelFrame(main_frame, text="Certificate Transparency")
        ct_section.pack(fill=X, pady=5)
        
        ttk.Label(ct_section, text="Domaine Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.ct_target_var = tk.StringVar(value="example.com")
        ct_target_entry = ttk.Entry(ct_section, textvariable=self.ct_target_var, width=40)
        ct_target_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(ct_section, text="Surveiller Certificats", 
                  command=self.monitor_certificates).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Log OSINT
        log_frame = ttk.LabelFrame(main_frame, text="Log OSINT")
        log_frame.pack(fill=BOTH, expand=True, pady=5)
        
        self.osint_log = scrolledtext.ScrolledText(log_frame, height=10)
        self.osint_log.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def setup_ad_tab(self):
        """Onglet Active Directory"""
        ad_frame = ttk.Frame(self.notebook)
        self.notebook.add(ad_frame, text="🏢 Active Directory")
        
        # Frame principale
        main_frame = ttk.Frame(ad_frame)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Section Kerberos
        kerberos_section = ttk.LabelFrame(main_frame, text="Attaques Kerberos")
        kerberos_section.pack(fill=X, pady=5)
        
        ttk.Label(kerberos_section, text="Domaine Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.kerberos_domain_var = tk.StringVar(value="example.local")
        kerberos_domain_entry = ttk.Entry(kerberos_section, textvariable=self.kerberos_domain_var, width=40)
        kerberos_domain_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(kerberos_section, text="Liste Utilisateurs:").grid(row=1, column=0, padx=5, pady=5)
        self.kerberos_users_var = tk.StringVar(value="admin,user,test")
        kerberos_users_entry = ttk.Entry(kerberos_section, textvariable=self.kerberos_users_var, width=40)
        kerberos_users_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(kerberos_section, text="Attaque Kerberos", 
                  command=self.kerberos_attack).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Section BloodHound
        bloodhound_section = ttk.LabelFrame(main_frame, text="BloodHound")
        bloodhound_section.pack(fill=X, pady=5)
        
        ttk.Label(bloodhound_section, text="Domaine Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.bloodhound_domain_var = tk.StringVar(value="example.local")
        bloodhound_domain_entry = ttk.Entry(bloodhound_section, textvariable=self.bloodhound_domain_var, width=40)
        bloodhound_domain_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(bloodhound_section, text="Collecte BloodHound", 
                  command=self.bloodhound_collection).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Section mouvement latéral
        lateral_section = ttk.LabelFrame(main_frame, text="Mouvement Latéral")
        lateral_section.pack(fill=X, pady=5)
        
        ttk.Label(lateral_section, text="Domaine Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.lateral_domain_var = tk.StringVar(value="example.local")
        lateral_domain_entry = ttk.Entry(lateral_section, textvariable=self.lateral_domain_var, width=40)
        lateral_domain_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(lateral_section, text="Hôtes Compromis:").grid(row=1, column=0, padx=5, pady=5)
        self.lateral_hosts_var = tk.StringVar(value="host1,host2,host3")
        lateral_hosts_entry = ttk.Entry(lateral_section, textvariable=self.lateral_hosts_var, width=40)
        lateral_hosts_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(lateral_section, text="Mouvement Latéral", 
                  command=self.lateral_movement).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Section escalade privilèges
        escalation_section = ttk.LabelFrame(main_frame, text="Escalade Privilèges AD")
        escalation_section.pack(fill=X, pady=5)
        
        ttk.Label(escalation_section, text="Domaine Cible:").grid(row=0, column=0, padx=5, pady=5)
        self.escalation_domain_var = tk.StringVar(value="example.local")
        escalation_domain_entry = ttk.Entry(escalation_section, textvariable=self.escalation_domain_var, width=40)
        escalation_domain_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(escalation_section, text="Escalade Privilèges", 
                  command=self.ad_privilege_escalation).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Log AD
        log_frame = ttk.LabelFrame(main_frame, text="Log Active Directory")
        log_frame.pack(fill=BOTH, expand=True, pady=5)
        
        self.ad_log = scrolledtext.ScrolledText(log_frame, height=10)
        self.ad_log.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def refresh_templates(self):
        """Actualise la liste des templates"""
        self.template_listbox.delete(0, tk.END)
        templates = self.get_available_templates()
        
        for template in templates:
            self.template_listbox.insert(tk.END, os.path.basename(template))
            
    def get_available_templates(self):
        """Retourne la liste des templates disponibles"""
        templates = []
        if os.path.exists("templates"):
            for file in os.listdir("templates"):
                if file.endswith('.html'):
                    templates.append(os.path.join("templates", file))
        return templates
        
    def start_server(self):
        """Démarre le serveur"""
        try:
            host = self.host_entry.get()
            port = int(self.port_entry.get())
            
            # Sélectionner le template
            selection = self.template_listbox.curselection()
            if selection:
                templates = self.get_available_templates()
                template_path = templates[selection[0]]
                self.phishing.set_template(template_path)
                self.selected_template = template_path
            
            # Démarrer le serveur
            self.phishing.start_server(host, port)
            self.server_running = True
            
            # Mettre à jour l'interface
            self.start_server_btn.config(state='disabled')
            self.stop_server_btn.config(state='normal')
            self.server_url_label.config(text=f"URL: http://{host}:{port}")
            
            # Auto-ouverture navigateur
            if self.auto_browser_var.get():
                webbrowser.open(f"http://{host}:{port}")
                
            messagebox.showinfo("✅ Succès", f"Serveur démarré sur http://{host}:{port}")
            
        except Exception as e:
            messagebox.showerror("❌ Erreur", f"Erreur démarrage serveur: {e}")
            
    def stop_server(self):
        """Arrête le serveur"""
        try:
            self.phishing.stop_server()
            self.server_running = False
            
            # Mettre à jour l'interface
            self.start_server_btn.config(state='normal')
            self.stop_server_btn.config(state='disabled')
            self.server_url_label.config(text="URL: Serveur arrêté")
            
            messagebox.showinfo("✅ Succès", "Serveur arrêté")
            
        except Exception as e:
            messagebox.showerror("❌ Erreur", f"Erreur arrêt serveur: {e}")
            
    def clone_site(self):
        """Clone un site"""
        url = self.clone_url_entry.get()
        if not url:
            messagebox.showerror("❌ Erreur", "Veuillez entrer une URL")
            return
            
        def clone_thread():
            try:
                self.clone_log.insert(tk.END, f"🌐 Clonage de: {url}\n")
                self.clone_log.see(tk.END)
                
                template_path = self.cloner.clone_site(url)
                
                if template_path:
                    self.clone_log.insert(tk.END, f"✅ Site cloné: {template_path}\n")
                    self.phishing.set_template(template_path)
                    messagebox.showinfo("✅ Succès", f"Site cloné: {template_path}")
                else:
                    self.clone_log.insert(tk.END, "❌ Erreur de clonage\n")
                    messagebox.showerror("❌ Erreur", "Erreur lors du clonage")
                    
            except Exception as e:
                self.clone_log.insert(tk.END, f"❌ Erreur: {e}\n")
                messagebox.showerror("❌ Erreur", f"Erreur: {e}")
                
        threading.Thread(target=clone_thread, daemon=True).start()
        
    def create_custom_template(self):
        """Crée un template personnalisé"""
        # Interface pour créer un template personnalisé
        custom_window = tk.Toplevel(self.root)
        custom_window.title("🎨 Template Personnalisé")
        custom_window.geometry("600x400")
        custom_window.configure(bg=self.colors['bg'])
        
        # URL
        tk.Label(custom_window, text="URL du site:", bg=self.colors['bg'], fg=self.colors['fg']).pack(pady=5)
        url_entry = tk.Entry(custom_window, bg=self.colors['secondary'], fg=self.colors['fg'])
        url_entry.pack(fill='x', padx=20, pady=5)
        
        # Champs personnalisés
        tk.Label(custom_window, text="Champs du formulaire:", bg=self.colors['bg'], fg=self.colors['fg']).pack(pady=10)
        
        fields_frame = tk.Frame(custom_window, bg=self.colors['bg'])
        fields_frame.pack(fill='both', expand=True, padx=20)
        
        fields = []
        
        def add_field():
            field_frame = tk.Frame(fields_frame, bg=self.colors['secondary'])
            field_frame.pack(fill='x', pady=5)
            
            name_entry = tk.Entry(field_frame, bg=self.colors['bg'], fg=self.colors['fg'])
            name_entry.pack(side='left', padx=5)
            name_entry.insert(0, "field_name")
            
            label_entry = tk.Entry(field_frame, bg=self.colors['bg'], fg=self.colors['fg'])
            label_entry.pack(side='left', padx=5)
            label_entry.insert(0, "Field Label")
            
            type_var = tk.StringVar(value="text")
            type_combo = ttk.Combobox(field_frame, textvariable=type_var, 
                                     values=["text", "password", "email", "number"])
            type_combo.pack(side='left', padx=5)
            
            fields.append({
                'frame': field_frame,
                'name': name_entry,
                'label': label_entry,
                'type': type_var
            })
            
        def create_template():
            url = url_entry.get()
            if not url:
                messagebox.showerror("❌ Erreur", "Veuillez entrer une URL")
                return
                
            custom_fields = []
            for field in fields:
                custom_fields.append({
                    'name': field['name'].get(),
                    'label': field['label'].get(),
                    'type': field['type'].get()
                })
                
            try:
                template_path = self.cloner.create_custom_template(url, custom_fields)
                messagebox.showinfo("✅ Succès", f"Template créé: {template_path}")
                custom_window.destroy()
            except Exception as e:
                messagebox.showerror("❌ Erreur", f"Erreur: {e}")
                
        # Boutons
        buttons_frame = tk.Frame(custom_window, bg=self.colors['bg'])
        buttons_frame.pack(fill='x', pady=20)
        
        tk.Button(buttons_frame, text="➕ Ajouter Champ", command=add_field,
                 bg=self.colors['accent'], fg='black').pack(side='left', padx=5)
        
        tk.Button(buttons_frame, text="🎨 Créer Template", command=create_template,
                 bg=self.colors['success'], fg='black').pack(side='left', padx=5)
        
        # Ajouter un premier champ
        add_field()
        
    def launch_attack(self):
        """Lance une attaque"""
        attack_type = self.attack_type_var.get()
        target = self.target_entry.get()
        
        if not target:
            messagebox.showerror("❌ Erreur", "Veuillez entrer une cible")
            return
            
        def attack_thread():
            try:
                self.attack_log.insert(tk.END, f"⚡ Lancement attaque {attack_type} sur {target}\n")
                self.attack_log.see(tk.END)
                
                if attack_type == "scan":
                    result = self.attacks.network_scan(target)
                elif attack_type == "ssh":
                    username = "admin"  # À améliorer
                    wordlist = "wordlist.txt"  # À améliorer
                    result = self.attacks.ssh_brute_force(target, username, wordlist)
                elif attack_type == "web":
                    result = self.attacks.web_enumeration(target)
                elif attack_type == "sql":
                    result = self.attacks.sql_injection_test(target)
                elif attack_type == "xss":
                    result = self.attacks.xss_test(target)
                    
                self.attack_log.insert(tk.END, f"✅ Attaque terminée\n")
                self.attack_log.see(tk.END)
                
            except Exception as e:
                self.attack_log.insert(tk.END, f"❌ Erreur: {e}\n")
                self.attack_log.see(tk.END)
                
        threading.Thread(target=attack_thread, daemon=True).start()
        
    def show_attack_results(self):
        """Affiche les résultats d'attaques"""
        results = self.attacks.get_attack_results()
        
        if not results:
            messagebox.showinfo("📊 Résultats", "Aucun résultat d'attaque disponible")
            return
            
        # Créer une fenêtre pour afficher les résultats
        results_window = tk.Toplevel(self.root)
        results_window.title("📊 Résultats d'Attaques")
        results_window.geometry("800x600")
        results_window.configure(bg=self.colors['bg'])
        
        text_widget = scrolledtext.ScrolledText(results_window, 
                                               bg=self.colors['secondary'],
                                               fg=self.colors['fg'])
        text_widget.pack(fill='both', expand=True, padx=10, pady=10)
        
        text_widget.insert(tk.END, json.dumps(results, indent=2))
        
    def start_ngrok(self):
        """Démarre Ngrok"""
        def ngrok_thread():
            try:
                self.tunnel_status_text.insert(tk.END, "🚇 Démarrage Ngrok...\n")
                self.tunnel_status_text.see(tk.END)
                
                url = self.tunnels.start_ngrok(8080)
                
                if url:
                    self.tunnel_status_text.insert(tk.END, f"✅ Ngrok: {url}\n")
                    self.current_tunnel = url
                else:
                    self.tunnel_status_text.insert(tk.END, "❌ Erreur Ngrok\n")
                    
                self.tunnel_status_text.see(tk.END)
                
            except Exception as e:
                self.tunnel_status_text.insert(tk.END, f"❌ Erreur: {e}\n")
                self.tunnel_status_text.see(tk.END)
                
        threading.Thread(target=ngrok_thread, daemon=True).start()
        
    def start_cloudflare(self):
        """Démarre Cloudflare"""
        def cloudflare_thread():
            try:
                self.tunnel_status_text.insert(tk.END, "☁️ Démarrage Cloudflare...\n")
                self.tunnel_status_text.see(tk.END)
                
                url = self.tunnels.start_cloudflare_tunnel(8080)
                
                if url:
                    self.tunnel_status_text.insert(tk.END, f"✅ Cloudflare: {url}\n")
                    self.current_tunnel = url
                else:
                    self.tunnel_status_text.insert(tk.END, "❌ Erreur Cloudflare\n")
                    
                self.tunnel_status_text.see(tk.END)
                
            except Exception as e:
                self.tunnel_status_text.insert(tk.END, f"❌ Erreur: {e}\n")
                self.tunnel_status_text.see(tk.END)
                
        threading.Thread(target=cloudflare_thread, daemon=True).start()
        
    def start_localtunnel(self):
        """Démarre LocalTunnel"""
        def localtunnel_thread():
            try:
                self.tunnel_status_text.insert(tk.END, "🌐 Démarrage LocalTunnel...\n")
                self.tunnel_status_text.see(tk.END)
                
                url = self.tunnels.start_localtunnel(8080)
                
                if url:
                    self.tunnel_status_text.insert(tk.END, f"✅ LocalTunnel: {url}\n")
                    self.current_tunnel = url
                else:
                    self.tunnel_status_text.insert(tk.END, "❌ Erreur LocalTunnel\n")
                    
                self.tunnel_status_text.see(tk.END)
                
            except Exception as e:
                self.tunnel_status_text.insert(tk.END, f"❌ Erreur: {e}\n")
                self.tunnel_status_text.see(tk.END)
                
        threading.Thread(target=localtunnel_thread, daemon=True).start()
        
    def start_proxy(self):
        """Démarre le proxy"""
        def proxy_thread():
            try:
                self.tunnel_status_text.insert(tk.END, "🔄 Démarrage Proxy...\n")
                self.tunnel_status_text.see(tk.END)
                
                url = self.tunnels.start_proxy_server(8080, 9090)
                
                if url:
                    self.tunnel_status_text.insert(tk.END, f"✅ Proxy: {url}\n")
                    self.current_tunnel = url
                else:
                    self.tunnel_status_text.insert(tk.END, "❌ Erreur Proxy\n")
                    
                self.tunnel_status_text.see(tk.END)
                
            except Exception as e:
                self.tunnel_status_text.insert(tk.END, f"❌ Erreur: {e}\n")
                self.tunnel_status_text.see(tk.END)
                
        threading.Thread(target=proxy_thread, daemon=True).start()
        
    def refresh_tunnel_status(self):
        """Actualise le status des tunnels"""
        tunnels = self.tunnels.get_active_tunnels()
        
        self.tunnel_status_text.delete(1.0, tk.END)
        
        if tunnels:
            for name, tunnel in tunnels.items():
                self.tunnel_status_text.insert(tk.END, f"✅ {name}: {tunnel.get('public_url', 'N/A')}\n")
        else:
            self.tunnel_status_text.insert(tk.END, "❌ Aucun tunnel actif\n")
            
    def stop_all_tunnels(self):
        """Arrête tous les tunnels"""
        self.tunnels.stop_all_tunnels()
        self.tunnel_status_text.insert(tk.END, "⏹️ Tous les tunnels arrêtés\n")
        self.tunnel_status_text.see(tk.END)
        
    def update_stats(self):
        """Met à jour les statistiques"""
        try:
            stats = self.phishing.get_stats()
            
            # Mettre à jour les labels
            self.stats_labels['total_victims'].config(text=str(stats['total_victims']))
            self.stats_labels['successful_attacks'].config(text=str(stats['successful_attacks']))
            self.stats_labels['captured_credentials'].config(text=str(stats['captured_credentials']))
            
            # Compter les pays
            countries = len(stats.get('geographic_data', {}))
            self.stats_labels['countries'].config(text=str(countries))
            
            # Mettre à jour les credentials
            credentials = self.phishing.get_credentials()
            self.creds_text.delete(1.0, tk.END)
            
            if credentials:
                for cred in credentials[-10:]:  # 10 derniers
                    email = cred.get('email', 'N/A')
                    ip = cred.get('ip_address', 'N/A')
                    timestamp = cred.get('timestamp', 'N/A')
                    self.creds_text.insert(tk.END, f"📧 {email} | 🌐 {ip} | ⏰ {timestamp}\n")
            else:
                self.creds_text.insert(tk.END, "Aucun credential capturé")
                
        except Exception as e:
            print(f"Erreur mise à jour stats: {e}")
            
        # Programmer la prochaine mise à jour
        self.root.after(5000, self.update_stats)  # Toutes les 5 secondes
        
    def export_credentials(self):
        """Exporte les credentials"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                self.phishing.export_credentials(filename)
                messagebox.showinfo("✅ Succès", f"Credentials exportés vers {filename}")
            except Exception as e:
                messagebox.showerror("❌ Erreur", f"Erreur export: {e}")
                
    def export_stats(self):
        """Exporte les statistiques"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                stats = self.phishing.get_stats()
                with open(filename, 'w') as f:
                    json.dump(stats, f, indent=2)
                messagebox.showinfo("✅ Succès", f"Stats exportées vers {filename}")
            except Exception as e:
                messagebox.showerror("❌ Erreur", f"Erreur export: {e}")
                
    def save_config(self):
        """Sauvegarde la configuration"""
        config = {
            'auto_start': self.auto_start_var.get(),
            'auto_browser': self.auto_browser_var.get(),
            'auto_save': self.auto_save_var.get(),
            'host': self.host_entry.get(),
            'port': self.port_entry.get()
        }
        
        try:
            with open('config.json', 'w') as f:
                json.dump(config, f, indent=2)
            messagebox.showinfo("✅ Succès", "Configuration sauvegardée")
        except Exception as e:
            messagebox.showerror("❌ Erreur", f"Erreur sauvegarde: {e}")
            
    def reset_config(self):
        """Réinitialise la configuration"""
        if messagebox.askyesno("🔄 Confirmation", "Réinitialiser la configuration ?"):
            self.auto_start_var.set(False)
            self.auto_browser_var.set(False)
            self.auto_save_var.set(True)
            self.host_entry.delete(0, tk.END)
            self.host_entry.insert(0, "0.0.0.0")
            self.port_entry.delete(0, tk.END)
            self.port_entry.insert(0, "8080")
            
    def open_templates_folder(self):
        """Ouvre le dossier des templates"""
        import subprocess
        import platform
        
        templates_path = os.path.abspath("templates")
        
        if platform.system() == "Windows":
            subprocess.run(["explorer", templates_path])
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", templates_path])
        else:  # Linux
            subprocess.run(["xdg-open", templates_path])
            
    def open_logs_folder(self):
        """Ouvre le dossier des logs"""
        import subprocess
        import platform
        
        logs_path = os.path.abspath("logs")
        
        if not os.path.exists(logs_path):
            os.makedirs(logs_path)
            
        if platform.system() == "Windows":
            subprocess.run(["explorer", logs_path])
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", logs_path])
        else:  # Linux
            subprocess.run(["xdg-open", logs_path])
    
    # ===== MÉTHODES MANQUANTES POUR LES EXPLOITS AVANCÉS =====
    
    def create_custom_exploit(self):
        """Crée un exploit personnalisé"""
        try:
            os_target = self.exploit_os_var.get()
            exploit_type = self.exploit_type_var.get()
            payload = self.exploit_payload_var.get()
            
            self.exploit_log.insert(tk.END, f"💥 Création exploit {exploit_type} pour {os_target}...\n")
            self.exploit_log.see(tk.END)
            
            result = self.exploit.create_custom_exploit(os_target, exploit_type, payload)
            
            if result:
                self.exploit_log.insert(tk.END, f"✅ Exploit créé: {result}\n")
            else:
                self.exploit_log.insert(tk.END, "❌ Erreur création exploit\n")
                
            self.exploit_log.see(tk.END)
            
        except Exception as e:
            self.exploit_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.exploit_log.see(tk.END)
    
    def create_privilege_escalation(self):
        """Crée un script d'escalade de privilèges"""
        try:
            os_target = self.escalation_os_var.get()
            method = self.escalation_method_var.get()
            
            self.exploit_log.insert(tk.END, f"🔓 Création script escalade {method} pour {os_target}...\n")
            self.exploit_log.see(tk.END)
            
            result = self.exploit.create_privilege_escalation_script(os_target, method)
            
            if result:
                self.exploit_log.insert(tk.END, f"✅ Script escalade créé: {result}\n")
            else:
                self.exploit_log.insert(tk.END, "❌ Erreur création script escalade\n")
                
            self.exploit_log.see(tk.END)
            
        except Exception as e:
            self.exploit_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.exploit_log.see(tk.END)
    
    def create_polymorphic_virus(self):
        """Crée un virus polymorphe"""
        try:
            os_target = self.virus_os_var.get()
            
            self.exploit_log.insert(tk.END, f"🦠 Création virus polymorphe pour {os_target}...\n")
            self.exploit_log.see(tk.END)
            
            result = self.exploit.create_polymorphic_virus(os_target)
            
            if result:
                self.exploit_log.insert(tk.END, f"✅ Virus polymorphe créé: {result}\n")
            else:
                self.exploit_log.insert(tk.END, "❌ Erreur création virus polymorphe\n")
                
            self.exploit_log.see(tk.END)
            
        except Exception as e:
            self.exploit_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.exploit_log.see(tk.END)
    
    # ===== MÉTHODES MANQUANTES POUR L'INGÉNIERIE SOCIALE =====
    
    def create_phishing_campaign(self):
        """Crée une campagne de phishing"""
        try:
            campaign_type = self.campaign_type_var.get()
            pretext = self.campaign_pretext_var.get()
            
            self.social_log.insert(tk.END, f"🧠 Création campagne {campaign_type}...\n")
            self.social_log.see(tk.END)
            
            result = self.social.create_phishing_campaign(campaign_type, pretext)
            
            if result:
                self.social_log.insert(tk.END, f"✅ Campagne créée: {result}\n")
            else:
                self.social_log.insert(tk.END, "❌ Erreur création campagne\n")
                
            self.social_log.see(tk.END)
            
        except Exception as e:
            self.social_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.social_log.see(tk.END)
    
    def create_pretext_scenario(self):
        """Crée un scénario de prétexte"""
        try:
            pretext_type = self.pretext_type_var.get()
            
            self.social_log.insert(tk.END, f"🎭 Création scénario {pretext_type}...\n")
            self.social_log.see(tk.END)
            
            result = self.social.create_pretext_scenario(pretext_type)
            
            if result:
                self.social_log.insert(tk.END, f"✅ Scénario créé: {result}\n")
            else:
                self.social_log.insert(tk.END, "❌ Erreur création scénario\n")
                
            self.social_log.see(tk.END)
            
        except Exception as e:
            self.social_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.social_log.see(tk.END)
    
    def create_vishing_script(self):
        """Crée un script vishing"""
        try:
            vishing_type = self.vishing_type_var.get()
            
            self.social_log.insert(tk.END, f"📞 Création script vishing {vishing_type}...\n")
            self.social_log.see(tk.END)
            
            result = self.social.create_vishing_script(vishing_type)
            
            if result:
                self.social_log.insert(tk.END, f"✅ Script vishing créé: {result}\n")
            else:
                self.social_log.insert(tk.END, "❌ Erreur création script vishing\n")
                
            self.social_log.see(tk.END)
            
        except Exception as e:
            self.social_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.social_log.see(tk.END)
    
    # ===== MÉTHODES MANQUANTES POUR LES OPÉRATIONS FURTIVES =====
    
    def create_stealth_payload(self):
        """Crée un payload furtif"""
        try:
            os_target = self.stealth_os_var.get()
            level = self.stealth_level_var.get()
            
            self.stealth_log.insert(tk.END, f"👻 Création payload furtif {level} pour {os_target}...\n")
            self.stealth_log.see(tk.END)
            
            result = self.stealth.create_stealth_payload(os_target, level)
            
            if result:
                self.stealth_log.insert(tk.END, f"✅ Payload furtif créé: {result}\n")
            else:
                self.stealth_log.insert(tk.END, "❌ Erreur création payload furtif\n")
                
            self.stealth_log.see(tk.END)
            
        except Exception as e:
            self.stealth_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.stealth_log.see(tk.END)
    
    def create_rootkit(self):
        """Crée un rootkit"""
        try:
            os_target = self.rootkit_os_var.get()
            
            self.stealth_log.insert(tk.END, f"🕷️ Création rootkit pour {os_target}...\n")
            self.stealth_log.see(tk.END)
            
            result = self.stealth.create_rootkit(os_target)
            
            if result:
                self.stealth_log.insert(tk.END, f"✅ Rootkit créé: {result}\n")
            else:
                self.stealth_log.insert(tk.END, "❌ Erreur création rootkit\n")
                
            self.stealth_log.see(tk.END)
            
        except Exception as e:
            self.stealth_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.stealth_log.see(tk.END)
    
    def create_anti_forensics_tool(self):
        """Crée un outil anti-forensics"""
        try:
            self.stealth_log.insert(tk.END, "🔒 Création outil anti-forensics...\n")
            self.stealth_log.see(tk.END)
            
            result = self.stealth.create_anti_forensics_tool()
            
            if result:
                self.stealth_log.insert(tk.END, f"✅ Outil anti-forensics créé: {result}\n")
            else:
                self.stealth_log.insert(tk.END, "❌ Erreur création outil anti-forensics\n")
                
            self.stealth_log.see(tk.END)
            
        except Exception as e:
            self.stealth_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.stealth_log.see(tk.END)
    
    # ===== MÉTHODES MANQUANTES POUR LE MALWARE AVANCÉ =====
    
    def create_keylogger(self):
        """Crée un keylogger"""
        try:
            os_target = self.keylogger_os_var.get()
            
            self.malware_log.insert(tk.END, f"⌨️ Création keylogger pour {os_target}...\n")
            self.malware_log.see(tk.END)
            
            result = self.malware.create_keylogger(os_target)
            
            if result:
                self.malware_log.insert(tk.END, f"✅ Keylogger créé: {result}\n")
            else:
                self.malware_log.insert(tk.END, "❌ Erreur création keylogger\n")
                
            self.malware_log.see(tk.END)
            
        except Exception as e:
            self.malware_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.malware_log.see(tk.END)
    
    def create_ransomware(self):
        """Crée un ransomware"""
        try:
            os_target = self.ransomware_os_var.get()
            
            self.malware_log.insert(tk.END, f"🔒 Création ransomware pour {os_target}...\n")
            self.malware_log.see(tk.END)
            
            result = self.malware.create_ransomware(os_target)
            
            if result:
                self.malware_log.insert(tk.END, f"✅ Ransomware créé: {result}\n")
            else:
                self.malware_log.insert(tk.END, "❌ Erreur création ransomware\n")
                
            self.malware_log.see(tk.END)
            
        except Exception as e:
            self.malware_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.malware_log.see(tk.END)
    
    def create_cryptominer(self):
        """Crée un cryptominer"""
        try:
            os_target = self.miner_os_var.get()
            
            self.malware_log.insert(tk.END, f"⛏️ Création cryptominer pour {os_target}...\n")
            self.malware_log.see(tk.END)
            
            result = self.malware.create_cryptominer(os_target)
            
            if result:
                self.malware_log.insert(tk.END, f"✅ Cryptominer créé: {result}\n")
            else:
                self.malware_log.insert(tk.END, "❌ Erreur création cryptominer\n")
                
            self.malware_log.see(tk.END)
            
        except Exception as e:
            self.malware_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.malware_log.see(tk.END)
    
    # ===== MÉTHODES MANQUANTES POUR LES EXPLOITS ZERO-DAY =====
    
    def create_buffer_overflow_exploit(self):
        """Crée un exploit buffer overflow"""
        try:
            os_target = self.bof_os_var.get()
            service = self.bof_service_var.get()
            
            self.zero_day_log.insert(tk.END, f"🔥 Création exploit buffer overflow pour {service} sur {os_target}...\n")
            self.zero_day_log.see(tk.END)
            
            result = self.zero_day.create_buffer_overflow_exploit(os_target, service)
            
            if result:
                self.zero_day_log.insert(tk.END, f"✅ Exploit buffer overflow créé: {result}\n")
            else:
                self.zero_day_log.insert(tk.END, "❌ Erreur création exploit buffer overflow\n")
                
            self.zero_day_log.see(tk.END)
            
        except Exception as e:
            self.zero_day_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.zero_day_log.see(tk.END)
    
    def create_heap_spray_exploit(self):
        """Crée un exploit heap spraying"""
        try:
            os_target = self.heap_os_var.get()
            
            self.zero_day_log.insert(tk.END, f"💥 Création exploit heap spraying pour {os_target}...\n")
            self.zero_day_log.see(tk.END)
            
            result = self.zero_day.create_heap_spray_exploit(os_target)
            
            if result:
                self.zero_day_log.insert(tk.END, f"✅ Exploit heap spraying créé: {result}\n")
            else:
                self.zero_day_log.insert(tk.END, "❌ Erreur création exploit heap spraying\n")
                
            self.zero_day_log.see(tk.END)
            
        except Exception as e:
            self.zero_day_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.zero_day_log.see(tk.END)
    
    def create_rop_chain_exploit(self):
        """Crée un exploit ROP chain"""
        try:
            os_target = self.rop_os_var.get()
            arch = self.rop_arch_var.get()
            
            self.zero_day_log.insert(tk.END, f"🔗 Création exploit ROP chain {arch} pour {os_target}...\n")
            self.zero_day_log.see(tk.END)
            
            result = self.zero_day.create_rop_chain_exploit(os_target, arch)
            
            if result:
                self.zero_day_log.insert(tk.END, f"✅ Exploit ROP chain créé: {result}\n")
            else:
                self.zero_day_log.insert(tk.END, "❌ Erreur création exploit ROP chain\n")
                
            self.zero_day_log.see(tk.END)
            
        except Exception as e:
            self.zero_day_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.zero_day_log.see(tk.END)
    
    def create_format_string_exploit(self):
        """Crée un exploit format string"""
        try:
            os_target = self.format_os_var.get()
            
            self.zero_day_log.insert(tk.END, f"📝 Création exploit format string pour {os_target}...\n")
            self.zero_day_log.see(tk.END)
            
            result = self.zero_day.create_format_string_exploit(os_target)
            
            if result:
                self.zero_day_log.insert(tk.END, f"✅ Exploit format string créé: {result}\n")
            else:
                self.zero_day_log.insert(tk.END, "❌ Erreur création exploit format string\n")
                
            self.zero_day_log.see(tk.END)
            
        except Exception as e:
            self.zero_day_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.zero_day_log.see(tk.END)
    
    # ===== MÉTHODES MANQUANTES POUR LA PERSISTANCE AVANCÉE =====
    
    def create_bootkit(self):
        """Crée un bootkit"""
        try:
            os_target = self.bootkit_os_var.get()
            
            self.persistence_log.insert(tk.END, f"🕷️ Création bootkit pour {os_target}...\n")
            self.persistence_log.see(tk.END)
            
            result = self.persistence.create_bootkit(os_target)
            
            if result:
                self.persistence_log.insert(tk.END, f"✅ Bootkit créé: {result}\n")
            else:
                self.persistence_log.insert(tk.END, "❌ Erreur création bootkit\n")
                
            self.persistence_log.see(tk.END)
            
        except Exception as e:
            self.persistence_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.persistence_log.see(tk.END)
    
    def create_firmware_persistence(self):
        """Crée une persistance firmware"""
        try:
            os_target = self.firmware_os_var.get()
            
            self.persistence_log.insert(tk.END, f"🔧 Création persistance firmware pour {os_target}...\n")
            self.persistence_log.see(tk.END)
            
            result = self.persistence.create_firmware_persistence(os_target)
            
            if result:
                self.persistence_log.insert(tk.END, f"✅ Persistance firmware créée: {result}\n")
            else:
                self.persistence_log.insert(tk.END, "❌ Erreur création persistance firmware\n")
                
            self.persistence_log.see(tk.END)
            
        except Exception as e:
            self.persistence_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.persistence_log.see(tk.END)
    
    def create_kernel_rootkit(self):
        """Crée un kernel rootkit"""
        try:
            os_target = self.kernel_os_var.get()
            
            self.persistence_log.insert(tk.END, f"⚙️ Création kernel rootkit pour {os_target}...\n")
            self.persistence_log.see(tk.END)
            
            result = self.persistence.create_kernel_rootkit(os_target)
            
            if result:
                self.persistence_log.insert(tk.END, f"✅ Kernel rootkit créé: {result}\n")
            else:
                self.persistence_log.insert(tk.END, "❌ Erreur création kernel rootkit\n")
                
            self.persistence_log.see(tk.END)
            
        except Exception as e:
            self.persistence_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.persistence_log.see(tk.END)
    
    def create_hypervisor_rootkit(self):
        """Crée un hypervisor rootkit"""
        try:
            self.persistence_log.insert(tk.END, "🖥️ Création hypervisor rootkit...\n")
            self.persistence_log.see(tk.END)
            
            result = self.persistence.create_hypervisor_rootkit()
            
            if result:
                self.persistence_log.insert(tk.END, f"✅ Hypervisor rootkit créé: {result}\n")
            else:
                self.persistence_log.insert(tk.END, "❌ Erreur création hypervisor rootkit\n")
                
            self.persistence_log.see(tk.END)
            
        except Exception as e:
            self.persistence_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.persistence_log.see(tk.END)
    
    # ===== MÉTHODES MANQUANTES POUR L'EXPLOITATION WEB =====
    
    def scan_sql_injection(self):
        """Scanne les vulnérabilités SQL injection"""
        try:
            url = self.sql_url_var.get()
            points = self.sql_points_var.get()
            
            self.web_exploit_log.insert(tk.END, f"💉 Scan SQL injection sur {url}...\n")
            self.web_exploit_log.see(tk.END)
            
            result = self.web_exploit.scan_sql_injection(url, points.split(','))
            
            if result:
                self.web_exploit_log.insert(tk.END, f"✅ Scan SQL injection terminé: {len(result)} vulnérabilités trouvées\n")
            else:
                self.web_exploit_log.insert(tk.END, "❌ Erreur scan SQL injection\n")
                
            self.web_exploit_log.see(tk.END)
            
        except Exception as e:
            self.web_exploit_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.web_exploit_log.see(tk.END)
    
    def scan_xss(self):
        """Scanne les vulnérabilités XSS"""
        try:
            url = self.xss_url_var.get()
            points = self.xss_points_var.get()
            
            self.web_exploit_log.insert(tk.END, f"🎯 Scan XSS sur {url}...\n")
            self.web_exploit_log.see(tk.END)
            
            result = self.web_exploit.scan_xss(url, points.split(','))
            
            if result:
                self.web_exploit_log.insert(tk.END, f"✅ Scan XSS terminé: {len(result)} vulnérabilités trouvées\n")
            else:
                self.web_exploit_log.insert(tk.END, "❌ Erreur scan XSS\n")
                
            self.web_exploit_log.see(tk.END)
            
        except Exception as e:
            self.web_exploit_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.web_exploit_log.see(tk.END)
    
    def generate_csrf_exploit(self):
        """Génère un exploit CSRF"""
        try:
            url = self.csrf_url_var.get()
            action = self.csrf_action_var.get()
            
            self.web_exploit_log.insert(tk.END, f"🔄 Génération exploit CSRF pour {url}...\n")
            self.web_exploit_log.see(tk.END)
            
            result = self.web_exploit.generate_csrf_exploit(url, action)
            
            if result:
                self.web_exploit_log.insert(tk.END, f"✅ Exploit CSRF généré: {result}\n")
            else:
                self.web_exploit_log.insert(tk.END, "❌ Erreur génération exploit CSRF\n")
                
            self.web_exploit_log.see(tk.END)
            
        except Exception as e:
            self.web_exploit_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.web_exploit_log.see(tk.END)
    
    def create_upload_exploit(self):
        """Crée un exploit upload de fichier"""
        try:
            url = self.upload_url_var.get()
            path = self.upload_path_var.get()
            
            self.web_exploit_log.insert(tk.END, f"📁 Création exploit upload pour {url}...\n")
            self.web_exploit_log.see(tk.END)
            
            result = self.web_exploit.create_upload_exploit(url, path)
            
            if result:
                self.web_exploit_log.insert(tk.END, f"✅ Exploit upload créé: {result}\n")
            else:
                self.web_exploit_log.insert(tk.END, "❌ Erreur création exploit upload\n")
                
            self.web_exploit_log.see(tk.END)
            
        except Exception as e:
            self.web_exploit_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.web_exploit_log.see(tk.END)
    
    # ===== MÉTHODES MANQUANTES POUR L'OSINT =====
    
    def enumerate_subdomains(self):
        """Énumère les sous-domaines"""
        try:
            domain = self.subdomain_target_var.get()
            
            self.osint_log.insert(tk.END, f"🔍 Énumération sous-domaines pour {domain}...\n")
            self.osint_log.see(tk.END)
            
            result = self.osint.enumerate_subdomains(domain)
            
            if result:
                self.osint_log.insert(tk.END, f"✅ Énumération terminée: {len(result)} sous-domaines trouvés\n")
            else:
                self.osint_log.insert(tk.END, "❌ Erreur énumération sous-domaines\n")
                
            self.osint_log.see(tk.END)
            
        except Exception as e:
            self.osint_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.osint_log.see(tk.END)
    
    def harvest_emails(self):
        """Récolte les emails"""
        try:
            domain = self.email_target_var.get()
            
            self.osint_log.insert(tk.END, f"📧 Récolte emails pour {domain}...\n")
            self.osint_log.see(tk.END)
            
            result = self.osint.harvest_emails(domain)
            
            if result:
                self.osint_log.insert(tk.END, f"✅ Récolte terminée: {len(result)} emails trouvés\n")
            else:
                self.osint_log.insert(tk.END, "❌ Erreur récolte emails\n")
                
            self.osint_log.see(tk.END)
            
        except Exception as e:
            self.osint_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.osint_log.see(tk.END)
    
    def social_media_osint(self):
        """Effectue l'OSINT sur les réseaux sociaux"""
        try:
            organization = self.social_target_var.get()
            
            self.osint_log.insert(tk.END, f"📱 OSINT réseaux sociaux pour {organization}...\n")
            self.osint_log.see(tk.END)
            
            result = self.osint.social_media_osint(organization)
            
            if result:
                self.osint_log.insert(tk.END, f"✅ OSINT terminé: {len(result)} comptes trouvés\n")
            else:
                self.osint_log.insert(tk.END, "❌ Erreur OSINT réseaux sociaux\n")
                
            self.osint_log.see(tk.END)
            
        except Exception as e:
            self.osint_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.osint_log.see(tk.END)
    
    def monitor_certificates(self):
        """Surveille les certificats"""
        try:
            domain = self.ct_target_var.get()
            
            self.osint_log.insert(tk.END, f"🔒 Surveillance certificats pour {domain}...\n")
            self.osint_log.see(tk.END)
            
            result = self.osint.monitor_certificates(domain)
            
            if result:
                self.osint_log.insert(tk.END, f"✅ Surveillance terminée: {len(result)} certificats trouvés\n")
            else:
                self.osint_log.insert(tk.END, "❌ Erreur surveillance certificats\n")
                
            self.osint_log.see(tk.END)
            
        except Exception as e:
            self.osint_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.osint_log.see(tk.END)
    
    # ===== MÉTHODES MANQUANTES POUR ACTIVE DIRECTORY =====
    
    def kerberos_attack(self):
        """Lance une attaque Kerberos"""
        try:
            domain = self.kerberos_domain_var.get()
            users = self.kerberos_users_var.get()
            
            self.ad_log.insert(tk.END, f"🔑 Attaque Kerberos sur {domain}...\n")
            self.ad_log.see(tk.END)
            
            result = self.ad_attacks.kerberos_attack(domain, users.split(','))
            
            if result:
                self.ad_log.insert(tk.END, f"✅ Attaque Kerberos terminée: {len(result)} tickets trouvés\n")
            else:
                self.ad_log.insert(tk.END, "❌ Erreur attaque Kerberos\n")
                
            self.ad_log.see(tk.END)
            
        except Exception as e:
            self.ad_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.ad_log.see(tk.END)
    
    def bloodhound_collection(self):
        """Effectue la collecte BloodHound"""
        try:
            domain = self.bloodhound_domain_var.get()
            
            self.ad_log.insert(tk.END, f"🩸 Collecte BloodHound pour {domain}...\n")
            self.ad_log.see(tk.END)
            
            result = self.ad_attacks.bloodhound_collection(domain)
            
            if result:
                self.ad_log.insert(tk.END, f"✅ Collecte BloodHound terminée: {result}\n")
            else:
                self.ad_log.insert(tk.END, "❌ Erreur collecte BloodHound\n")
                
            self.ad_log.see(tk.END)
            
        except Exception as e:
            self.ad_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.ad_log.see(tk.END)
    
    def lateral_movement(self):
        """Effectue un mouvement latéral"""
        try:
            domain = self.lateral_domain_var.get()
            hosts = self.lateral_hosts_var.get()
            
            self.ad_log.insert(tk.END, f"🔄 Mouvement latéral sur {domain}...\n")
            self.ad_log.see(tk.END)
            
            result = self.ad_attacks.lateral_movement(domain, hosts.split(','))
            
            if result:
                self.ad_log.insert(tk.END, f"✅ Mouvement latéral terminé: {len(result)} hôtes compromis\n")
            else:
                self.ad_log.insert(tk.END, "❌ Erreur mouvement latéral\n")
                
            self.ad_log.see(tk.END)
            
        except Exception as e:
            self.ad_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.ad_log.see(tk.END)
    
    def ad_privilege_escalation(self):
        """Effectue l'escalade de privilèges AD"""
        try:
            domain = self.escalation_domain_var.get()
            
            self.ad_log.insert(tk.END, f"🔓 Escalade privilèges AD sur {domain}...\n")
            self.ad_log.see(tk.END)
            
            result = self.ad_attacks.privilege_escalation(domain)
            
            if result:
                self.ad_log.insert(tk.END, f"✅ Escalade privilèges terminée: {result}\n")
            else:
                self.ad_log.insert(tk.END, "❌ Erreur escalade privilèges\n")
                
            self.ad_log.see(tk.END)
            
        except Exception as e:
            self.ad_log.insert(tk.END, f"❌ Erreur: {e}\n")
            self.ad_log.see(tk.END)
            
    def run(self):
        """Lance l'application"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.cleanup()
            
    def cleanup(self):
        """Nettoie les ressources"""
        print("🧹 Nettoyage...")
        if self.server_running:
            self.phishing.stop_server()
        self.tunnels.stop_all_tunnels()
        print("✅ Nettoyage terminé")

def main():
    """Fonction principale"""
    # Créer les dossiers nécessaires
    directories = ['templates', 'cloned_sites', 'exports', 'logs']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            
    # Lancer l'application
    app = UltimatePhishingGUI()
    app.run()

if __name__ == "__main__":
    main() 