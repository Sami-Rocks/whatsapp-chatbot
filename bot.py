from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Fall')

#trainer= ListTrainer(chatbot)

response = chatbot.get_response("What are you doing?")
print(response)