import json

def load_matchups():
  try:
    with open("./results/matchup.json", "r", encoding="utf-8-sig") as file:
      data = json.load(file)
      print("Loaded matchups:", data)  # Debug print
      return data
  except Exception as e:
    print(f"Error loading matchup.json: {e}")
    return []
  
def load_event_results():
  try:
    with open("./results/event_results.json", "r", encoding="utf-8-sig") as file:
      data = json.load(file)
      #print("Loaded event results:", data)  # Debug print
      return data
  except Exception as e:
    print(f"Error loading event_results.json: {e}")
    return []
  
def load_characters():
  try:
    with open("./results/teams.json", "r", encoding="utf-8-sig") as file:
      data = json.load(file)
      #print("Loaded characters:", data)  # Debug print
      return data
  except Exception as e:
    print(f"Error loading teams.json: {e}")
    return []

def combine_event_data():
  characters_data = load_characters()
  event_results_data = load_event_results()
  matchups_data = load_matchups()

  combined_data = []
  for event in event_results_data:
    event_id = event.get("event_id")
    
    characters = next((char for char in characters_data if char["event_id"] == event_id), {})
    matchup = next((match for match in matchups_data if match["event_id"] == event_id), {})
    if matchup is None:
      matchup = {}

    combined_event = {
      "event_id": event_id,
      "results": event,
      "teams": characters,
      "matchup": matchup,
    }
    combined_data.append(combined_event)

  try:
    with open("./results/gac_event_data.json", "w", encoding="utf-8") as file:
      json.dump(combined_data, file, indent=4, ensure_ascii=False)
    print("GAC Event data has been saved to 'gac_event_data.json'.")
    #print(combined_data)
  except Exception as e:
    print(f"Error saving combined data: {e}")

  return combined_data

def combineResults():
  print("Starting data combination...")  # Debug print
  combined_data = combine_event_data()
  print("Data combined.")  # Debug print
  return combined_data
