import os
import time
import json
import webbrowser
import subprocess
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def delete_data():
    try:
        os.remove('data.json')

        for _ in range(10):
            for char in "|/\\":
                time.sleep(0.1)
                print(f"\r\033[97m    [•] Menghapus hasil.. {char}", end='', flush=True)
            print(f"\r{' ' * len('    [•] Menghapus hasil... ')}", end='', flush=True)

        print()
        print("\033[1m\033[97m    [•]\033[92m Berhasil Menghapus hasil \033[93m✓\033[97m")
        print("\033[K", end='')  # Menghapus tanda /\||
        print()

    except FileNotFoundError:
        print("\033[1m\033[97m    [•]\033[91m Belum Ada Hasil Yang Tersimpan !!!\033[97m")

    except Exception as e:
        print(f"Error: {e}")

def print_purple(text):
    print("\033[95m" + text + "\033[0m")


def check_data():
    try:
        with open('data.json', 'r') as file:
            data = file.read()
            if not data.strip():
                print_purple("    [•] Data tidak tersimpan di 'data.json'!")
                return

            try:
                saved_data = json.loads(data)
            except json.JSONDecodeError:
                print("\033[1m\033[97m    [•]\033[91m Belum Ada Hasil Yang Tersimpan !\033[97m")
                time.sleep(1)
                os.system("cleae")
                return

            # Animasi loading
            for _ in range(10):
                for char in "|/-\\":
                    time.sleep(0.1)  # Waktu jeda untuk animasi
                    print(f"\r\033[97m    [•] Checking hasil.. {char}", end='', flush=True)
                print(f"\r{' ' * len('    [•] Checking hasil... ')}", end='', flush=True)  # Menghapus teks sebelumnya

            print()
            print("\033[1m\033[97m    [•]\033[92m Hasil Tersimpan \033[93m✓\033[97m")
            print("\033[K", end='')  # Menghapus tanda /\||
            print()
            # Mencetak data yang disimpan
            print(json.dumps(saved_data, indent=4))
            print()

    except FileNotFoundError:
        print("\033[1m\033[97m    [•]\033[91m Belum Ada Hasil Yang Tersimpan !\033[97m")
    except Exception as e:
        print(f"Error: {e}")

def menu_fpt():
   print("\033[1m\033[97m")
   print("    [1] Ambil Key Login ")
   print("    [2] Masukan Key Login ")
   print()
   menu = input("    [•] Enter Your Choice:\033[92m ")
   if menu == "1":
     print("\033[1m\033[97m")
     print("    [•] Link Key : \033[92mhttps://sfl.gl/1s71Cc\033[97m  ")
     input("    [•] Press Enter open browser...")
     os.system("xdg-open https://sfl.gl/1s71Cc")
   elif menu == "2":
     input_key()

def input_key():
    print("\033[97m\033[1m")
#    print("    [•] Link Key : \033[92mhttps://sfl.gl/1s71Cc\033[97m  ")
    key = input("\033[1m\033[97m    [•] Masukkan Key Login :\033[92m ")
    print("\033[1m\033[97m    [•] Mohon tunggu sebentar...")
    if key != 'g7lj971vx2zqoxytypahnv':
        print()

        # Animasi loading
        for _ in range(10):
            for char in "|/-\\":
                time.sleep(0.1)  # Waktu jeda untuk animasi
                print(f"\r    [•] Checking key... {char}", end='', flush=True)
            print(f"\r{' ' * len('[•] Checking key... ')}", end='', flush=True)  # Menghapus teks sebelumnya

        # Setelah animasi loading selesai, hapus baris sebelumnya
        print("\r\033[K    [•] Key Salah \033[91mx\033[1m\033[97m")

        # Menghapus tanda /\||
        print("\033[K", end='')

        # Lanjutkan dengan bagian program lainnya di sini
        time.sleep(2)
        display_menu()
    else:
        print()

        # Animasi loading
        for _ in range(10):
            for char in "|/-\\":
                time.sleep(0.1)  # Waktu jeda untuk animasi
                print(f"\r    [•] Checking key... {char}", end='', flush=True)
            print(f"\r{' ' * len('    [•] Checking key... ')}", end='', flush=True)  # Menghapus teks sebelumnya

        # Setelah animasi loading selesai, hapus baris sebelumnya
        print("\r\033[K    [•] Key Benar \033[92m✓")

        # Menghapus tanda /\||
        print("\033[K", end='')

        # Lanjutkan dengan bagian program lainnya di sini
        time.sleep(2)
        os.system("clear")
        os.system("python .app.pyc")

