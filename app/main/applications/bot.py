from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
#from . import applications

bot = ChatBot("Rohtak")
trainer = ListTrainer(bot)
# trainer.set_trainer(ListTrainer)
# trainer.set_trainer(ChatterBotCorpusTrainer)

# conversation = [
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome."
# ]

#trainer.train(conversation)
#trainer = ListTrainer(bot)
#trainer.train(conversation)
# bot.set_trainer(ListTrainer)
# bot.set_trainer(ChatterBotCorpusTrainer)
#bot.train("chatterbot.corpus.english")
#trainer.train(ListTrainer)
trainer.train("chatterbot.corpus.english")

@applications.route("/bot")
def home():    
    return render_template("bot.html") 

@applications.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText))