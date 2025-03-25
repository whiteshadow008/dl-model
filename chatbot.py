from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot(
    name="Chatty",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I'm sorry, I don't understand. Can you rephrase that?",
            "maximum_similarity_threshold": 0.90,
        }
    ],
)

# Train the chatbot on the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Function to interact with the chatbot
def chat_with_bot():
    print("Hello! I'm Chatty, your AI friend. Let's chat!")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "bye", "quit"]:
            print("Chatty: Goodbye! It was nice talking to you!")
            break
        
        response = chatbot.get_response(user_input)
        print(f"Chatty: {response}")

# Run the chatbot
chat_with_bot()
