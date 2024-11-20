def getGacEventResults():
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
  events = soup.find_all("div", class_="gac-counters-battle-summary")

  event_results = []

  # Iterate through each event
  for event_id, event in enumerate(events, start=1):
    # Initialize event data dictionary
    event_data = {"event_id": event_id}

    # Find all stat labels and their corresponding values
    stats = event.find_all("div", class_="gac-counters-battle-summary__stat")
    for stat in stats:
      label = stat.find("div", class_="gac-counters-battle-summary__stat-label").text.strip()
      value = stat.find("div", class_="gac-counters-battle-summary__stat-value").text.strip()

      # Add label-value pairs to the event data
      if label == "Banners":
        event_data["banners"] = value
      elif label == "Attempt":
        event_data["attempt"] = value
      elif label == "Outcome":
        event_data["outcome"] = value
      elif label == "Duration":
        event_data["duration"] = value
      elif label == "Date":
        event_data["date"] = value

    event_results.append(event_data)

  # Print the full results for verification
  # print("\nFinal GAC Results:")
  # print(json.dumps(gac_results, indent=4, ensure_ascii=False))

  # Save results to JSON
  with open("./results/event_results.json", "w", encoding="utf-8") as json_file:
      json.dump(event_results, json_file, indent=4, ensure_ascii=False)

  print("GAC Event Results have been written to 'event_results.json'.")
  return event_results
