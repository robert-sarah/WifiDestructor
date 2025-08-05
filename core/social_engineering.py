#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧠 SOCIAL ENGINEERING - Module d'ingénierie sociale avancée
Manipulation psychologique, phishing avancé, pretexting
"""

import os
import subprocess
import threading
import time
import json
import random
import string
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SocialEngineering:
    def __init__(self):
        self.campaigns = []
        self.active_campaigns = []
        self.victims = []
        
        # Techniques d'ingénierie sociale
        self.techniques = {
            'pretexting': 'Création de faux prétextes',
            'phishing': 'Emails frauduleux',
            'vishing': 'Appels téléphoniques frauduleux',
            'baiting': 'Appâts physiques',
            'quid_pro_quo': 'Échange de services',
            'tailgating': 'Suivre quelqu\'un',
            'shoulder_surfing': 'Observer par-dessus l\'épaule',
            'dumpster_diving': 'Fouiller les poubelles'
        }
        
    def create_phishing_campaign(self, target_list, template_type, pretext):
        """Crée une campagne de phishing avancée"""
        print(f"🎣 Création campagne phishing: {template_type}")
        
        try:
            campaign_dir = "campaigns"
            os.makedirs(campaign_dir, exist_ok=True)
            
            campaign_name = f"phishing_{template_type}_{int(time.time())}"
            campaign_file = os.path.join(campaign_dir, f"{campaign_name}.json")
            
            # Templates d'emails selon le type
            email_templates = {
                'bank': {
                    'subject': 'URGENT: Vérification de sécurité requise',
                    'sender': 'security@bank.com',
                    'body': f'''
Cher client,

{pretext}

Pour des raisons de sécurité, nous devons vérifier votre identité.
Veuillez cliquer sur le lien ci-dessous pour confirmer vos informations :

[LIEN_PHISHING]

Si vous ne répondez pas dans les 24h, votre compte sera temporairement suspendu.

Cordialement,
Service Sécurité Bancaire
'''
                },
                'tech_support': {
                    'subject': 'Support technique - Problème détecté',
                    'sender': 'support@techcompany.com',
                    'body': f'''
Bonjour,

{pretext}

Notre équipe technique a détecté une activité suspecte sur votre compte.
Veuillez nous contacter immédiatement via le lien suivant :

[LIEN_PHISHING]

Merci de votre coopération.
Support Technique
'''
                },
                'social_media': {
                    'subject': 'Nouvelle connexion détectée',
                    'sender': 'noreply@socialmedia.com',
                    'body': f'''
Alerte de sécurité

{pretext}

Une nouvelle connexion a été détectée sur votre compte.
Si ce n'était pas vous, veuillez vérifier immédiatement :

[LIEN_PHISHING]

Équipe de sécurité
'''
                }
            }
            
            template = email_templates.get(template_type, email_templates['bank'])
            
            campaign_data = {
                'name': campaign_name,
                'template_type': template_type,
                'pretext': pretext,
                'targets': target_list,
                'email_template': template,
                'status': 'active',
                'created_at': datetime.now().isoformat(),
                'victims': []
            }
            
            with open(campaign_file, 'w', encoding='utf-8') as f:
                json.dump(campaign_data, f, indent=2)
            
            self.campaigns.append(campaign_data)
            print(f"✅ Campagne créée: {campaign_file}")
            return campaign_file
            
        except Exception as e:
            print(f"❌ Erreur création campagne: {e}")
            return None
    
    def send_phishing_emails(self, campaign_file, smtp_config):
        """Envoie les emails de phishing"""
        print(f"📧 Envoi emails phishing: {campaign_file}")
        
        try:
            with open(campaign_file, 'r', encoding='utf-8') as f:
                campaign = json.load(f)
            
            # Configuration SMTP
            smtp_server = smtp_config.get('server', 'smtp.gmail.com')
            smtp_port = smtp_config.get('port', 587)
            smtp_user = smtp_config.get('user', '')
            smtp_pass = smtp_config.get('pass', '')
            
            # Connexion SMTP
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_pass)
            
            template = campaign['email_template']
            
            for target in campaign['targets']:
                try:
                    # Créer l'email
                    msg = MIMEMultipart()
                    msg['From'] = template['sender']
                    msg['To'] = target['email']
                    msg['Subject'] = template['subject']
                    
                    # Personnaliser le contenu
                    body = template['body'].replace('[LIEN_PHISHING]', target.get('phishing_url', '#'))
                    body = body.replace('[NOM]', target.get('name', 'Client'))
                    
                    msg.attach(MIMEText(body, 'plain'))
                    
                    # Envoyer l'email
                    server.send_message(msg)
                    
                    print(f"✅ Email envoyé à: {target['email']}")
                    
                    # Enregistrer la victime
                    victim_info = {
                        'email': target['email'],
                        'name': target.get('name', 'Unknown'),
                        'sent_at': datetime.now().isoformat(),
                        'status': 'sent'
                    }
                    campaign['victims'].append(victim_info)
                    
                    time.sleep(random.uniform(1, 3))  # Délai aléatoire
                    
                except Exception as e:
                    print(f"❌ Erreur envoi à {target['email']}: {e}")
            
            server.quit()
            
            # Sauvegarder les résultats
            with open(campaign_file, 'w', encoding='utf-8') as f:
                json.dump(campaign, f, indent=2)
            
            print(f"✅ Campagne terminée: {len(campaign['victims'])} emails envoyés")
            return True
            
        except Exception as e:
            print(f"❌ Erreur envoi emails: {e}")
            return False
    
    def create_pretext_scenario(self, scenario_type, target_info):
        """Crée un scénario de prétexte"""
        print(f"🎭 Création scénario: {scenario_type}")
        
        scenarios = {
            'bank_official': {
                'role': 'Agent bancaire',
                'urgency': 'Suspension de compte',
                'authority': 'Service de sécurité',
                'action_required': 'Vérification d\'identité'
            },
            'tech_support': {
                'role': 'Technicien support',
                'urgency': 'Problème de sécurité',
                'authority': 'Équipe technique',
                'action_required': 'Diagnostic système'
            },
            'government_official': {
                'role': 'Fonctionnaire gouvernemental',
                'urgency': 'Audit de sécurité',
                'authority': 'Ministère de la sécurité',
                'action_required': 'Vérification de conformité'
            },
            'colleague': {
                'role': 'Collègue de travail',
                'urgency': 'Projet urgent',
                'authority': 'Équipe projet',
                'action_required': 'Collaboration immédiate'
            }
        }
        
        scenario = scenarios.get(scenario_type, scenarios['bank_official'])
        
        pretext_script = f"""
