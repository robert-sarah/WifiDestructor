#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de test pour Phishing Tool Pro v2.0
Vérifie que toutes les dépendances et fonctionnalités sont opérationnelles
"""

import sys
import importlib

def test_imports():
    """Teste l'importation de toutes les dépendances"""
    print("🔍 Test des dépendances...")
    
    required_modules = [
        'flask',
        'flask_socketio', 
        'cv2',
        'PIL',
        'qrcode',
        'requests',
        'geocoder',
        'user_agents',
        'psutil',
        'tkinter',
        'threading',
        'json',
        'datetime',
        'base64',
        'io'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n❌ {len(failed_imports)} module(s) manquant(s): {', '.join(failed_imports)}")
        return False
    else:
        print(f"\n✅ Tous les modules sont installés ({len(required_modules)} modules)")
        return True

def test_functionality():
    """Teste les fonctionnalités de base"""
    print("\n🔧 Test des fonctionnalités...")
    
    # Test Flask
    try:
        from flask import Flask
        app = Flask(__name__)
        print("✅ Flask fonctionne")
    except Exception as e:
        print(f"❌ Flask: {e}")
        return False
    
    # Test OpenCV
    try:
        import cv2
        print("✅ OpenCV fonctionne")
    except Exception as e:
        print(f"❌ OpenCV: {e}")
        return False
    
    # Test QR Code
    try:
        import qrcode
        qr = qrcode.QRCode()
        print("✅ QR Code fonctionne")
    except Exception as e:
        print(f"❌ QR Code: {e}")
        return False
    
    # Test Géolocalisation
    try:
        import geocoder
        print("✅ Géolocalisation fonctionne")
    except Exception as e:
        print(f"❌ Géolocalisation: {e}")
        return False
    
    # Test User Agents
    try:
        from user_agents import parse
        ua = parse("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        print("✅ User Agents fonctionne")
    except Exception as e:
        print(f"❌ User Agents: {e}")
        return False
    
    return True

def test_file_structure():
    """Teste la structure des fichiers"""
    print("\n📁 Test de la structure des fichiers...")
    
    import os
    
    required_files = [
        'phishing_tool.py',
        'requirements.txt',
        'README.md',
        'install.sh',
        'run.bat',
        'install.bat'
    ]
    
    required_dirs = [
        'templates',
        'captures',
        'logs'
    ]
    
    missing_files = []
    missing_dirs = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file}")
            missing_files.append(file)
    
    for dir in required_dirs:
        if os.path.exists(dir):
            print(f"✅ {dir}/")
        else:
            print(f"❌ {dir}/")
            missing_dirs.append(dir)
    
    if missing_files or missing_dirs:
        print(f"\n⚠️  Fichiers/dossiers manquants: {len(missing_files) + len(missing_dirs)}")
        return False
    else:
        print(f"\n✅ Structure des fichiers correcte")
        return True

def main():
    """Fonction principale de test"""
    print("🎣 Test de Phishing Tool Pro v2.0 - BlackEye + CamPhish Enhanced")
    print("=" * 60)
    
    # Tests
    imports_ok = test_imports()
    functionality_ok = test_functionality()
    structure_ok = test_file_structure()
    
    print("\n" + "=" * 60)
    print("📊 RÉSULTATS DES TESTS")
    print("=" * 60)
    
    if imports_ok and functionality_ok and structure_ok:
        print("🎉 TOUS LES TESTS SONT PASSÉS!")
        print("✅ L'installation est complète et fonctionnelle")
        print("\n🚀 Vous pouvez maintenant lancer l'outil:")
        print("   python phishing_tool.py")
        print("   ou")
        print("   run.bat (Windows)")
        print("   ./install.sh (Linux/Mac)")
        return True
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("⚠️  Veuillez corriger les problèmes avant d'utiliser l'outil")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 