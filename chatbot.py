import json
import random

# Load intents from JSON file
with open("intents.json", "r") as file:
    intents = json.load(file)["intents"]

def get_response(user_input):
    user_input = user_input.lower()

    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that. Could you please rephrase?"
