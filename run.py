import os
import time
import json
 
def update():
    os.system("clear")
    print("\033[1m\033[97m[•] Melakukan update ...\033[97m")
    os.system("git pull")

    # Check if the update was successful
    if os.system("git status | grep 'Your branch is up to date'") == 0:
        print("\033[1m\033[92m[✓] Update berhasil!\033[97m")
    else:
        print("\033[1m\033[91m[x] Update gagal!\033[97m")

    time.sleep(2)
    input("\n\033[1m\033[97m[•] Tekan Enter untuk melanjutkan...")
    os.system("clear")
update()
def delete_data():
    try:
        os.remove('data.json')
        print("All saved keys have been deleted.")
    except FileNotFoundError:
        print("\033[1m[•]\033[91m Belum Ada Hasil Yang Tersimpan !\033[97m")


def print_purple(text):
    print("\033[95m" + text + "\033[0m")

def check_data():
    try:
        with open('data.json', 'r') as file:
            data = file.read()
            if not data.strip():
                print_purple("Data tidak tersimpan di 'data.json'!")
                return

            try:
                saved_data = json.loads(data)
            except json.JSONDecodeError:
                print("Error: 'data.json' is not valid JSON.")
                return

            print_purple("Isi 'data.json':")
            print(json.dumps(saved_data, indent=4))

    except FileNotFoundError:
        print_purple("File 'data.json' not found!")
    except Exception as e:
        print(f"Error: {e}")

def input_key():
    key = input("\033[1m[•] Masukkan Key Login:\033[92m ")
    print("\033[1m\033[97m[•] Mohon tunggu sebentar...")
    if key != '123456789':
        print()

        # Animasi loading
        for _ in range(10):
            for char in "|/-\\":
                time.sleep(0.1)  # Waktu jeda untuk animasi
                print(f"\r[•] Checking key... {char}", end='', flush=True)
            print(f"\r{' ' * len('[•] Checking key... ')}", end='', flush=True)  # Menghapus teks sebelumnya

        # Setelah animasi loading selesai, hapus baris sebelumnya
        print("\r\033[K[•] Key Salah \033[91mx\033[1m\033[97m")

        # Menghapus tanda /\||
        print("\033[K", end='')

        # Lanjutkan dengan bagian program lainnya di sini
        time.sleep(2)
        os.system("python run.py")
    else:
        print()

        # Animasi loading
        for _ in range(10):
            for char in "|/-\\":
                time.sleep(0.1)  # Waktu jeda untuk animasi
                print(f"\r[•] Checking key... {char}", end='', flush=True)
            print(f"\r{' ' * len('[•] Checking key... ')}", end='', flush=True)  # Menghapus teks sebelumnya

        # Setelah animasi loading selesai, hapus baris sebelumnya
        print("\r\033[K[•] Key Benar \033[92m✓")

        # Menghapus tanda /\||
        print("\033[K", end='')

        # Lanjutkan dengan bagian program lainnya di sini
        time.sleep(2)
        os.system("clear")
        os.system("python .app.py")

def display_menu():
    os.system("clear")
    print("\033[1m\033[97m╔══════════════════════════════╗╔════════════════════════╗")
    print("║             \033[95mMENU\033[97m             ║║         \033[95mINFO\033[97m           ║")
    print("╟──────────────────────────────╢╟────────────────────────╢\033[97m")
    print("║\033[97m   [1] Jalankan Secript FPT   ║║  Versi  : FPT V1.0     \033[97m║")
    print("║   [2] Check Hasil Yang Masuk ║║  Creator: Kztutorial   ║")
    print("║   [3] Hapus Hasil Yang Masuk ║║  Githube: Kztutorial99 ║")
    print("║   [4] Keluar                 ║║                        ║")
    print("╚══════════════════════════════╝╚════════════════════════╝")

def main():
    while True:
        display_menu()
        choice = input("\033[1m\033[97m[•] Enter your choice:\033[92m ")
        print("\033[1m\033[93m-----------------------\033[97m")
        if choice == '1':
            input_key()
            input("\033[1m[•]Press Enter to continue...")
        elif choice == '2':
            check_data()
            input("\033[1m[•] Press Enter to continue...")
        elif choice == '3':
            delete_data()
            input("\033[1m[•] Press Enter to continue...")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
