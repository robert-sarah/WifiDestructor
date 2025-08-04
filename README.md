# 🎣 Phishing Tool Pro v2.0 - BlackEye + CamPhish Enhanced

## 🚀 Fonctionnalités Avancées

### ✨ Templates BlackEye
- **16 sites populaires** : Facebook, Google, Instagram, Netflix, PayPal, Steam, Twitter, WhatsApp, Amazon, Apple ID, Microsoft, LinkedIn, GitHub, Dropbox, Spotify, Discord
- **Interface réaliste** : Templates identiques aux sites originaux
- **Catégorisation** : Social, Tech, Finance, Gaming, Entertainment, etc.

### 📸 CamPhish - Capture Webcam
- **Capture automatique** : Photo de la victime via webcam
- **Stockage sécurisé** : Images sauvegardées dans `/captures/`
- **Timing intelligent** : Capture après 3 secondes d'accès

### 🌍 Géolocalisation Avancée
- **Localisation précise** : Ville, pays, coordonnées GPS
- **Informations réseau** : IP, ISP, Timezone
- **Carte interactive** : Visualisation des victimes

### 💻 Détection Système
- **Navigateur** : Chrome, Firefox, Safari, Edge
- **Système d'exploitation** : Windows, macOS, Linux, Android, iOS
- **Appareil** : Desktop, Mobile, Tablet
- **Résolution écran** : Informations détaillées

### 🎯 Interface Moderne
- **Design professionnel** : Interface sombre et moderne
- **Notifications temps réel** : Alertes instantanées
- **Logs détaillés** : Historique complet des activités
- **Export avancé** : JSON, CSV, Excel

## 🛠️ Installation

### Prérequis
- Python 3.7+
- pip
- git

### Installation Automatique
```bash
# Cloner le repository
git clone https://github.com/votre-repo/phishing-tool-pro.git
cd phishing-tool-pro

# Installation automatique
chmod +x install.sh
./install.sh
```

### Installation Manuelle
```bash
# Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## 🚀 Utilisation

### Lancement
```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Lancer l'outil
python3 phishing_tool.py
```

### Interface Utilisateur

#### 1. **Onglet Templates**
- Sélectionnez un template (Facebook, Google, etc.)
- Aperçu du site choisi
- Informations sur le template

#### 2. **Onglet Serveur**
- Démarrage/arrêt du serveur
- Configuration host/port
- URL générée automatiquement
- QR Code pour accès mobile

#### 3. **Onglet Credentials**
- Liste des victimes capturées
- Informations détaillées (IP, navigateur, OS, localisation)
- Export des données
- Nettoyage des données

#### 4. **Onglet Settings**
- Configuration avancée
- Auto-ouverture navigateur
- Paramètres de sécurité

## 📊 Fonctionnalités Avancées

### 🎯 Capture Intelligente
```
✅ Email/Mot de passe
✅ Adresse IP
✅ Géolocalisation
✅ Navigateur/OS
✅ Capture webcam
✅ Informations système
✅ Timestamp précis
```

### 🌐 Templates Disponibles
| Site | Catégorie | Statut |
|------|-----------|--------|
| Facebook | Social | ✅ |
| Google | Search | ✅ |
| Instagram | Social | ✅ |
| Netflix | Entertainment | ✅ |
| PayPal | Finance | ✅ |
| Steam | Gaming | ✅ |
| Twitter | Social | ✅ |
| WhatsApp | Messaging | ✅ |
| Amazon | Shopping | ✅ |
| Apple ID | Tech | ✅ |
| Microsoft | Tech | ✅ |
| LinkedIn | Professional | ✅ |
| GitHub | Tech | ✅ |
| Dropbox | Storage | ✅ |
| Spotify | Entertainment | ✅ |
| Discord | Gaming | ✅ |

## 🔧 Configuration

### Variables d'Environnement
```bash
export PHISHING_HOST=0.0.0.0
export PHISHING_PORT=8080
export PHISHING_DEBUG=false
```

### Fichiers de Configuration
- `templates/` : Templates HTML
- `captures/` : Images webcam
- `logs/` : Fichiers de logs
- `exports/` : Données exportées

## 📈 Statistiques

### Métriques Collectées
- **Victimes capturées** : Nombre total
- **Taux de succès** : Pourcentage de victimes
- **Géolocalisation** : Répartition géographique
- **Navigateurs** : Types de navigateurs utilisés
- **Systèmes** : OS des victimes

### Export des Données
```bash
# Export JSON
python3 -c "import json; print(json.dumps(credentials, indent=2))"

# Export CSV
python3 -c "import csv; ..."

# Export Excel
python3 -c "import pandas; ..."
```

## 🛡️ Sécurité

### ⚠️ Avertissements
- **Usage éthique uniquement** : Tests de sécurité autorisés
- **Consentement requis** : Informer les participants
- **Légalité** : Respecter les lois locales
- **Responsabilité** : L'utilisateur est responsable

### 🔒 Bonnes Pratiques
- Utiliser uniquement pour des tests autorisés
- Documenter les tests effectués
- Supprimer les données après usage
- Respecter la vie privée

## 🐛 Dépannage

### Problèmes Courants

#### Serveur ne démarre pas
```bash
# Vérifier le port
netstat -tulpn | grep :8080

# Changer le port
python3 phishing_tool.py --port 8081
```

#### Webcam non détectée
```bash
# Vérifier les permissions
ls -la /dev/video*

# Installer opencv
pip install opencv-python
```

#### Dépendances manquantes
```bash
# Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall
```

## 📝 Changelog

### v2.0 - BlackEye + CamPhish Enhanced
- ✅ Ajout de 8 nouveaux templates BlackEye
- ✅ Intégration CamPhish (capture webcam)
- ✅ Géolocalisation avancée
- ✅ Détection navigateur/OS
- ✅ Interface moderne
- ✅ Notifications temps réel
- ✅ Export avancé

### v1.0 - Version Initiale
- ✅ Templates de base
- ✅ Interface graphique
- ✅ Capture de credentials
- ✅ Serveur Flask

## 🤝 Contribution

### Comment Contribuer
1. Fork le projet
2. Créer une branche feature
3. Commiter les changements
4. Pousser vers la branche
5. Créer une Pull Request

### Standards de Code
- PEP 8 pour Python
- Commentaires en français
- Documentation complète
- Tests unitaires

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## ⚖️ Avertissement Légal

**ATTENTION** : Cet outil est destiné uniquement à des fins éducatives et de test de sécurité autorisés. L'utilisation de cet outil pour des activités malveillantes est strictement interdite. Les développeurs ne sont pas responsables de l'utilisation abusive de cet outil.

## 📞 Support

- **Issues** : GitHub Issues
- **Discussions** : GitHub Discussions
- **Email** : support@phishing-tool.com

---

**🎯 Phishing Tool Pro v2.0 - Plus fort et plus rapide que jamais !** 