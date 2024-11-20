# Imports
from bs4 import BeautifulSoup
import json
#import requests

# GET CHARACTER NAMES
# Get the character names from the HTML
# Returns a list of character names JSON
def getCharacters():
    with open("./Test-HTML-Files/GacEventData.html", encoding="utf-8") as testFile:
        soup = BeautifulSoup(testFile, 'html.parser')
        #print(soup.prettify())

        eventContainer = soup.find_all('div', class_='gac-counters-battle-summary__sides')
        attackingContainers = soup.find_all('div', class_='gac-counters-battle-summary__side gac-counters-battle-summary__side--attacker')
        #print(attackingContainers)

        defendingContainers = soup.find_all('div', class_='gac-counters-battle-summary__side gac-counters-battle-summary__side--defense')
        #print(defendingContainers)

        attackCharacterNames = []
        defenseCharacterNames = []
        for event in eventContainer:
            for container in attackingContainers:
                characters = container.find_all('div', attrs={'data-unit-def-tooltip-app': True})
                #print(characters)
                for character in characters:
                    attackCharacterNames.append(character['data-unit-def-tooltip-app'])
                    #print(character['data-unit-def-tooltip-app'])
            print('Attacking Team: ' + str(attackCharacterNames))

            for container in defendingContainers:
                characters = container.find_all('div', attrs={'data-unit-def-tooltip-app': True})
                #print(characters)
                for character in characters:
                    defenseCharacterNames.append(character['data-unit-def-tooltip-app'])
                    #print(character['data-unit-def-tooltip-app'])
            print('Defending Team: ' + str(defenseCharacterNames))

            #character_data = {
            #    'attacking team': attackCharacterNames,
            #    'defending team': defenseCharacterNames
            #}
            #return character_data

        #gac_data = json.dumps(character_data, indent=4)
        #print(gac_data)
        #return gac_data


'''
SAMPLE OUTPUT:

{
    "attacking": [
        "EMPERORPALPATINE",
        "STARKILLER",
        "MARAJADE",
        "OLDBENKENOBI",
        "VISASMARR"
    ],
    "defending": [
        "MANDALORBOKATAN",
        "THEMANDALORIANBESKARARMOR",
        "IG12",
        "PAZVIZSLA",
        "ARMORER"
    ]
}
'''