import spacy
import random
nlp = spacy.load("en_core_web_sm")

intents = {
    "greet": {
        "examples": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hi there!", "Hello!", "Hey! How can I assist you today?"]
    },

    "goodbye": {
        "examples": ["bye", "goodbye", "see you", "talk to you later", "talk later", "talk soon"],
        "responses": ["Goodbye!", "See you soon!", "Take care!"]
    },

    "thanks": {
        "examples": ["thanks", "thank you", "thx", "much appreciated"],
        "responses": ["You're welcome!", "No problem!", "Anytime!"]
    },

    "how_are_you": {
        "examples": ["how are you", "how's it going", "how do you do", "are you fine", "doing okay"],
        "responses": ["I'm doing great, thanks!", "All good here!", "Fantastic, what about you?"]
    },

    "who_made_you": {
        "examples": ["who made you", "who created you", "who built you"],
        "responses": ["I was created by Bineet Bhadani 🧠", "My developer is Bineet, a creative mind!"]
    },

    "name": {
        "examples": ["what's your name", "who are you", "your name please"],
        "responses": ["I'm your friendly chatbot 🤖", "Call me ChatBuddy!", "I'm a smart assistant!"]
    },

    "help": {
        "examples": ["help", "can you help me", "i need assistance", "i need help"],
        "responses": ["Sure! What do you need help with?", "I'm here to assist. Ask me anything."]
    },

    "joke": {
        "examples": ["tell me a joke", "make me laugh", "funny joke please"],
        "responses": [
            "Why did the developer go broke? Because he used up all his cache!",
            "Why don’t robots have brothers? Because they all share the same motherboard!",
            "I would tell you a UDP joke… but you might not get it. 😄"
        ]
    },

    "what_can_you_do": {
        "examples": ["what can you do", "how can you help", "what are your features"],
        "responses": [
            "I can chat, answer questions, tell jokes, and more!",
            "I’m here to talk, assist, and entertain!",
            "Ask me anything. I'm ready!"
        ]
    }
}

def preprocess(text):
    text = text.lower()
    doc = nlp(text)
    cleaned_words = set()
    for token in doc:
        if token.is_punct:
            continue
        cleaned_words.add(token.lemma_)
    return cleaned_words

def get_intent(user_input):
    user_lemmas = preprocess(user_input)
    for intent, data in intents.items():
        for example in data["examples"]:
            example_lemmas = preprocess(example)
            if user_lemmas.intersection(example_lemmas):
                return intent
    return None

def get_response(user_input):
    intent = get_intent(user_input)
    if intent:
        return random.choice(intents[intent]["responses"])
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

def main():
    print("Welcome to the simple chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