def menu_utama():
    menu_dict = {
        1: "Youtube",
        2: "Whatsapp",
        3: "Facebook",
        4: "Instagram",
        5: "Github",
        6: "Email",
        7: "Grub"
    }

    print("\033[1m\033[97m╔══════════════════════════════╗")
    print("║\033[97m\033[1m   [•]\033[95m Admin Support \033[97m         ║")
    print("╟──────────────────────────────╢")
    print("║\033[97m\033[1m   [1]\033[92m Youtube \033[97m               ║")
    print("║\033[97m\033[1m   [2]\033[92m Whatsapp \033[97m              ║")
    print("║\033[97m\033[1m   [3]\033[92m Facebook \033[97m              ║")
    print("║\033[97m\033[1m   [4]\033[92m Instagram \033[97m             ║")
    print("║\033[97m\033[1m   [5]\033[92m Github \033[97m                ║")
    print("║\033[97m\033[1m   [6]\033[92m Email \033[97m                 ║")
    print("╚══════════════════════════════╝")
    print("\033[1m\033[97m╔══════════════════════════════╗")
    print("║\033[97m\033[1m   [•]\033[95m Join Grub \033[97m             ║")
    print("╟──────────────────────────────╢")
    print("║\033[97m\033[1m   [7]\033[92m Grub Whatsapp \033[97m         ║")
    print("╚══════════════════════════════╝")
    try:
        menu = int(input("\033[1m\033[97m    [•] Pilih layanan:\033[92m "))
        if menu in menu_dict:
            print(f"\033[1m\033[97m    [•] Mengalihkan ke {menu_dict[menu]}...", end='', flush=True)
            for _ in range(10):
                for char in " ⣾⣷⣯⣟⡿⢿⣻⣽":
                    time.sleep(0.1)
                    print(f"\b{char}", end='', flush=True)
            os.system(f"xdg-open {get_link(menu)}")
            print("\033[K", end='')  # Hapus sisa animasi loading setelah mengarahkan
        else:
            print("")
            time.sleep(2)
    except ValueError:
        print("\033[97m\033[1m    [•] \033[91mMasukan tidak valid !")
        time.sleep(2)

def get_link(menu):
    links = {
        1: "https://youtube.com/@Kz.tutorial",
        2: "https://wa.me/62895325844493",
        3: "https://www.facebook.com/profile.php?id=100088711306499",
        4: "https://www.instagram.com/Kztutorial97",
        5: "https://github.com/Kztutorial99",
        6: "mailto:pangkeyjulio2@gmail.com",
        7: "https://chat.whatsapp.com/FIKWwQwu5gpFGefdCRwFcJ",
        9: " "
    }
    return links.get(menu)

def check_time_period():
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        return "Pagi "
    elif 12 <= current_hour < 15:
        return "Siang"
    elif 15 <= current_hour < 18:
        return "Sore "
    else:
        return "Malam"

def update():
    print("\033[1m\033[97m    [•] Mohon tunggu sebentar...\033[92m")
    # Animasi loading
    animation = "|/-\\"
    for _ in range(10):
        for char in animation:
            time.sleep(0.1)
            print(f"\r\033[1m\033[97m    [•] Processing Update... {char}", end='', flush=True)
        print("\r\033[K", end='', flush=True)

    try:
        # Melakukan git pull dan menangkap output serta errornya
        output = os.popen("git pull 2>&1").read()

        # Memeriksa apakah output mengandung string "Already up to date."
        if "Already up to date." not in output:
            print("\n\033[1m\033[97m    [•] \033[92mBerhasil Update Script \033[93m✓ \033[92m")
        else:
            print("\n\033[1m\033[97m    [•] \033[92mBerhasil Update Script \033[93m✓\033[92m")

    except Exception as e:
        # Menangani pesan kesalahan dan menampilkan pesan yang sesuai
        if "SSL_ERROR_SYSCALL" in str(e):
            print("\033[97m    [!] \033[91mGagal Melakukan Update Gagal ! \033[97m")
            print("\033[97m    [!] \033[91mKoneksi SSL gagal.\033[0m")
            print("\033[97m    [!] \033[91mSilahkan Coba lagi nanti ! \033[97m")
        else:
            print(f"\n\033[91m    [•] Gagal melakukan update: {e}\033[0m")

    input("\n\033[1m\033[97m    [•] Tekan Enter untuk melanjutkan...")
    os.system("clear")

def display_menu():
    os.system("clear")
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d-%m-%Y")
    print("\033[1m\033[97m╔══════════════════════════════╗╔════════════════════════╗")
    print("║             \033[95mMENU\033[97m             ║║         \033[95mINFO\033[97m           ║")
    print("╟──────────────────────────────╢╟────────────────────────╢\033[97m")
    print("║\033[97m   [1]\033[92m Jalankan Secript FPT   \033[97m║║  Versi  :\033[92m FPT\033[91m V1.0     \033[97m║")
    print("║\033[97m   [2]\033[92m Check Hasil Yang Masuk \033[97m║║  Creator:\033[92m Kz.tutorial  \033[97m║")
    print("║\033[97m   [3]\033[92m Hapus Hasil Yang Masuk \033[97m║║  Githube:\033[92m Kztutorial99 \033[97m║")
    print("║\033[97m   [4]\033[92m Hubungi Pembuat        \033[97m║║                        ║")
    print(f"║\033[97m   [5]\033[92m Update Secript         \033[97m║║  Tanggal: \033[96m{current_date}\033[97m   ║")
    print(f"║\033[97m   [6]\033[92m Keluar                 \033[97m║║  Jam: \033[96m{current_time}\033[97m\033[93m {waktu}\033[97m   ║")
    print("╚══════════════════════════════╝╚════════════════════════╝")

def main():
    while True:
        display_menu()
        choice = input("\033[1m\033[97m    [•] Enter your choice:\033[92m ")
        if choice == '1':
            menu_fpt()
        elif choice == '2':
            check_data()
            input("\033[1m    [•] \033[93mPress \033[92mEnter\033[93m to continue...\033[93m")
        elif choice == '3':
            delete_data()
            input("\033[1m    [•] \033[93mPress \033[92mEnter\033[93m to continue...\033[97m")
        elif choice == '4':
            menu_utama()
        elif choice == '5':
            update()
        elif choice == '6':
            print("\033[1m\033[97m    [•]\033[91m\033[1m Exit Program...\033[97m")
            print()
            break
        else:
            print("\033[97m\033[1m    [•] \033[91mMasukan tidak valid !")
            time.sleep(2)

if __name__ == "__main__":
    waktu = check_time_period()
    main()
