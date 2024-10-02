def replace_domain(url, old_domain, new_domain):
    if url.startswith(old_domain):
        return url.replace(old_domain, new_domain, 1)
    else:
        return url

# Baca URL dari file shortlink.txt
with open('shortlink.txt', 'r') as file:
    urls = file.readlines()

# Domain lama yang ingin diganti
old_domain = "https://qrco.de/"

# Proses pertama: ganti ke https://q-r.to/
new_domain_1 = "https://q-r.to/"
updated_urls = []

for url in urls:
    url = url.strip()  # Hapus spasi atau karakter newline
    updated_url = replace_domain(url, old_domain, new_domain_1)
    updated_urls.append(updated_url)

# Simpan hasil sementara ke file
with open('updated_links.txt', 'w') as file:
    for updated_url in updated_urls:
        file.write(f"{updated_url}\n")

print("Proses pertama selesai: semua URL diperbarui ke https://q-r.to/ dan disimpan di updated_links.txt")

# Proses kedua: ganti ke https://l.ead.me/ setelah proses pertama selesai
new_domain_2 = "https://l.ead.me/"
final_updated_urls = []

for url in updated_urls:
    updated_url = replace_domain(url, new_domain_1, new_domain_2)
    final_updated_urls.append(updated_url)

# Tambahkan hasil ke file yang sama
with open('updated_links.txt', 'a') as file:
    for updated_url in final_updated_urls:
        file.write(f"{updated_url}\n")

print("Proses kedua selesai: semua URL diperbarui ke https://l.ead.me/ dan disimpan di updated_links.txt")
