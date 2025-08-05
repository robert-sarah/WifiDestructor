@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM 🎣 ULTIMATE PHISHING TOOL v4.0 - Script d'Installation Windows
REM Compatible: Windows 10/11

echo.
echo ================================
echo 🎣 ULTIMATE PHISHING TOOL v4.0
echo    Installation Windows
echo ================================
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python n'est pas installé!
    echo 📦 Téléchargez Python depuis https://python.org
    echo 💡 Assurez-vous de cocher "Add Python to PATH"
    pause
    exit /b 1
) else (
    echo ✅ Python est installé
)

REM Vérifier si pip est installé
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip n'est pas installé!
    echo 📦 Réinstallez Python avec pip
    pause
    exit /b 1
) else (
    echo ✅ pip est installé
)

REM Créer un environnement virtuel
if not exist "venv" (
    echo 📦 Création de l'environnement virtuel...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo ❌ Erreur création environnement virtuel
        pause
        exit /b 1
    )
    echo ✅ Environnement virtuel créé
) else (
    echo ✅ Environnement virtuel existant
)

REM Activer l'environnement virtuel
echo 📦 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Mettre à jour pip
echo 📦 Mise à jour de pip...
python -m pip install --upgrade pip

REM Installer les dépendances Python
echo 📦 Installation des dépendances Python...
if exist "requirements.txt" (
    pip install -r requirements.txt
) else (
    echo ⚠️ Fichier requirements.txt non trouvé
)

REM Installer les dépendances supplémentaires
echo 📦 Installation des dépendances supplémentaires...
pip install flask==2.3.3 requests==2.31.0 user-agents==2.2.0 geocoder==1.38.1 beautifulsoup4==4.12.2 colorama==0.4.6 paramiko==3.3.1 python-nmap==0.7.1 qrcode==7.4.2 Pillow==10.0.1 pynput>=1.7.6 cryptography>=3.4.8 dnspython>=2.2.1 python-whois>=0.7.1 shodan>=1.28.1

REM Créer les dossiers nécessaires
echo 📁 Création des dossiers...
if not exist "templates" mkdir templates
if not exist "logs" mkdir logs
if not exist "payloads" mkdir payloads
if not exist "backdoors" mkdir backdoors
if not exist "exploits" mkdir exploits
if not exist "captures" mkdir captures
if not exist "config" mkdir config
if not exist "data" mkdir data
echo ✅ Dossiers créés

REM Vérifier les outils de sécurité
echo 🔍 Vérification des outils de sécurité...

REM Vérifier nmap (critique)
nmap --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ nmap disponible (critique)
) else (
    echo ❌ nmap manquant (CRITIQUE)
    echo 📦 Téléchargez nmap depuis https://nmap.org/download.html
)

REM Vérifier aircrack-ng (optionnel sur Windows)
aircrack-ng --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ aircrack-ng disponible (optionnel)
) else (
    echo ⚠️ aircrack-ng non disponible (optionnel sur Windows)
    echo 📦 Téléchargez depuis https://www.aircrack-ng.org/
)

REM Vérifier masscan (optionnel)
masscan --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ masscan disponible (optionnel)
) else (
    echo ⚠️ masscan non disponible (optionnel)
    echo 📦 Téléchargez depuis https://github.com/robertdavidgraham/masscan
)

REM Test de l'installation
echo 🧪 Test de l'installation...

REM Tester Tkinter
python -c "import tkinter; print('Tkinter OK')" 2>nul
if %errorlevel% equ 0 (
    echo ✅ Tkinter disponible
) else (
    echo ❌ Tkinter non disponible
)

REM Tester les modules principaux
for %%m in (flask requests paramiko cryptography) do (
    python -c "import %%m; print('%%m OK')" 2>nul
    if !errorlevel! equ 0 (
        echo ✅ %%m disponible
    ) else (
        echo ❌ %%m non disponible
    )
)

REM Tester l'application
python -c "import sys; sys.path.append('.'); from ultimate_phishing_gui import UltimatePhishingGUI; print('Application OK')" 2>nul
if %errorlevel% equ 0 (
    echo ✅ Application principale OK
) else (
    echo ❌ Erreur dans l'application principale
)

echo.
echo ==========================================
echo 🎣 INSTALLATION TERMINÉE AVEC SUCCÈS! 🎣
echo ==========================================
echo.
echo 📋 Pour lancer l'application:
echo   python ultimate_phishing_gui.py
echo   ou
echo   python run.py
echo.
echo 📋 Instructions importantes:
echo   - Exécutez en tant qu'administrateur pour les attaques WiFi
echo   - Installez les outils manquants si nécessaire
echo   - nmap: https://nmap.org/download.html
echo   - aircrack-ng: https://www.aircrack-ng.org/
echo.
echo ⚠️  UTILISEZ CET OUTIL UNIQUEMENT À DES FINS ÉDUCATIVES ET LÉGALES! ⚠️
echo.
pause 