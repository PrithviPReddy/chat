# main.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

def main():
    
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")
    
    chat = model.start_chat(history=[])

    while True:
        user_input = input("You : ")
        if user_input.lower() in ["exit", "quit"]:
            print("bye")
            break

        response = chat.send_message(user_input)
        print("Bot :->", response.text, "\n")

if __name__ == "__main__":
    main()
