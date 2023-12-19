import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

my_news = {}

def haberleri_cek(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        haberler = soup.find_all('span', class_='titleline')

        for i, haber in enumerate(haberler[:5]):
            haber_metni = haber.find('span').text
            haber_baslik = haber.find('a').text
            print(f"Haber {i + 1}:")
            print(f"Başlık: {haber_metni}")
            print(f"Metin: {haber_baslik}")
            print("")
        return haberler
    else:
        print(f"Hata! Sayfa yüklenemedi. Status Code: {response.status_code}")


haberleri_cek(url)