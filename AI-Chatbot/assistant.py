from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

print("=" * 40)
print("   My Assistant   ")
print("=" * 40)

roles = {"1": "You are a friendly school teacher. Explain every concept using simple langauge and real-life examples", 
         "2": "You are a senior Python developer. Explain programming concepts clearly and always include python examples.",
         "3": "You are an experienced travel guide. Recommend places, food, transportation and travel.",
         "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",
         "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."}

memory = []

# Greet the user
print("\nAI: Hello! I'm ready to help you.")
print("Type 'quit' anytime to exit.\n")

while True:
    choice_input = input("Choose your assistant.\n 1. Teacher\n 2. Python Expert\n 3. Travel Guide\n 4. Motivational Coach\n 5. Interviewer\n Enter your choice: ")
    memory.append({"role": "system", "content": roles.get(choice_input)})
    
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
    
