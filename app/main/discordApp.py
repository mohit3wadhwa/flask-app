from datetime import datetime
from flask import render_template, session, redirect, url_for,flash
from . import main
from dhooks import Webhook
from discord_webhooks import DiscordWebhooks
import os
import discord
#from dotenv import load_dotenv


@main.route('/discord', methods=['GET', 'POST'])
def discord1():
    # hook = DiscordWebhooks("https://discordapp.com/api/webhooks/739500812438339716/ML9oYkmBQbrJglR12XqtFquCG01ksv_7tyt2vVtV9g7s9n_P5xXCIvBAQuVAJ6Wf_B-y")
    # # hook.send = (f"kya baat hai from Python via webhook")
    # hook.set_content(content='Hello! from Python')
    # hook.send()

    #load_dotenv()
    #TOKEN = os.getenv('DISCORD_TOKEN')
    TOKEN ='NzM5NTEwNzA5MzE4MTg5MTI2.XybhBA.9ZB2dELcgNRZxJ9wcbSR4xsbJZw'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    client.run(TOKEN)


    return redirect('/')
    

