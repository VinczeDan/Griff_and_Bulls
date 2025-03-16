import requests
from bs4 import BeautifulSoup

# Az MLSZ adatbank oldal URL-je
url = "https://adatbank.mlsz.hu/club/63/13/29938/1/294435.html"

# HTTP kérés küldése
response = requests.get(url)

# Ellenőrizd, hogy a kérés sikeres volt-e
if response.status_code == 200:
    # HTML tartalom elemzése
    soup = BeautifulSoup(response.text, 'html.parser')

    # Példa: Keresd meg a meccsek táblázatát
    matches = soup.find_all('div', class_='schedule')  # A class_ értéke változhat az MLSZ honlapján

    # Az adatok feldolgozása
    for match in matches:
        home_team = match.find('div', class_='home_team').text.strip()
        away_team = match.find('div', class_='away_team').text.strip()
        score = match.find('span', class_='schedule-points').text.strip()

        print(f"{home_team} {score} {away_team}")
else:
    print(f"Nem sikerült elérni az MLSZ honlapját. Státusz kód: {response.status_code}")