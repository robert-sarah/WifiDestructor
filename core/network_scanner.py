#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌐 NETWORK SCANNER - Module de scan réseau avancé
Nmap + Masscan + Advanced Reconnaissance
"""

import os
import subprocess
import threading
import time
import json
import socket
import nmap
from datetime import datetime

class NetworkScanner:
    def __init__(self):
        self.scan_results = []
        self.active_scans = []
        
    def quick_scan(self, target):
        """Scan rapide avec nmap"""
        print(f"🔍 Quick scan: {target}")
        
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments='-sS -sV -O --top-ports 100')
            
            results = {
                'target': target,
                'scan_type': 'quick',
                'hosts': nm.all_hosts(),
                'services': {},
                'timestamp': datetime.now().isoformat()
            }
            
            for host in nm.all_hosts():
                results['services'][host] = nm[host].all_tcp()
                
            self.scan_results.append(results)
            return results
            
        except Exception as e:
            print(f"❌ Erreur quick scan: {e}")
            return None
            
    def full_scan(self, target):
        """Scan complet avec tous les ports"""
        print(f"🔍 Full scan: {target}")
        
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments='-sS -sV -O -p- --script=vuln')
            
            results = {
                'target': target,
                'scan_type': 'full',
                'hosts': nm.all_hosts(),
                'services': {},
                'vulnerabilities': [],
                'timestamp': datetime.now().isoformat()
            }
            
            for host in nm.all_hosts():
                results['services'][host] = nm[host].all_tcp()
                
                # Extraire les vulnérabilités
                for port in nm[host].all_tcp():
                    if 'script' in nm[host]['tcp'][port]:
                        for script_name, output in nm[host]['tcp'][port]['script'].items():
                            if 'VULNERABLE' in output:
                                results['vulnerabilities'].append({
                                    'host': host,
                                    'port': port,
                                    'script': script_name,
                                    'output': output
                                })
                                
            self.scan_results.append(results)
            return results
            
        except Exception as e:
            print(f"❌ Erreur full scan: {e}")
            return None
            
    def masscan_scan(self, target, ports="1-65535"):
        """Scan rapide avec masscan"""
        print(f"⚡ Masscan: {target}")
        
        try:
            cmd = [
                'masscan',
                target,
                '-p', ports,
                '--rate', '10000',
                '-oJ', 'masscan_output.json'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                with open('masscan_output.json', 'r') as f:
                    masscan_data = json.load(f)
                    
                results = {
                    'target': target,
                    'scan_type': 'masscan',
                    'ports_found': masscan_data,
                    'timestamp': datetime.now().isoformat()
                }
                
                self.scan_results.append(results)
                return results
                
        except Exception as e:
            print(f"❌ Erreur masscan: {e}")
            return None
            
    def service_enumeration(self, target, port):
        """Énumération des services"""
        print(f"🔍 Service enum: {target}:{port}")
        
        try:
            # Scripts nmap pour énumération
            scripts = [
                'banner',
                'http-title',
                'http-headers',
                'ssl-cert',
                'ftp-anon',
                'ssh-hostkey',
                'smb-enum-shares'
            ]
            
            nm = nmap.PortScanner()
            script_args = ','.join(scripts)
            nm.scan(target, arguments=f'-sV -p {port} --script={script_args}')
            
            results = {
                'target': target,
                'port': port,
                'scan_type': 'service_enum',
                'services': {},
                'timestamp': datetime.now().isoformat()
            }
            
            for host in nm.all_hosts():
                if port in nm[host]['tcp']:
                    service_info = nm[host]['tcp'][port]
                    results['services'][host] = {
                        'name': service_info.get('name', 'unknown'),
                        'product': service_info.get('product', ''),
                        'version': service_info.get('version', ''),
                        'extrainfo': service_info.get('extrainfo', ''),
                        'scripts': service_info.get('script', {})
                    }
                    
            self.scan_results.append(results)
            return results
            
        except Exception as e:
            print(f"❌ Erreur service enum: {e}")
            return None
            
    def web_enumeration(self, target):
        """Énumération web avancée"""
        print(f"🌐 Web enum: {target}")
        
        try:
            # Utiliser dirb/gobuster pour énumération web
            common_paths = [
                '/admin', '/login', '/wp-admin', '/phpmyadmin',
                '/config', '/backup', '/.git', '/.env',
                '/robots.txt', '/sitemap.xml', '/api'
            ]
            
            results = {
                'target': target,
                'scan_type': 'web_enum',
                'found_paths': [],
                'timestamp': datetime.now().isoformat()
            }
            
            # Test avec curl
            for path in common_paths:
                try:
                    cmd = ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', f'http://{target}{path}']
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    
                    if result.stdout.strip() == '200':
                        results['found_paths'].append({
                            'path': path,
                            'status': 200
                        })
                        
                except Exception:
                    pass
                    
            self.scan_results.append(results)
            return results
            
        except Exception as e:
            print(f"❌ Erreur web enum: {e}")
            return None
            
    def dns_enumeration(self, domain):
        """Énumération DNS"""
        print(f"🔍 DNS enum: {domain}")
        
        try:
            results = {
                'domain': domain,
                'scan_type': 'dns_enum',
                'records': {},
                'timestamp': datetime.now().isoformat()
            }
            
            # Types de records DNS à vérifier
            record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
            
            for record_type in record_types:
                try:
                    cmd = ['nslookup', '-type=' + record_type, domain]
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        results['records'][record_type] = result.stdout
                        
                except Exception:
                    pass
                    
            self.scan_results.append(results)
            return results
            
        except Exception as e:
            print(f"❌ Erreur DNS enum: {e}")
            return None
            
    def subdomain_enumeration(self, domain):
        """Énumération de sous-domaines"""
        print(f"🔍 Subdomain enum: {domain}")
        
        try:
            results = {
                'domain': domain,
                'scan_type': 'subdomain_enum',
                'subdomains': [],
                'timestamp': datetime.now().isoformat()
            }
            
            # Liste de sous-domaines communs
            common_subdomains = [
                'www', 'mail', 'ftp', 'admin', 'blog', 'dev', 'test',
                'api', 'cdn', 'static', 'img', 'media', 'support'
            ]
            
            for subdomain in common_subdomains:
                full_domain = f"{subdomain}.{domain}"
                try:
                    ip = socket.gethostbyname(full_domain)
                    results['subdomains'].append({
                        'subdomain': full_domain,
                        'ip': ip
                    })
                except socket.gaierror:
                    pass
                    
            self.scan_results.append(results)
            return results
            
        except Exception as e:
            print(f"❌ Erreur subdomain enum: {e}")
            return None
            
    def vulnerability_scan(self, target):
        """Scan de vulnérabilités"""
        print(f"🔍 Vuln scan: {target}")
        
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments='--script=vuln -sV')
            
            results = {
                'target': target,
                'scan_type': 'vulnerability_scan',
                'vulnerabilities': [],
                'timestamp': datetime.now().isoformat()
            }
            
            for host in nm.all_hosts():
                for port in nm[host].all_tcp():
                    if 'script' in nm[host]['tcp'][port]:
                        for script_name, output in nm[host]['tcp'][port]['script'].items():
                            if 'VULNERABLE' in output or 'CVE' in output:
                                results['vulnerabilities'].append({
                                    'host': host,
                                    'port': port,
                                    'script': script_name,
                                    'output': output
                                })
                                
            self.scan_results.append(results)
            return results
            
        except Exception as e:
            print(f"❌ Erreur vuln scan: {e}")
            return None
            
    def get_scan_results(self):
        """Retourne les résultats de scan"""
        return self.scan_results
        
    def export_scan_data(self, filename):
        """Exporte les données de scan"""
        with open(filename, 'w') as f:
            json.dump(self.scan_results, f, indent=2)
            
        print(f"📤 Données de scan exportées: {filename}")
        
    def clear_results(self):
        """Nettoie les résultats"""
        self.scan_results = [] 