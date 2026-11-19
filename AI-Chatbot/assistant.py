from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

print("=" * 40)
print("   My Assistant   ")
print("=" * 40)

memory = []

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == "quit":
        print("Goodbye! Have a good day!")
        break
    
    memory.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(model=os.getenv("MODEL"), messages=memory)
    ai_response = response.choices[0].message.content
    
    # Temporary addition
    print("----- Conversation History -----")
    for message in memory:
        print(message)
    print("-- End of conversation history --")
    
    memory.append({"role":"assistant","content": ai_response})
    print("\nAI:" + ai_response)
    
