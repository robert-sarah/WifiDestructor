#!/usr/bin/env python3
"""
Script de test pour vérifier la détection des outils
"""

import subprocess
import platform
import sys

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

def test_detection():
    """Teste la détection des outils"""
    print("🧪 Test de détection des outils")
    print("=" * 50)
    
    os_type = platform.system().lower()
    print(f"🖥️ Système détecté: {os_type}")
    print()
    
    # Outils CRITIQUES selon l'OS
    critical_tools = {
        'linux': ['nmap'],
        'darwin': ['nmap'],
        'windows': ['nmap']
    }
    
    # Outils OPTIONNELS selon l'OS
    optional_tools_list = {
        'linux': ['aircrack-ng', 'masscan'],
        'darwin': ['aircrack-ng', 'masscan'],
        'windows': ['aircrack-ng', 'masscan']
    }
    
    critical_to_check = critical_tools.get(os_type, [])
    optional_to_check = optional_tools_list.get(os_type, [])
    
    print("🔍 Test des outils critiques...")
    missing_critical = []
    for tool in critical_to_check:
        if not check_tool_availability(tool, "critique"):
            missing_critical.append(tool)
    
    print("\n🔍 Test des outils optionnels...")
    missing_optional = []
    for tool in optional_to_check:
        if not check_tool_availability(tool, "optionnel"):
            missing_optional.append(tool)
    
    print("\n📊 Résumé du test:")
    print("-" * 30)
    
    if missing_critical:
        print(f"❌ Outils critiques manquants: {', '.join(missing_critical)}")
        print("💡 Ces outils sont nécessaires pour le bon fonctionnement")
    else:
        print("✅ Tous les outils critiques sont disponibles")
    
    if missing_optional:
        print(f"📋 Outils optionnels non disponibles: {', '.join(missing_optional)}")
        print("💡 Ces outils améliorent les fonctionnalités mais ne sont pas critiques")
    else:
        print("✅ Tous les outils optionnels sont disponibles")
    
    print("\n🎯 Recommandations:")
    if missing_critical:
        print("⚠️ Installez les outils critiques manquants:")
        if os_type in ['linux', 'darwin']:
            print("  Debian/Ubuntu: sudo apt-get install nmap")
            print("  macOS: brew install nmap")
        elif os_type == 'windows':
            print("  Windows: Téléchargez nmap depuis https://nmap.org/download.html")
    
    if missing_optional:
        print("📦 Pour installer les outils optionnels:")
        if os_type in ['linux', 'darwin']:
            print("  Debian/Ubuntu: sudo apt-get install aircrack-ng masscan")
            print("  macOS: brew install aircrack-ng masscan")
        elif os_type == 'windows':
            print("  Windows: Ces outils sont optionnels sur Windows")
    
    return missing_critical, missing_optional

if __name__ == "__main__":
    try:
        missing_critical, missing_optional = test_detection()
        
        print("\n" + "=" * 50)
        if not missing_critical:
            print("🎉 Test réussi: Tous les outils critiques sont disponibles!")
        else:
            print("⚠️ Test incomplet: Certains outils critiques sont manquants")
            
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        sys.exit(1)