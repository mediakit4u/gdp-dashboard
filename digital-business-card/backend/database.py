import json

def save_card(data):
    with open("cards.json", "a") as file:
        file.write(json.dumps(data) + "\n")

def get_cards():
    with open("cards.json", "r") as file:
        return [json.loads(line) for line in file.readlines()]
