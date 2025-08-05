#!/bin/bash

# 🎣 ULTIMATE PHISHING TOOL v4.0 - Script d'Installation Cross-Platform
# Compatible: Debian, Ubuntu, macOS, Windows (WSL)

set -e  # Arrêter en cas d'erreur

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Fonction d'affichage avec couleurs
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${PURPLE}================================${NC}"
    echo -e "${PURPLE}🎣 ULTIMATE PHISHING TOOL v4.0${NC}"
    echo -e "${PURPLE}   Installation Cross-Platform${NC}"
    echo -e "${PURPLE}================================${NC}"
}

# Détection du système d'exploitation
detect_os() {
    print_status "Détection du système d'exploitation..."
    
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if command -v apt-get &> /dev/null; then
            OS="debian"
            PACKAGE_MANAGER="apt-get"
        elif command -v yum &> /dev/null; then
            OS="rhel"
            PACKAGE_MANAGER="yum"
        elif command -v pacman &> /dev/null; then
            OS="arch"
            PACKAGE_MANAGER="pacman"
        else
            OS="linux"
            PACKAGE_MANAGER="unknown"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        PACKAGE_MANAGER="brew"
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        OS="windows"
        PACKAGE_MANAGER="choco"
    else
        OS="unknown"
        PACKAGE_MANAGER="unknown"
    fi
    
    print_success "Système détecté: $OS ($PACKAGE_MANAGER)"
}

# Vérification des prérequis
check_prerequisites() {
    print_status "Vérification des prérequis..."
    
    # Vérifier Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 n'est pas installé!"
        print_status "Installation de Python 3..."
        
        case $OS in
            "debian"|"ubuntu")
                sudo apt-get update
                sudo apt-get install -y python3 python3-pip python3-venv
                ;;
            "macos")
                if ! command -v brew &> /dev/null; then
                    print_error "Homebrew n'est pas installé!"
                    print_status "Installation de Homebrew..."
                    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
                fi
                brew install python3
                ;;
            "windows")
                print_warning "Veuillez installer Python 3 manuellement depuis python.org"
                ;;
            *)
                print_error "Système non supporté pour l'installation automatique de Python"
                ;;
        esac
    else
        print_success "Python 3 est installé"
    fi
    
    # Vérifier pip
    if ! command -v pip3 &> /dev/null; then
        print_error "pip3 n'est pas installé!"
        case $OS in
            "debian"|"ubuntu")
                sudo apt-get install -y python3-pip
                ;;
            "macos")
                brew install python3
                ;;
        esac
    else
        print_success "pip3 est installé"
    fi
}

# Installation des dépendances système
install_system_dependencies() {
    print_status "Installation des dépendances système..."
    
    case $OS in
        "debian"|"ubuntu")
            print_status "Mise à jour des paquets..."
            sudo apt-get update
            
            print_status "Installation des outils de sécurité..."
            sudo apt-get install -y \
                aircrack-ng \
                nmap \
                masscan \
                git \
                curl \
                wget \
                build-essential \
                libssl-dev \
                libffi-dev \
                python3-dev
            ;;
            
        "macos")
            if ! command -v brew &> /dev/null; then
                print_error "Homebrew n'est pas installé!"
                exit 1
            fi
            
            print_status "Installation des outils de sécurité..."
            brew install \
                aircrack-ng \
                nmap \
                masscan \
                git \
                curl \
                wget
            ;;
            
        "windows")
            print_warning "Installation manuelle requise sur Windows:"
            print_status "- Installez aircrack-ng depuis https://www.aircrack-ng.org/"
            print_status "- Installez nmap depuis https://nmap.org/download.html"
            print_status "- Installez masscan depuis https://github.com/robertdavidgraham/masscan"
            ;;
            
        *)
            print_warning "Système non supporté pour l'installation automatique"
            ;;
    esac
}

