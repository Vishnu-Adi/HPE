# main.py
import os
from dotenv import load_dotenv
from prompt import classification_prompt
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential



load_dotenv()

endpoint = "https://models.inference.ai.azure.com"
api_key = os.getenv("PHI_API_KEY")
model_name = "Phi-4"
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key),
)
def get_response(user_input):
    messages = [
        SystemMessage(content=classification_prompt),
        UserMessage(content=user_input),
    ]
    response = client.complete(
        messages=messages,
        temperature=1.0,
        top_p=0.5,
        max_tokens=1000,
        model=model_name,
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
