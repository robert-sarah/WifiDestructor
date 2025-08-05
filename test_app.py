#!/usr/bin/env python3
"""
Script de test pour l'application Ultimate Phishing GUI
"""

import sys
import os
import platform
import subprocess

def test_python_modules():
    """Teste les modules Python requis"""
    print("🔍 Test des modules Python...")
    
    required_modules = [
        'tkinter',
        'threading',
        'subprocess',
        'platform',
        'sys',
        'os'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} disponible")
        except ImportError:
            print(f"❌ {module} manquant")
            missing_modules.append(module)
    
    return missing_modules

def test_system_tools():
    """Teste les outils système"""
    print("\n🔍 Test des outils système...")
    
    os_type = platform.system().lower()
    
    # Outils critiques
    critical_tools = {
        'linux': ['nmap'],
        'darwin': ['nmap'],
        'windows': ['nmap']
    }
    
    # Outils optionnels
    optional_tools = {
        'linux': ['aircrack-ng', 'masscan'],
        'darwin': ['aircrack-ng', 'masscan'],
        'windows': ['aircrack-ng', 'masscan']
    }
    
    critical_to_check = critical_tools.get(os_type, [])
    optional_to_check = optional_tools.get(os_type, [])
    
    missing_critical = []
    missing_optional = []
    
    # Test des outils critiques
    for tool in critical_to_check:
        try:
            result = subprocess.run([tool, '--version'], 
                                 capture_output=True, 
                                 timeout=3)
            print(f"✅ {tool} disponible (critique)")
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            print(f"❌ {tool} manquant (CRITIQUE)")
            missing_critical.append(tool)
    
    # Test des outils optionnels
    for tool in optional_to_check:
        try:
            result = subprocess.run([tool, '--version'], 
                                 capture_output=True, 
                                 timeout=3)
            print(f"✅ {tool} disponible (optionnel)")
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            print(f"⚠️ {tool} non disponible (optionnel)")
            missing_optional.append(tool)
    
    return missing_critical, missing_optional

def test_file_structure():
    """Teste la structure des fichiers"""
    print("\n🔍 Test de la structure des fichiers...")
    
    required_files = [
        'ultimate_phishing_gui.py',
        'requirements.txt',
        'README.md'
    ]
    
    optional_files = [
        'install.sh',
        'install.bat',
        'test_detection.py'
    ]
    
    missing_required = []
    missing_optional = []
    
    # Test des fichiers requis
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} présent")
        else:
            print(f"❌ {file} manquant")
            missing_required.append(file)
    
    # Test des fichiers optionnels
    for file in optional_files:
        if os.path.exists(file):
            print(f"✅ {file} présent (optionnel)")
        else:
            print(f"⚠️ {file} non présent (optionnel)")
            missing_optional.append(file)
    
    return missing_required, missing_optional

def test_application_import():
    """Teste l'import de l'application"""
    print("\n🔍 Test de l'import de l'application...")
    
    try:
        # Ajouter le répertoire courant au path
        sys.path.insert(0, os.getcwd())
        
        # Importer l'application
        import ultimate_phishing_gui
        print("✅ Import de ultimate_phishing_gui réussi")
        
        # Tester l'import des fonctions principales
        from ultimate_phishing_gui import check_system_dependencies, check_tool_availability
        print("✅ Import des fonctions de détection réussi")
        
        return True
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        return False
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🧪 TEST COMPLET DE L'APPLICATION")
    print("=" * 50)
    
    print(f"🖥️ Système: {platform.system()} {platform.release()}")
    print(f"🐍 Python: {sys.version}")
    print(f"📁 Répertoire: {os.getcwd()}")
    print()
    
    # Tests
    missing_modules = test_python_modules()
    missing_critical, missing_optional = test_system_tools()
    missing_required, missing_optional_files = test_file_structure()
    import_success = test_application_import()
    
    # Résumé
    print("\n" + "=" * 50)
    print("📊 RÉSULTATS DU TEST")
    print("=" * 50)
    
    all_tests_passed = True
    
    if missing_modules:
        print(f"❌ Modules Python manquants: {', '.join(missing_modules)}")
        all_tests_passed = False
    else:
        print("✅ Tous les modules Python sont disponibles")
    
    if missing_critical:
        print(f"❌ Outils critiques manquants: {', '.join(missing_critical)}")
        all_tests_passed = False
    else:
        print("✅ Tous les outils critiques sont disponibles")
    
    if missing_required:
        print(f"❌ Fichiers requis manquants: {', '.join(missing_required)}")
        all_tests_passed = False
    else:
        print("✅ Tous les fichiers requis sont présents")
    
    if not import_success:
        print("❌ L'application ne peut pas être importée")
        all_tests_passed = False
    else:
        print("✅ L'application peut être importée correctement")
    
    # Recommandations
    print("\n🎯 RECOMMANDATIONS:")
    
    if missing_critical:
        os_type = platform.system().lower()
        print("⚠️ Installez les outils critiques manquants:")
        if os_type in ['linux', 'darwin']:
            print("  Debian/Ubuntu: sudo apt-get install nmap")
            print("  macOS: brew install nmap")
        elif os_type == 'windows':
            print("  Windows: Téléchargez nmap depuis https://nmap.org/download.html")
    
    if missing_optional:
        print(f"📋 Outils optionnels non disponibles: {', '.join(missing_optional)}")
        print("💡 Ces outils améliorent les fonctionnalités mais ne sont pas critiques")
    
    if missing_modules:
        print("📦 Installez les modules Python manquants:")
        print("  pip install -r requirements.txt")
    
    # Conclusion
    print("\n" + "=" * 50)
    if all_tests_passed:
        print("🎉 TOUS LES TESTS SONT RÉUSSIS!")
        print("🚀 L'application est prête à être utilisée")
    else:
        print("⚠️ CERTAINS TESTS ONT ÉCHOUÉ")
        print("💡 Corrigez les problèmes avant d'utiliser l'application")
    
    return all_tests_passed

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        sys.exit(1) 