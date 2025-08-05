# 🎣 ULTIMATE PHISHING TOOL v4.0

Interface graphique moderne pour le pentest avancé avec support cross-platform complet.

## 🌍 Compatibilité

| Système | Statut | Installation |
|---------|---------|--------------|
| **Windows** | ✅ 100% | `install.bat` |
| **Debian/Ubuntu** | ✅ 100% | `bash install.sh` |
| **macOS** | ✅ 100% | `bash install.sh` |
| **Arch Linux** | ✅ 100% | `bash install.sh` |

## 🚀 Installation Rapide

### Windows
```cmd
# Double-cliquez sur install.bat
# Ou exécutez en ligne de commande:
install.bat
```

### Linux/macOS
```bash
# Rendre le script exécutable
chmod +x install.sh

# Exécuter l'installation
bash install.sh
```

## 📦 Installation Manuelle

### Prérequis

#### Windows
- Python 3.8+ (https://python.org)
- pip (inclus avec Python)
- nmap (https://nmap.org/download.html)

#### Linux (Debian/Ubuntu)
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv aircrack-ng nmap masscan
```

#### macOS
```bash
# Installer Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installer les outils
brew install python3 aircrack-ng nmap masscan
```

### Installation Python

1. **Cloner le projet**
```bash
git clone <repository-url>
cd WifiDestructor2
```

2. **Créer l'environnement virtuel**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate.bat  # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

## 🎯 Utilisation

### Lancement
```bash
# Activer l'environnement virtuel
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate.bat  # Windows

# Lancer l'application
python ultimate_phishing_gui.py
```

### Permissions Requises

#### Linux/macOS
```bash
# Pour les attaques WiFi (optionnel)
sudo usermod -a -G netdev $USER
# Redémarrez votre session
```

#### Windows
- Exécutez en tant qu'administrateur pour les fonctionnalités avancées

## 🔧 Fonctionnalités

### 🎣 Phishing
- Templates personnalisables
- Clonage de sites web
- Gestion des tunnels (ngrok, Cloudflare)
- Capture automatique des credentials

### 📡 Attaques WiFi
- Scan des réseaux
- Attaques de désauthentification
- Capture de handshake WPA/WPA2
- Crack de mots de passe
- Points d'accès factices
- Attaques Evil Twin
- Attaques WPS

### 🌐 Réseau
- Scan de ports (nmap, masscan)
- Énumération de services
- Scan de vulnérabilités
- Énumération DNS/subdomaines

### 🚪 Backdoors
- Windows Registry/Service
- Linux Cron/Service
- Persistence avancée
- Rootkits

### 💣 Exploits Avancés
- Exploits personnalisés
- Escalade de privilèges
- Virus polymorphes
- Buffer overflow
- ROP chains

### 🎭 Ingénierie Sociale
- Campagnes de phishing
- Scénarios de prétexte
- Scripts de vishing
- Opérations furtives

### 🦠 Malware
- Keyloggers
- Ransomware
- Cryptominers
- Rootkits avancés

### 🔍 OSINT
- Énumération de sous-domaines
- Harvesting d'emails
- OSINT réseaux sociaux
- Monitoring de certificats

### 🏢 Active Directory
- Attaques Kerberos
- BloodHound
- Mouvement latéral
- Escalade de privilèges AD

## 🛠️ Dépannage

### Erreurs Communes

#### "Permission denied"
```bash
# Linux/macOS
sudo python ultimate_phishing_gui.py

# Windows
# Exécutez en tant qu'administrateur
```

#### "aircrack-ng not found"
```bash
# Debian/Ubuntu
sudo apt-get install aircrack-ng

# macOS
brew install aircrack-ng

# Windows
# Téléchargez depuis https://www.aircrack-ng.org/
```

#### "nmap not found"
```bash
# Debian/Ubuntu
sudo apt-get install nmap

# macOS
brew install nmap

# Windows
# Téléchargez depuis https://nmap.org/download.html
```

#### Erreurs de modules Python
```bash
# Réinstaller les dépendances
pip install -r requirements.txt

# Ou utiliser le script d'installation
bash install.sh  # Linux/macOS
install.bat      # Windows
```

### Vérification de l'Installation

```bash
# Tester l'application
python -c "from ultimate_phishing_gui import UltimatePhishingGUI; print('✅ Installation OK')"

# Vérifier les outils
aircrack-ng --version
nmap --version
```

## 📁 Structure du Projet

```
WifiDestructor2/
├── ultimate_phishing_gui.py    # Interface principale
├── install.sh                  # Script d'installation Linux/macOS
├── install.bat                 # Script d'installation Windows
├── requirements.txt            # Dépendances Python
├── core/                       # Modules de base
│   ├── phishing_core.py
│   ├── wifi_attacks.py
│   ├── network_scanner.py
│   └── ...
├── templates/                  # Templates de phishing
├── logs/                       # Logs d'activité
├── payloads/                   # Payloads générés
├── backdoors/                  # Backdoors créés
├── exploits/                   # Exploits générés
├── captures/                   # Captures WiFi
└── config/                     # Configuration
```

## ⚠️ Avertissement Légal

**⚠️ ATTENTION: Cet outil est destiné UNIQUEMENT à des fins éducatives et de test de pénétration autorisées.**

- Utilisez uniquement sur vos propres systèmes ou avec autorisation explicite
- Respectez les lois locales sur la cybersécurité
- Les auteurs ne sont pas responsables de l'utilisation malveillante
- Testez toujours dans un environnement contrôlé

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter de nouvelles fonctionnalités
- Améliorer la documentation

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🆘 Support

Pour obtenir de l'aide :
1. Consultez ce README
2. Vérifiez les logs dans le dossier `logs/`
3. Exécutez `bash install.sh` pour réparer l'installation
4. Ouvrez une issue sur GitHub

---

**🎣 ULTIMATE PHISHING TOOL v4.0 - Cross-Platform Pentesting GUI** 