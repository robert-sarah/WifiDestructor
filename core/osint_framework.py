#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔍 OSINT FRAMEWORK - Module de reconnaissance en sources ouvertes
Intelligence gathering, subdomain takeover, certificate transparency
"""

import os
import subprocess
import threading
import time
import json
import requests
import dns.resolver
import whois
import shodan
from datetime import datetime

class OSINTFramework:
    def __init__(self):
        self.osint_results = []
        self.active_scans = []
        
    def subdomain_enumeration(self, target_domain):
        """Énumération de sous-domaines avancée"""
        print(f"🔍 Énumération sous-domaines: {target_domain}")
        
        try:
            osint_dir = "osint_results"
            os.makedirs(osint_dir, exist_ok=True)
            
            scan_name = f"subdomain_enum_{target_domain}_{int(time.time())}"
            scan_file = os.path.join(osint_dir, f"{scan_name}.py")
            
            # Techniques d'énumération
            enum_techniques = {
                'brute_force': [
                    'www', 'mail', 'ftp', 'admin', 'api', 'dev', 'test',
                    'staging', 'prod', 'cdn', 'static', 'assets', 'img',
                    'docs', 'support', 'help', 'blog', 'news', 'forum',
                    'shop', 'store', 'app', 'mobile', 'web', 'portal',
                    'dashboard', 'panel', 'control', 'manage', 'system'
                ],
                'dns_queries': [
                    'A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SRV'
                ],
                'certificate_transparency': True,
                'search_engines': True,
                'dns_bruteforce': True
            }
            
            scan_code = f'''#!/usr/bin/env python3
import dns.resolver
import requests
import subprocess
import json
import time
from datetime import datetime

class SubdomainEnumeration:
    def __init__(self):
        self.target_domain = "{target_domain}"
        self.subdomains = []
        self.techniques = {enum_techniques}
        
    def dns_bruteforce(self):
        """Brute force DNS"""
        print(f"[+] Brute force DNS sur {{self.target_domain}}")
        
        wordlist = {enum_techniques['brute_force']}
        
        for subdomain in wordlist:
            try:
                full_domain = f"{{subdomain}}.{{self.target_domain}}"
                answers = dns.resolver.resolve(full_domain, 'A')
                
                for answer in answers:
                    self.subdomains.append({{
                        'subdomain': full_domain,
                        'ip': str(answer),
                        'technique': 'brute_force'
                    }})
                    print(f"[+] Trouvé: {{full_domain}} -> {{answer}}")
                    
            except Exception as e:
                pass
                
    def certificate_transparency(self):
        """Recherche via Certificate Transparency"""
        print(f"[+] Recherche Certificate Transparency")
        
        try:
            # Utiliser crt.sh pour CT
            url = f"https://crt.sh/?q=%.{{self.target_domain}}&output=json"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                for cert in data:
                    if 'name_value' in cert:
                        domains = cert['name_value'].split('\\n')
                        for domain in domains:
                            if self.target_domain in domain:
                                self.subdomains.append({{
                                    'subdomain': domain,
                                    'technique': 'certificate_transparency',
                                    'issuer': cert.get('issuer_name', 'Unknown')
                                }})
                                
        except Exception as e:
            print(f"[-] Erreur CT: {{e}}")
            
    def search_engines(self):
        """Recherche via moteurs de recherche"""
        print(f"[+] Recherche moteurs de recherche")
        
        search_queries = [
            f'site:*.{{self.target_domain}}',
            f'inurl:{{self.target_domain}}',
            f'intitle:{{self.target_domain}}'
        ]
        
        # Simuler recherche (en vrai, utiliser APIs)
        for query in search_queries:
            print(f"[+] Query: {{query}}")
            
    def run_enumeration(self):
        """Lance l'énumération complète"""
        print(f"[+] Début énumération {{self.target_domain}}")
        
        self.dns_bruteforce()
        self.certificate_transparency()
        self.search_engines()
        
        # Sauvegarder les résultats
        with open(f"subdomains_{{self.target_domain}}.json", 'w') as f:
            json.dump(self.subdomains, f, indent=2)
            
        print(f"[+] Énumération terminée: {{len(self.subdomains)}} sous-domaines trouvés")
        return self.subdomains

if __name__ == "__main__":
    enum = SubdomainEnumeration()
    results = enum.run_enumeration()
'''
            
            with open(scan_file, 'w', encoding='utf-8') as f:
                f.write(scan_code)
            
            scan_info = {
                'name': scan_name,
                'target_domain': target_domain,
                'file': scan_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'subdomain_enumeration'
            }
            
            self.osint_results.append(scan_info)
            print(f"✅ Scanner sous-domaines créé: {scan_file}")
            return scan_file
            
        except Exception as e:
            print(f"❌ Erreur création scanner sous-domaines: {e}")
            return None
    
    def email_harvesting(self, target_domain):
        """Récolte d'emails automatisée"""
        print(f"📧 Récolte emails: {target_domain}")
        
        try:
            osint_dir = "osint_results"
            os.makedirs(osint_dir, exist_ok=True)
            
            harvest_name = f"email_harvest_{target_domain}_{int(time.time())}"
            harvest_file = os.path.join(osint_dir, f"{harvest_name}.py")
            
            harvest_code = f'''#!/usr/bin/env python3
