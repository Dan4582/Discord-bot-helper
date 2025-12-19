from flask import Flask
from threading import Thread
import os
import discord
from discord.ext import commands

# Your Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Flask web server
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Run Flask in a separate thread
t = Thread(target=run)
t.start()

# Start the bot
bot.run(os.getenv("TOKEN"))