# Installation des dépendances Python
install_python_dependencies() {
    print_status "Installation des dépendances Python..."
    
    # Créer un environnement virtuel
    if [ ! -d "venv" ]; then
        print_status "Création de l'environnement virtuel..."
        python3 -m venv venv
    fi
    
    # Activer l'environnement virtuel
    source venv/bin/activate
    
    # Mettre à jour pip
    pip install --upgrade pip
    
    # Installer les dépendances
    if [ -f "requirements.txt" ]; then
        print_status "Installation des dépendances depuis requirements.txt..."
        pip install -r requirements.txt
    else
        print_warning "Fichier requirements.txt non trouvé!"
    fi
    
    # Installer les dépendances supplémentaires
    print_status "Installation des dépendances supplémentaires..."
    pip install \
        flask==2.3.3 \
        requests==2.31.0 \
        user-agents==2.2.0 \
        geocoder==1.38.1 \
        beautifulsoup4==4.12.2 \
        colorama==0.4.6 \
        paramiko==3.3.1 \
        python-nmap==0.7.1 \
        qrcode==7.4.2 \
        Pillow==10.0.1 \
        pynput>=1.7.6 \
        cryptography>=3.4.8 \
        dnspython>=2.2.1 \
        python-whois>=0.7.1 \
        shodan>=1.28.1
}

# Vérification des outils de sécurité
check_security_tools() {
    print_status "Vérification des outils de sécurité..."
    
    local critical_tools=("nmap")
    local optional_tools=("aircrack-ng" "masscan")
    local missing_critical=()
    local missing_optional=()
    
    # Vérifier les outils critiques
    print_status "Vérification des outils critiques..."
    for tool in "${critical_tools[@]}"; do
        if command -v "$tool" &> /dev/null; then
            print_success "$tool ✓ (critique)"
        else
            missing_critical+=("$tool")
            print_error "$tool manquant (CRITIQUE)"
        fi
    done
    
    # Vérifier les outils optionnels
    print_status "Vérification des outils optionnels..."
    for tool in "${optional_tools[@]}"; do
        if command -v "$tool" &> /dev/null; then
            print_success "$tool ✓ (optionnel)"
        else
            missing_optional+=("$tool")
            print_warning "$tool non disponible (optionnel)"
        fi
    done
    
    # Installer seulement les outils critiques manquants
    if [ ${#missing_critical[@]} -ne 0 ]; then
        print_warning "Outils critiques manquants: ${missing_critical[*]}"
        print_status "Installation des outils critiques..."
        
        case $OS in
            "debian"|"ubuntu")
                for tool in "${missing_critical[@]}"; do
                    sudo apt-get install -y "$tool"
                done
                ;;
            "macos")
                for tool in "${missing_critical[@]}"; do
                    brew install "$tool"
                done
                ;;
            *)
                print_error "Installation manuelle requise pour: ${missing_critical[*]}"
                ;;
        esac
    else
        print_success "Tous les outils critiques sont disponibles"
    fi
    
    # Informer sur les outils optionnels
    if [ ${#missing_optional[@]} -ne 0 ]; then
        print_warning "Outils optionnels non disponibles: ${missing_optional[*]}"
        print_status "Ces outils améliorent les fonctionnalités mais ne sont pas critiques"
        
        case $OS in
            "debian"|"ubuntu")
                print_status "Pour installer les outils optionnels:"
                print_status "sudo apt-get install aircrack-ng masscan"
                ;;
            "macos")
                print_status "Pour installer les outils optionnels:"
                print_status "brew install aircrack-ng masscan"
                ;;
        esac
    fi
}

# Création des dossiers nécessaires
create_directories() {
    print_status "Création des dossiers nécessaires..."
    
    local directories=(
        "templates"
        "logs"
        "payloads"
        "backdoors"
        "exploits"
        "captures"
        "config"
        "data"
    )
    
    for dir in "${directories[@]}"; do
        if [ ! -d "$dir" ]; then
            mkdir -p "$dir"
            print_success "Dossier créé: $dir"
        else
            print_success "Dossier existant: $dir"
        fi
    done
}

