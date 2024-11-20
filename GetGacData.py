from bs4 import BeautifulSoup
import requests

def getGacData():
    response = requests.get('https://swgoh.gg/p/887623583/gac-history/O1729630800000/1/')
    html = response.text

    with open('./Test-HTML-Files/GacEventData.html', 'w', encoding='utf-8') as file:
        file.write(html)
    print()
    print("Save Successful")
