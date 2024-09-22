import requests

url = "https://api.qr-code-generator.com/v1/codes"
params = {
    "access-token": "yCqMeZOoAq708oDFH8-lPS3N8wA2yuGVdFfZgphs7Sx7a6Y0oNCn0JO5C-lipibI",
    "_lang": "en",
    "status": "active",
    "page": "1",  # Ini akan diperbarui dalam loop
    "per-page": "10",
    "sort": "-created",
    "expand": "folder,lastFrameTemplate,style,campaign",
    "rnd": "1714834005921"
}
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://app.qr-code-generator.com",
    "priority": "u=1, i",
    "referer": "https://app.qr-code-generator.com/",
    "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# Membuka file 'id.txt' dengan mode append di luar loop
with open('id.txt', 'a') as file:
    # Loop untuk halaman 1 sampai 20
    for page in range(1, 21):
        params['page'] = str(page)
        
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            ids = [item['id'] for item in data]
            print(f"IDs found in the response for page {page}:", ids)
            
            # Menyimpan hasil ke dalam file 'id.txt' dengan metode append
            for id_value in ids:
                file.write(str(id_value) + '\n')
        else:
            print(f"Failed to fetch data for page {page}. Status code:", response.status_code)
