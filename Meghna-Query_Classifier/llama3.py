import os
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from prompt import classification_prompt

load_dotenv()
token = os.getenv("LLAMA_API_KEY")
endpoint = "https://models.github.ai/inference"
model_name = "meta/Meta-LLaMA-3-8B-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)
def get_response(user_input):
    messages = [
    SystemMessage(classification_prompt),
    UserMessage(user_input),
]
    response = client.complete(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model_name
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
