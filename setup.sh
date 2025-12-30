#!/bin/bash
echo "⚡ r001B - Social Media Security Toolkit Kurulumu"

# Python ve pip kontrolü
if ! command -v python3 &> /dev/null; then
    echo "Python3 yüklenmeli!"
    exit 1
fi

# Gerekli kütüphaneleri yükle
pip3 install -r requirements.txt

# Wordlist oluştur
mkdir -p wordlists
echo "admin\n123456\npassword\n123456789" > wordlists/common_passwords.txt

# Çalıştırma izni ver
chmod +x main.py

echo "⚡ r001B - Kurulum tamamlandı! Çalıştırmak için: python3 main.py"
