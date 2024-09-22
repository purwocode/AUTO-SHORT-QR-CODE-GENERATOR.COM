import requests
import random
import string

def generate_random_email():
    letters = ''.join(random.choices(string.ascii_lowercase, k=5))
    numbers = ''.join(random.choices(string.digits, k=6))
    return f"{letters}{numbers}@mailnesia.com"

def create_accounts(num_accounts):
    url = "https://login.qr-code-generator.com/api/signup"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://login.qr-code-generator.com",
        "priority": "u=1, i",
        "referer": "https://login.qr-code-generator.com/signup/",
        "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    for _ in range(num_accounts):
        email = generate_random_email()
        data = {
            "email": email,
            "password": email,
            "language_code": "en",
            "currency": "usd",
            "terms": True,
            "signup_country_code": "ID"
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 204:
            print(f"Sukses: Create Account for {email}")
            with open("sukses.txt", "a") as file:
                file.write(f"{email}\n")
        elif response.status_code == 400 and "An account with the given email already exists." in response.text:
            print(f"Gagal: An account with the given email ({email}) already exists.")
        else:
            print(f"Tidak diketahui untuk {email}: ", response.text)

# Tentukan jumlah akun yang ingin dibuat
num_accounts = int(input("Masukkan jumlah akun yang ingin dibuat: "))
create_accounts(num_accounts)
