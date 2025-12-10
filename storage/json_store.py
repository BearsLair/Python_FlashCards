import json

def save_decks(decks):
    with open("../data/json.data", "w") as data:
        data.write(json.dumps(decks))
    print("Saved as JSON to data folder.")

def load_decks():
    with open("../data/json.data", "r") as file:
        data = json.load(file)
    print("Read data in JSON file:")
    print(data)