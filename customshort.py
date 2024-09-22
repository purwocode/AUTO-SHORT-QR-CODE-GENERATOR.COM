import requests
import random
import string

# Fungsi untuk membaca ID dari file
def read_id_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Fungsi untuk membuat kode acak
def generate_random_code(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Fungsi untuk menyimpan short URL ke file
def append_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text + '\n')

# URL awal
base_url = "https://api.qr-code-generator.com/v1/codes/"
base_token = "yCqMeZOoAq708oDFH8-lPS3N8wA2yuGVdFfZgphs7Sx7a6Y0oNCn0JO5C-lipibI"
# Baca semua ID dari file
ids = read_id_from_file("id.txt")

# Loop melalui setiap ID dan melakukan proses
for id_value in ids:
    # Gabungkan ID dengan URL
    url = f"{base_url}{id_value}?access-token={base_token}"

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://app.qr-code-generator.com",
        "priority": "u=1, i",
        "referer": "https://app.qr-code-generator.com/",
        "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    # Membuat kode acak
    random_code = generate_random_code()

    data = {
        "domain_id": None,
        "short_code": random_code
    }

    # Lakukan permintaan ke server
    response = requests.put(url, headers=headers, json=data)

    # Tampilkan hanya nilai 'short_url' dari respons dan simpan ke file
    if response.status_code == 200:
        response_json = response.json()
        if 'short_url' in response_json:
            short_url = response_json['short_url']
            print(f"ID: {id_value}, Random Code: {random_code}, Short URL: {short_url}")
            append_to_file("shortlink.txt", short_url)
        else:
            print(f"ID: {id_value}, Random Code: {random_code}, Short URL not found in response")
    else:
        print(f"ID: {id_value}, Random Code: {random_code}, Error: {response.status_code}")
