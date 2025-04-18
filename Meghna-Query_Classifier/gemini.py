# main.py
import os
from dotenv import load_dotenv
from prompt import classification_prompt
import google.generativeai as genai



load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def get_response(user_input):
    messages=classification_prompt + "\n\nUser: " +user_input
    response = model.generate_content(messages)
    return response.text

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Write the question: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                break
            ai_response = get_response(user_input)
            print(ai_response)
        except KeyboardInterrupt:
            print("\nExiting...") 
            break
