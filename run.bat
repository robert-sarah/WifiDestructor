@echo off
echo 🎣 Phishing Tool Pro v2.0 - BlackEye + CamPhish Enhanced
echo ==================================================

REM Vérifier si l'environnement virtuel existe
if not exist "venv" (
    echo ❌ Environnement virtuel non trouvé. Lancement de l'installation...
    call install.bat
    if errorlevel 1 (
        echo ❌ Échec de l'installation
        pause
        exit /b 1
    )
)

REM Activer l'environnement virtuel
echo 🔧 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Lancer l'application
echo 🚀 Lancement de Phishing Tool Pro...
python phishing_tool.py

REM Pause pour voir les erreurs éventuelles
pause 