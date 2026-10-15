# main.py
import os
import sys

# Re-run with the project's virtualenv Python so `python3 main.py` just works
_venv_python = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".venv", "bin", "python")
if os.path.exists(_venv_python) and os.path.realpath(sys.prefix) != os.path.realpath(os.path.dirname(os.path.dirname(_venv_python))):
    os.execv(_venv_python, [_venv_python] + sys.argv)

import google.generativeai as genai
from dotenv import load_dotenv

def main():

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        "gemini-2.5-flash",
        system_instruction=(
            "Be extremely concise. Give only what was asked, with no preamble, "
            "filler, or closing remarks. "
            "If asked for code, reply with only the code, with no explanation before or after. "
            "If asked a multiple-choice question, reply with only the correct option, with no explanation. "
            "For other questions, answer in as few words as possible. "
            "Only explain if the user explicitly asks for an explanation."
        ),
    )

    chat = model.start_chat(history=[])

    while True:
        user_input = input("You : ")
        if user_input.lower() in ["exit", "quit"]:
            print("bye")
            break

        response = chat.send_message(user_input)
        print("Bot :", response.text, "\n")

if __name__ == "__main__":
    main()
