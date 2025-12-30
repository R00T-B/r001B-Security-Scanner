#!/usr/bin/env python3
import argparse
import sys
from modules.reconnaissance import Reconnaissance
from modules.password_analysis import PasswordAnalyzer
from modules.api_tester import APITester
from modules.vulnerability import VulnerabilityScanner
from modules.report_generator import ReportGenerator
from utils.logger import setup_logger

class SocialMediaToolkit:
    def __init__(self):
        self.logger = setup_logger()
        self.recon = Reconnaissance()
        self.password_analyzer = PasswordAnalyzer()
        self.api_tester = APITester()
        self.vuln_scanner = VulnerabilityScanner()
        self.reporter = ReportGenerator()
        
    def banner(self):
        print("""
        ⚡
       / \\
      ( O )
       \\_/
        
        ╔══════════════════════════════╗
        ║         r001B SECURITY       ║
        ║  Social Media Toolkit v1.0   ║
        ╚══════════════════════════════╝
        """)
    
    def main_menu(self):
        while True:
            print("\n=== ⚡ r001B - SOSYAL MEDYA GÜVENLİK TOOLKIT ===")
            print("1. Bilgi Toplama (Reconnaissance)")
            print("2. Şifre Analizi")
            print("3. API Güvenlik Testleri")
            print("4. Zafiyet Tarama")
            print("5. Tam Tarama (All-in-One)")
            print("6. Rapor Oluştur")
            print("0. Çıkış")
            
            choice = input("\nSeçim yapın (0-6): ")
            
            if choice == "1":
                self.recon_menu()
            elif choice == "2":
                self.password_menu()
            elif choice == "3":
                self.api_menu()
            elif choice == "4":
                self.vuln_menu()
            elif choice == "5":
                self.full_scan()
            elif choice == "6":
                self.generate_report()
            elif choice == "0":
                print("⚡ r001B - Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim!")
    
    def recon_menu(self):
        print("\n=== ⚡ r001B - BİLGİ TOPLAMA ===")
        username = input("Hedef kullanıcı adı: ")
        platforms = input("Platformlar (virgülle ayır, boşsa tümü): ")
        
        if platforms:
            platforms = [p.strip() for p in platforms.split(",")]
        else:
            platforms = None
            
        results = self.recon.username_search(username, platforms)
        self.reporter.save_recon_results(results)
    
    def password_menu(self):
        print("\n=== ⚡ r001B - ŞİFRE ANALİZİ ===")
        target = input("Hedef URL/Endpoint: ")
        username = input("Kullanıcı adı: ")
        wordlist = input("Wordlist yolu (varsayılan: wordlists/rockyou.txt): ")
        
        if not wordlist:
            wordlist = "wordlists/rockyou.txt"
            
        self.password_analyzer.brute_force_test(target, username, wordlist)
    
    def api_menu(self):
        print("\n=== ⚡ r001B - API TESTLERİ ===")
        api_url = input("API URL: ")
        token = input("API Token (opsiyonel): ")
        endpoints = input("Test edilecek endpointler (virgülle ayır): ")
        
        endpoints_list = [e.strip() for e in endpoints.split(",")]
        self.api_tester.test_endpoints(api_url, endpoints_list, token)
    
    def vuln_menu(self):
        print("\n=== ⚡ r001B - ZAFİYET TARAMA ===")
        target = input("Hedef URL: ")
        self.vuln_scanner.scan_vulnerabilities(target)
    
    def full_scan(self):
        print("\n=== ⚡ r001B - TAM TARAMA BAŞLATILIYOR ===")
        username = input("Hedef kullanıcı adı: ")
        target_url = input("Hedef URL (opsiyonel): ")
        
        # Bilgi toplama
        recon_results = self.recon.username_search(username)
        
        # Şifre testleri
        if target_url:
            self.password_analyzer.quick_test(target_url, username)
        
        # API testleri
        if target_url:
            self.api_tester.quick_scan(target_url)
        
        # Zafiyet tarama
        if target_url:
            self.vuln_scanner.quick_scan(target_url)
        
        print("\n⚡ r001B - Tam tarama tamamlandı!")
    
    def generate_report(self):
        print("\n=== ⚡ r001B - RAPOR OLUŞTURMA ===")
        self.reporter.generate_comprehensive_report()

if __name__ == "__main__":
    toolkit = SocialMediaToolkit()
    toolkit.banner()
    toolkit.main_menu()
