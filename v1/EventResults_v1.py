# Imports
from bs4 import BeautifulSoup
import json
#import requests

# GET EVENT STATS
# Get the event stats from the HTML
# Returns a list of event stats JSON
def getGacEventResults():
    with open("./Test-HTML-Files/GacEventData.html", encoding="utf-8") as testFile:
        soup = BeautifulSoup(testFile, 'html.parser')
        #print(soup.prettify())

        statContainers = soup.find_all('div', class_='gac-counters-battle-summary__stat')
        #print(statContainers)

        eventLabels = []
        eventStats = []

        for container in statContainers:
            statLabel = container.find_all('div', class_='gac-counters-battle-summary__stat-label')
            eventLabels.append(statLabel[0].text)
            #print(eventLabels)
            statValue = container.find_all('div', class_='gac-counters-battle-summary__stat-value')
            eventStats.append(statValue[0].text)
            #print(eventStats)

        gac_event_output = list(zip(eventLabels, eventStats))
        gacEvent = {label: stat for label, stat in gac_event_output}
        
        gac_stats = json.dumps(gacEvent, indent=4)
        print(gac_stats)
        return gac_stats


'''
SAMPLE OUTPUT:
{
    "Banners": "4",
    "Attempt": "1",
    "Outcome": "Draw",
    "League": "\u2026",
    "Zone": "\u2026",
    "Duration": " 5m 5s ",
    "Date": " Oct 24, 24 5:06:57 PM "
}
'''