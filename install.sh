#!/bin/bash

echo "🎣 Installation de Phishing Tool Pro v2.0 (BlackEye + CamPhish Enhanced)"
echo "=================================================="

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

echo "✅ Python3 détecté"

# Créer l'environnement virtuel
echo "🔧 Création de l'environnement virtuel..."
python3 -m venv venv

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances
echo "📦 Installation des dépendances..."
pip install --upgrade pip
pip install -r requirements.txt

# Créer les dossiers nécessaires
echo "📁 Création des dossiers..."
mkdir -p templates
mkdir -p captures
mkdir -p logs

echo "✅ Installation terminée!"
echo ""
echo "🚀 Pour lancer l'outil:"
echo "   source venv/bin/activate"
echo "   python3 phishing_tool.py"
echo ""
echo "🎯 Fonctionnalités disponibles:"
echo "   - Templates BlackEye (16 sites)"
echo "   - Capture webcam (CamPhish)"
echo "   - Géolocalisation avancée"
echo "   - Détection navigateur/OS"
echo "   - Interface moderne"
echo ""
echo "⚠️  ATTENTION: Utilisez uniquement pour des tests éthiques!" 