import nltk
from nltk.chat.util import Chat, reflections
import random

# Define your intents dictionary
intents = {
    "intents": [
        {

            "student": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"],
            "AI": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"]

        },
        {
           "student": ["Bye", "See you later", "Goodbye"],
            "AI": ["See you later, thanks for visiting", "Have a nice day", "Bye! Come back again soon."]

        },
        {
            "student": ["Thanks", "Thank you", "That's helpful"],
            "AI": ["Happy to help!", "Any time!", "My pleasure"]
        },
        {

            "student": ["Where is my class?",  "Which way i can go to my class?"],
            "AI": ["Which year did you studying" , "Give me your current pursuing year"]
        },
        {

            "student": ["Ist year", "1st year"],
            "AI": ["Ground floor ,opposite from the office room ","room no:123"]
        },
        {

             "student": ["IInd year", "2nd year"],
            "AI": ["Third floor ,room no:123"]
        },
        {

             "student": ["IIIrd year", "3rd year"],
            "AI": ["Third floor ,room no:123"]
        },
        {
            "student": ["Will there be reminders or notifications before the event?","When will I get the notifications or remainders prior to the event"],
            "AI": ["Yes ofcourse you will be receiving the notifications before event"],

        },
        {

            "student": ["Will I be able to get the certificate after completing workshop","If any complaints or doubts"],
            "AI": ["Yes you will be receiving the certificate but it will take some time"],

        },

        {

            "student": ["JA number","If any complaints or doubts"],
            "AI": ["AI&DS-9876543210"],

        },
        {

            "student": ["faculty profile"],
            "AI": ["https://www.ritrjpm.ac.in/departments/ai-and-ds/faculty.php"],

        },
        {

            "student": ["Who is the joker in college"],
            "AI": ["suba madhavan","soker madhavan"],

        },
    ]
}

# Function to handle user input and provide appropriate response
def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents['intents']:
        for pattern in intent['student']:
            if pattern.lower() in user_input:
                return random.choice(intent['AI'])
    return "Sorry, I'm not sure how to respond to that."

# Example of interacting with the chatbot
def chat():
    print("Chatbot: Hello! How can I assist you today? (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye'or"quit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)
if __name__ == "__main__":
    chat()
