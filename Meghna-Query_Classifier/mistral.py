# main.py
import os
from mistralai import Mistral
from prompt import classification_prompt
import random
from dotenv import load_dotenv

load_dotenv()

def get_response(user_input):
    client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))

    response = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {"role": "system", "content": classification_prompt},
            {"role": "user", "content":user_input}
    ]
    )
    return response.choices[0].message.content

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