# Configuration des permissions
setup_permissions() {
    print_status "Configuration des permissions..."
    
    case $OS in
        "debian"|"ubuntu"|"macos")
            # Rendre le script exécutable
            chmod +x install.sh
            chmod +x run.py
            chmod +x launch.py
            
            # Permissions pour les captures WiFi (Linux/macOS)
            if command -v aircrack-ng &> /dev/null; then
                print_status "Configuration des permissions WiFi..."
                sudo usermod -a -G netdev $USER 2>/dev/null || true
            fi
            ;;
        "windows")
            print_status "Permissions configurées pour Windows"
            ;;
    esac
}

# Test de l'installation
test_installation() {
    print_status "Test de l'installation..."
    
    # Tester Python
    if python3 -c "import tkinter; print('Tkinter OK')" 2>/dev/null; then
        print_success "Tkinter ✓"
    else
        print_error "Tkinter non disponible!"
    fi
    
    # Tester les modules principaux
    local modules=("flask" "requests" "paramiko" "cryptography")
    for module in "${modules[@]}"; do
        if python3 -c "import $module; print('$module OK')" 2>/dev/null; then
            print_success "$module ✓"
        else
            print_error "$module non disponible!"
        fi
    done
    
    # Tester l'application
    if python3 -c "import sys; sys.path.append('.'); from ultimate_phishing_gui import UltimatePhishingGUI; print('Application OK')" 2>/dev/null; then
        print_success "Application principale ✓"
    else
        print_error "Erreur dans l'application principale!"
    fi
}

# Affichage des instructions finales
show_final_instructions() {
    echo -e "${GREEN}"
    echo "=========================================="
    echo "🎣 INSTALLATION TERMINÉE AVEC SUCCÈS! 🎣"
    echo "=========================================="
    echo -e "${NC}"
    
    print_status "Pour lancer l'application:"
    echo "  python3 ultimate_phishing_gui.py"
    echo "  ou"
    echo "  python3 run.py"
    echo ""
    
    print_status "Instructions importantes:"
    case $OS in
        "debian"|"ubuntu")
            echo "  - Certaines attaques WiFi nécessitent sudo"
            echo "  - Redémarrez votre session pour les permissions WiFi"
            ;;
        "macos")
            echo "  - Certaines attaques WiFi nécessitent sudo"
            echo "  - Autorisez l'accès aux périphériques réseau"
            ;;
        "windows")
            echo "  - Exécutez en tant qu'administrateur pour les attaques WiFi"
            echo "  - Installez les outils manquants si nécessaire"
            ;;
    esac
    
    echo ""
    print_warning "⚠️  UTILISEZ CET OUTIL UNIQUEMENT À DES FINS ÉDUCATIVES ET LÉGALES! ⚠️"
    echo ""
}

# Fonction principale
main() {
    print_header
    
    # Vérifier si on est root (non recommandé)
    if [ "$EUID" -eq 0 ]; then
        print_warning "Exécution en tant que root détectée!"
        print_status "Il est recommandé d'exécuter en tant qu'utilisateur normal"
    fi
    
    # Détection du système
    detect_os
    
    # Vérification des prérequis
    check_prerequisites
    
    # Installation des dépendances système
    install_system_dependencies
    
    # Installation des dépendances Python
    install_python_dependencies
    
    # Vérification des outils de sécurité
    check_security_tools
    
    # Création des dossiers
    create_directories
    
    # Configuration des permissions
    setup_permissions
    
    # Test de l'installation
    test_installation
    
    # Instructions finales
    show_final_instructions
}

# Gestion des erreurs
trap 'print_error "Installation interrompue!"; exit 1' INT TERM

# Exécution du script
main "$@" 