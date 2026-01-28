import random
import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("app/intents.json") as file:
    intents = json.load(file)

def get_response(user_input):
    doc = nlp(user_input.lower())
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_doc = nlp(pattern.lower())
            if any(token.text in [t.text for t in doc] for token in pattern_doc):
                return random.choice(intent["responses"])
    return "I'm sorry, I don't understand. Can you rephrase?"
