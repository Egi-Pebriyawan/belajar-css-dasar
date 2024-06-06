import requests
import random
import string

# Fungsi untuk mengirim permintaan ke API
def send_request(url, data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Permintaan berhasil!")
    else:
        print(f"Gagal mengirim permintaan ke-{i}: {response.status_code}")

# URL API
url = "https://rabbleit.com/api/users?token=L2pxaGt4ZHJ5aTA_a2V5PTljYTYwMWE5ZjQ3YzczNWRmNzZkNWNhNDZmYTI2YTY2JnN1Ym1ldHJpYz0yMDUxOTE0OQ"

# Melakukan permintaan POST sebanyak 100 kali
for i in range(1, 10):
    # Membuat panjang teks acak
    text_length = random.randint(10, 50)  # Misal, panjang teks acak antara 5 dan 15 karakter
    # Membuat teks acak
    random_text = ''.join(random.choices(string.ascii_lowercase, k=text_length))
    # Data yang akan dikirimkan
    data = {"message": random_text}

    print(f"\nData random yang akan dikirim pada permintaan ke-{i}: {random_text}")

    # Mengirim permintaan ke API
    send_request(url, data)