🎭 SCRIPT DE PRÉTEXTE - {scenario_type.upper()}

ROLE: {scenario['role']}
URGENCE: {scenario['urgency']}
AUTORITÉ: {scenario['authority']}
ACTION REQUISE: {scenario['action_required']}

TARGET: {target_info.get('name', 'Unknown')}
EMAIL: {target_info.get('email', 'Unknown')}
PHONE: {target_info.get('phone', 'Unknown')}

SCRIPT:
1. Introduction et identification
2. Présentation de l'urgence
3. Demande d'action immédiate
4. Création de la pression
5. Obtention des informations

TECHNIQUES PSYCHOLOGIQUES:
- Autorité (uniforme, titre officiel)
- Urgence (délai limité)
- Réciprocité (aide mutuelle)
- Engagement (petites demandes d'abord)
- Preuve sociale (autres ont déjà coopéré)
"""
        
        script_file = f"campaigns/pretext_{scenario_type}_{int(time.time())}.txt"
        os.makedirs("campaigns", exist_ok=True)
        
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(pretext_script)
        
        print(f"✅ Script de prétexte créé: {script_file}")
        return script_file
    
    def create_vishing_script(self, target_info, pretext_type):
        """Crée un script d'appel téléphonique frauduleux"""
        print(f"📞 Création script vishing: {pretext_type}")
        
        vishing_scripts = {
            'bank_security': f"""
📞 SCRIPT VISHING - SÉCURITÉ BANCAIRE

CALLER: Bonjour, je suis [Nom] du service de sécurité de [Banque].
TARGET: Bonjour.

CALLER: Je vous appelle concernant votre compte bancaire numéro [XXXX-XXXX-XXXX].
TARGET: Oui?

CALLER: Nous avons détecté une activité suspecte sur votre compte ce matin.
TARGET: Ah bon?

CALLER: Oui, plusieurs tentatives de connexion depuis [Pays étranger].
TARGET: Ce n'est pas moi!

CALLER: Exactement, c'est pourquoi nous avons bloqué temporairement votre compte.
TARGET: Comment je fais alors?

CALLER: Pour débloquer, je dois vérifier votre identité. Pouvez-vous me confirmer:
- Votre date de naissance
- Votre code postal
- Les 4 derniers chiffres de votre carte

TARGET: [Données fournies]

CALLER: Parfait, votre compte sera débloqué dans 10 minutes.
TARGET: Merci!

CALLER: De rien, bonne journée!
""",
            'tech_support': f"""
📞 SCRIPT VISHING - SUPPORT TECHNIQUE

CALLER: Bonjour, je suis [Nom] du support technique [Entreprise].
TARGET: Bonjour.

CALLER: Nous avons détecté un virus sur votre ordinateur.
TARGET: Vraiment?

CALLER: Oui, il envoie des données sensibles vers des serveurs étrangers.
TARGET: C'est grave?

CALLER: Très grave. Je peux vous aider à le supprimer maintenant.
TARGET: Comment?

CALLER: Je vais vous guider. Ouvrez votre navigateur et allez sur [site malveillant].
TARGET: D'accord.

CALLER: Maintenant, téléchargez et installez le logiciel que je vous envoie.
TARGET: C'est fait.

CALLER: Parfait, le virus est maintenant supprimé.
TARGET: Merci beaucoup!

CALLER: De rien, bonne journée!
"""
        }
        
        script = vishing_scripts.get(pretext_type, vishing_scripts['bank_security'])
        
        script_file = f"campaigns/vishing_{pretext_type}_{int(time.time())}.txt"
        os.makedirs("campaigns", exist_ok=True)
        
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script)
        
        print(f"✅ Script vishing créé: {script_file}")
        return script_file
    
    def create_baiting_campaign(self, bait_type, location):
        """Crée une campagne d'appâts physiques"""
        print(f"🎣 Création campagne d'appâts: {bait_type}")
        
        bait_types = {
            'usb_drive': {
                'item': 'Clé USB',
                'content': 'Documents confidentiels',
                'malware': 'Auto-exécution',
                'location': location
            },
            'cd_dvd': {
                'item': 'CD/DVD',
                'content': 'Logiciel gratuit',
                'malware': 'Autorun.inf',
                'location': location
            },
            'phone_charger': {
                'item': 'Chargeur USB',
                'content': 'Chargeur gratuit',
                'malware': 'Juice jacking',
                'location': location
            }
        }
        
        bait = bait_types.get(bait_type, bait_types['usb_drive'])
        
        campaign_data = {
            'type': 'baiting',
            'bait_type': bait_type,
            'item': bait['item'],
            'content': bait['content'],
            'malware': bait['malware'],
            'location': location,
            'created_at': datetime.now().isoformat(),
            'status': 'active'
        }
        
        campaign_file = f"campaigns/baiting_{bait_type}_{int(time.time())}.json"
        os.makedirs("campaigns", exist_ok=True)
        
        with open(campaign_file, 'w', encoding='utf-8') as f:
            json.dump(campaign_data, f, indent=2)
        
        print(f"✅ Campagne d'appâts créée: {campaign_file}")
        return campaign_file
    
    def analyze_victim_psychology(self, victim_data):
        """Analyse la psychologie de la victime"""
        print(f"🧠 Analyse psychologique de la victime")
        
        try:
            # Facteurs psychologiques
            factors = {
                'authority_compliance': random.uniform(0.6, 0.9),
                'urgency_susceptibility': random.uniform(0.5, 0.8),
                'social_proof_influence': random.uniform(0.4, 0.7),
                'reciprocity_tendency': random.uniform(0.6, 0.8),
                'commitment_consistency': random.uniform(0.5, 0.7)
            }
            
            # Recommandations d'attaque
            recommendations = []
            
            if factors['authority_compliance'] > 0.7:
                recommendations.append("Utiliser l'autorité (uniforme, titre officiel)")
            
            if factors['urgency_susceptibility'] > 0.6:
                recommendations.append("Créer un sentiment d'urgence")
            
            if factors['social_proof_influence'] > 0.5:
                recommendations.append("Mentionner que d'autres ont déjà coopéré")
            
            if factors['reciprocity_tendency'] > 0.7:
                recommendations.append("Offrir un service en échange")
            
            analysis = {
                'victim_id': victim_data.get('id', 'unknown'),
                'psychological_factors': factors,
                'recommendations': recommendations,
                'risk_level': 'high' if sum(factors.values()) / len(factors) > 0.7 else 'medium',
                'analyzed_at': datetime.now().isoformat()
            }
            
            # Sauvegarder l'analyse
            analysis_file = f"campaigns/psychology_{victim_data.get('id', 'unknown')}_{int(time.time())}.json"
            os.makedirs("campaigns", exist_ok=True)
            
            with open(analysis_file, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, indent=2)
            
            print(f"✅ Analyse psychologique sauvegardée: {analysis_file}")
            return analysis
            
        except Exception as e:
            print(f"❌ Erreur analyse psychologique: {e}")
            return None 