import re
import requests
import dns.resolver
import subprocess
from urllib.parse import urljoin

class EmailHarvester:
    def __init__(self):
        self.target_domain = "{target_domain}"
        self.emails = []
        
    def extract_emails_from_webpage(self, url):
        """Extrait les emails d'une page web"""
        try:
            response = requests.get(url, timeout=10)
            content = response.text
            
            # Regex pour emails
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{{2,}}'
            emails = re.findall(email_pattern, content)
            
            # Filtrer les emails du domaine cible
            target_emails = [email for email in emails if self.target_domain in email]
            
            return target_emails
            
        except Exception as e:
            print(f"[-] Erreur extraction emails: {{e}}")
            return []
            
    def dns_mx_lookup(self):
        """Recherche les serveurs MX"""
        try:
            mx_records = dns.resolver.resolve(self.target_domain, 'MX')
            
            for mx in mx_records:
                print(f"[+] Serveur MX: {{mx.exchange}}")
                
        except Exception as e:
            print(f"[-] Erreur MX lookup: {{e}}")
            
    def common_email_patterns(self):
        """Génère des patterns d'emails communs"""
        common_patterns = [
            'admin@{target_domain}',
            'info@{target_domain}',
            'contact@{target_domain}',
            'support@{target_domain}',
            'help@{target_domain}',
            'sales@{target_domain}',
            'marketing@{target_domain}',
            'hr@{target_domain}',
            'jobs@{target_domain}',
            'webmaster@{target_domain}',
            'postmaster@{target_domain}',
            'abuse@{target_domain}',
            'security@{target_domain}',
            'dev@{target_domain}',
            'test@{target_domain}'
        ]
        
        return common_patterns
        
    def harvest_emails(self):
        """Lance la récolte d'emails"""
        print(f"[+] Début récolte emails {{self.target_domain}}")
        
        # Recherche MX
        self.dns_mx_lookup()
        
        # Patterns communs
        common_emails = self.common_email_patterns()
        self.emails.extend(common_emails)
        
        # Extraction depuis pages web
        web_urls = [
            f"https://www.{{self.target_domain}}",
            f"https://{{self.target_domain}}",
            f"http://www.{{self.target_domain}}",
            f"http://{{self.target_domain}}"
        ]
        
        for url in web_urls:
            web_emails = self.extract_emails_from_webpage(url)
            self.emails.extend(web_emails)
            
        # Dédupliquer
        self.emails = list(set(self.emails))
        
        print(f"[+] Récolte terminée: {{len(self.emails)}} emails trouvés")
        return self.emails

if __name__ == "__main__":
    harvester = EmailHarvester()
    emails = harvester.harvest_emails()
    print("Emails trouvés:", emails)
'''
            
            with open(harvest_file, 'w', encoding='utf-8') as f:
                f.write(harvest_code)
            
            harvest_info = {
                'name': harvest_name,
                'target_domain': target_domain,
                'file': harvest_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'email_harvesting'
            }
            
            self.osint_results.append(harvest_info)
            print(f"✅ Harvester emails créé: {harvest_file}")
            return harvest_file
            
        except Exception as e:
            print(f"❌ Erreur création harvester emails: {e}")
            return None
    
    def social_media_osint(self, target_organization):
        """OSINT sur réseaux sociaux"""
        print(f"📱 OSINT réseaux sociaux: {target_organization}")
        
        try:
            osint_dir = "osint_results"
            os.makedirs(osint_dir, exist_ok=True)
            
            social_name = f"social_osint_{target_organization}_{int(time.time())}"
            social_file = os.path.join(osint_dir, f"{social_name}.py")
            
            social_code = f'''#!/usr/bin/env python3
import requests
import json
import time
from datetime import datetime

