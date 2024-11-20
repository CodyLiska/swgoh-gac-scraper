import json

def getCharacters():
  from bs4 import BeautifulSoup
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
  events = soup.find_all("div", class_="gac-counters-battle-summary")

  gac_teams = []

  for event_id, event in enumerate(events, start=1):
    # Initialize storage for this event
    event_data = {"event_id": event_id, "offense_team": [], "defense_team": []}

    # Extract attacking team
    attacking_team = event.find("div", class_="gac-counters-battle-summary__side--attacker")
    if attacking_team:
      attack_characters = attacking_team.find_all("div", attrs={"data-unit-def-tooltip-app": True})
      event_data["offense_team"] = [char["data-unit-def-tooltip-app"] for char in attack_characters]

    # Extract defending team
    defending_team = event.find("div", class_="gac-counters-battle-summary__side--defense")
    if defending_team:
      defense_characters = defending_team.find_all("div", attrs={"data-unit-def-tooltip-app": True})
      event_data["defense_team"] = [char["data-unit-def-tooltip-app"] for char in defense_characters]

    # Add this event's data to the grouped data
    gac_teams.append(event_data)

  # Print grouped data for debugging
  # for i, event in enumerate(grouped_data):
  #   print(f"Event {i + 1}:")
  #   print("  Offense Team:", event["offense_team"])
  #   print("  Defense Team:", event["defense_team"])

  # Output grouped data as JSON
  with open("./results/teams.json", "w", encoding="utf-8") as json_file:
    json.dump(gac_teams, json_file, indent=4, ensure_ascii=False)

  print("Teams data has been written to 'teams.json'.")

  return gac_teams
