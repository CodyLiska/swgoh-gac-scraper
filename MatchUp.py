def getGacEventMatchup():
  from bs4 import BeautifulSoup
  import json
  import requests

  # # FOR TESTING WITH A FILE
  # with open("./Test-HTML-Files/CompleteBattleHTML.html", encoding="utf-8") as testFile:
  #   soup = BeautifulSoup(testFile, "html.parser")

  # URL to fetch HTML from
  url = "https://swgoh.gg/p/887623583/gac-history/O1730844000000/3/"

  # Send a GET request to fetch the HTML content
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
      # Parse the HTML content with BeautifulSoup
      soup = BeautifulSoup(response.text, "html.parser")
      # Now you can work with the soup object as usual
      #print(soup.prettify())  # Example of printing the parsed HTML
  else:
      print(f"Failed to retrieve the webpage: {response.status_code}")

  # Find all event containers
  events = soup.find_all("div", class_="tab-content")
  #print(events)

  matchups = []

  for event_id, event in enumerate(events, start=1):
    matchup_data = {"event_id": event_id}

    # Extract the matchup information from the header
    matchup_section = event.find("div", class_="mt-2 paper text-center")  # Use event to limit the scope

    if matchup_section:
      matchup_text = matchup_section.text.strip()
      print(f"Raw matchup text: {matchup_text}")

      # Extract player names by splitting the string
      if " / " in matchup_text:
        players = matchup_text.split(" / ")
        player1 = players[0].split("'")[0].strip()  # Extracting the name before "'s"
        player2 = players[1].split("'")[0].strip()  # Extracting the name before "'s"
        
        matchup_data["player"] = player1
        matchup_data["opponent"] = player2
      else:
        matchup_data["player"] = "Unknown"
        matchup_data["opponent"] = "Unknown"
    else:
        matchup_data["player"] = "Unknown"
        matchup_data["opponent"] = "Unknown"

    matchups.append(matchup_data)

  # Output JSON
  with open("./results/matchup.json", "w", encoding="utf-8") as json_file:
      json.dump(matchups, json_file, indent=4, ensure_ascii=False)

  print("Matchup data has been written to 'matchup.json'.")
  return matchups
