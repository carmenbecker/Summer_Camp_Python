"""
Created on 5/24/2023

@author: carmen
"""

import random
import time


def get_user_input():
    user_input = input("You: ")
    return user_input.lower()


def chatbot_response(user_input):
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "take care"]
    jokes = [
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "Había una vez un perro llamado Nadie. Un día, Nadie se perdió. La dueña preguntó: ¿Alguien ha visto a Nadie? Y todos respondieron: ¡No, Nadie!"
        "Mamá, en el colegio me llaman Facebook. ¿Y tú qué les has dicho? ¡Me gusta!"]

    if user_input in greetings:
        return "ChatBot: Hello! How can I assist you today?"
    elif user_input in farewells:
        return "ChatBot: Goodbye! Have a nice day!"
    elif "name" in user_input:
        return "ChatBot: My name is ChatBot. Nice to meet you!"
    elif "age" in user_input:
        return "ChatBot: I'm a chatbot. I don't have an age!"
    elif "joke" in user_input:
        return "ChatBot: " + random.choice(jokes)
    else:
        return "ChatBot: Sorry, I didn't understand that. Can you please rephrase?"


def run_chatbot():
    print("ChatBot: Hello! I'm a chatbot. How can I assist you today?")

    while True:
        user_input = get_user_input()

        if user_input == "exit":
            print("ChatBot: Goodbye! Have a nice day!")
            break

        response = chatbot_response(user_input)
        print(response)
        time.sleep(1)  # Delay the bot's response for better interaction




if __name__ == '__main__':
    run_chatbot()
