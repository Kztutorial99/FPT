import subprocess

def get_serveo_url():
    try:
        serveo_output = subprocess.check_output("ssh -R 80:127.0.0.1:8090 serveo.net", shell=True)
        serveo_url = serveo_output.decode('utf-8').strip()
        return serveo_url
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

# Contoh penggunaan:
serveo_url = get_serveo_url()
if serveo_url:
    print("URL Serveo:", serveo_url)
else:
    print("Gagal mendapatkan URL Serveo.")