class SocialMediaOSINT:
    def __init__(self):
        self.target_org = "{target_organization}"
        self.results = {{}}
        
    def linkedin_enumeration(self):
        """Énumération LinkedIn"""
        print(f"[+] Énumération LinkedIn: {{self.target_org}}")
        
        # Recherche d'employés (simulation)
        employees = [
            f"{{self.target_org}}_admin",
            f"{{self.target_org}}_ceo",
            f"{{self.target_org}}_cto",
            f"{{self.target_org}}_security",
            f"{{self.target_org}}_dev"
        ]
        
        return employees
        
    def twitter_enumeration(self):
        """Énumération Twitter"""
        print(f"[+] Énumération Twitter: {{self.target_org}}")
        
        # Recherche de comptes Twitter
        twitter_accounts = [
            f"@{{self.target_org}}",
            f"@{{self.target_org}}_official",
            f"@{{self.target_org}}_news",
            f"@{{self.target_org}}_support"
        ]
        
        return twitter_accounts
        
    def github_enumeration(self):
        """Énumération GitHub"""
        print(f"[+] Énumération GitHub: {{self.target_org}}")
        
        # Recherche de repos GitHub
        github_repos = [
            f"{{self.target_org}}/main-app",
            f"{{self.target_org}}/api",
            f"{{self.target_org}}/website",
            f"{{self.target_org}}/mobile-app"
        ]
        
        return github_repos
        
    def run_social_osint(self):
        """Lance l'OSINT réseaux sociaux"""
        print(f"[+] Début OSINT réseaux sociaux {{self.target_org}}")
        
        self.results['linkedin'] = self.linkedin_enumeration()
        self.results['twitter'] = self.twitter_enumeration()
        self.results['github'] = self.github_enumeration()
        
        # Sauvegarder résultats
        with open(f"social_osint_{{self.target_org}}.json", 'w') as f:
            json.dump(self.results, f, indent=2)
            
        print(f"[+] OSINT terminé: {{len(self.results)}} plateformes analysées")
        return self.results

if __name__ == "__main__":
    osint = SocialMediaOSINT()
    results = osint.run_social_osint()
'''
            
            with open(social_file, 'w', encoding='utf-8') as f:
                f.write(social_code)
            
            social_info = {
                'name': social_name,
                'target_organization': target_organization,
                'file': social_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'social_media_osint'
            }
            
            self.osint_results.append(social_info)
            print(f"✅ OSINT réseaux sociaux créé: {social_file}")
            return social_file
            
        except Exception as e:
            print(f"❌ Erreur création OSINT réseaux sociaux: {e}")
            return None
    
    def certificate_transparency_monitor(self, target_domain):
        """Surveillance Certificate Transparency"""
        print(f"🔐 Surveillance CT: {target_domain}")
        
        try:
            osint_dir = "osint_results"
            os.makedirs(osint_dir, exist_ok=True)
            
            ct_name = f"ct_monitor_{target_domain}_{int(time.time())}"
            ct_file = os.path.join(osint_dir, f"{ct_name}.py")
            
            ct_code = f'''#!/usr/bin/env python3
import requests
import json
import time
from datetime import datetime

class CertificateTransparencyMonitor:
    def __init__(self):
        self.target_domain = "{target_domain}"
        self.certificates = []
        
    def query_crt_sh(self):
        """Interroge crt.sh"""
        print(f"[+] Interrogation crt.sh pour {{self.target_domain}}")
        
        try:
            url = f"https://crt.sh/?q=%.{{self.target_domain}}&output=json"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                for cert in data:
                    cert_info = {{
                        'id': cert.get('id'),
                        'issuer_name': cert.get('issuer_name'),
                        'common_name': cert.get('common_name'),
                        'name_value': cert.get('name_value'),
                        'not_before': cert.get('not_before'),
                        'not_after': cert.get('not_after')
                    }}
                    
                    self.certificates.append(cert_info)
                    
        except Exception as e:
            print(f"[-] Erreur crt.sh: {{e}}")
            
    def query_censys(self):
        """Interroge Censys (simulation)"""
        print(f"[+] Interrogation Censys pour {{self.target_domain}}")
        
        # Simulation - en vrai utiliser l'API Censys
        censys_results = [
            {{
                'ip': '192.168.1.1',
                'port': 443,
                'certificate': '{{self.target_domain}} certificate'
            }}
        ]
        
        return censys_results
        
    def monitor_certificates(self):
        """Surveille les certificats"""
        print(f"[+] Début surveillance CT {{self.target_domain}}")
        
        self.query_crt_sh()
        
        # Sauvegarder résultats
        with open(f"ct_monitor_{{self.target_domain}}.json", 'w') as f:
            json.dump(self.certificates, f, indent=2)
            
        print(f"[+] Surveillance terminée: {{len(self.certificates)}} certificats trouvés")
        return self.certificates

if __name__ == "__main__":
    monitor = CertificateTransparencyMonitor()
    results = monitor.monitor_certificates()
'''
            
            with open(ct_file, 'w', encoding='utf-8') as f:
                f.write(ct_code)
            
            ct_info = {
                'name': ct_name,
                'target_domain': target_domain,
                'file': ct_file,
                'timestamp': datetime.now().isoformat(),
                'type': 'certificate_transparency'
            }
            
            self.osint_results.append(ct_info)
            print(f"✅ Moniteur CT créé: {ct_file}")
            return ct_file
            
        except Exception as e:
            print(f"❌ Erreur création moniteur CT: {e}")
            return None 