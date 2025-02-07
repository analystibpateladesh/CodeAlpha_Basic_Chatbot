import random
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"hi|hello|hey", [
            "Hello there! How's your day going?", 
            "Hey! What's new with you?", 
            "Hi! How can I make your day better today?"
        ]
    ],
    [
        r"how are you(.*)", [
            "I'm doing great, thanks for asking! How about you?", 
            "I'm just a virtual assistant, but I'm ready to chat. How are you feeling?"
        ]
    ],
    [
        r"what(.*) your name(.*)", [
            "I'm your friendly chatbot, but you can call me ChatBuddy! What's your name?", 
            "They call me ChatBuddy. What's yours?"
        ]
    ],
    [
        r"my name is (.*)", [
            "Nice to meet you, {0}! How can I assist you today?", 
            "Lovely name, {0}. So, what would you like to talk about today?"
        ]
    ],
    [
        r"what can you do(.*)", [
            "I can chat with you, share jokes, provide advice, and make your day better. Just ask!", 
            "I'm here to chat, keep you company, and maybe even make you laugh!"
        ]
    ],
    [
        r"tell me a joke", [
            "Why don't scientists trust atoms? Because they make up everything!", 
            "Why did the computer go to the doctor? Because it caught a virus!", 
            "What do you call a bear with no teeth? A gummy bear!"
        ]
    ],
    [
        r"(.*) created you(.*)", [
            "I was created by an awesome developer as part of a cool coding project!", 
            "A creative mind brought me to life for interesting conversations!"
        ]
    ],
    [
        r"(.*) weather(.*)", [
            "I can't check the weather right now, but I hope it's sunny wherever you are!", 
            "Weather changes all the time, just like conversations. Let's keep talking!"
        ]
    ],
    [
        r"bye|goodbye|exit", [
            "Goodbye! Have an amazing day ahead!", 
            "Take care! Come back soon for another chat!"
        ]
    ],
    [
        r"(.*)", [
            "That's interesting! Tell me more.", 
            "Can you elaborate on that?", 
            "I'm curious—what else can you share?"
        ]
    ]
]

print("Welcome to ChatBuddy! Type 'bye' to end the conversation.")

chatbot = Chat(pairs, reflections)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit"]:
        print("ChatBuddy: Goodbye! Take care.")
        break
    response = chatbot.respond(user_input)
    if "{0}" in response:
        name = user_input.split()[-1]
        response = response.format(name)
    print("ChatBuddy:", response)
