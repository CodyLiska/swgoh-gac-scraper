import json

def getGacEventMatchup():
  from bs4 import BeautifulSoup
  
  with open("./Test-HTML-Files/GacEventData.html", encoding="utf-8") as testFile:
    soup = BeautifulSoup(testFile, 'html.parser')
    
    matchup = soup.find('div', class_='mt-2 paper text-center').text.strip()
    print(matchup)

    # Output grouped data as JSON
    with open("./results/matchup.json", "w", encoding="utf-8") as json_file:
      json.dump(matchup, json_file, indent=4, ensure_ascii=False)

    print("Matchup data has been written to 'matchup.json'.")

    return matchup