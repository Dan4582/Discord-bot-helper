import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# ---------------- Discord Bot Setup ----------------

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Example command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# ---------------- Flask Web Server ----------------

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))  # Railway assigns PORT
    app.run(host='0.0.0.0', port=port)

# Run Flask in a separate thread
flask_thread = Thread(target=run_flask)
flask_thread.start()

# ---------------- Start Discord Bot ----------------

bot.run(os.getenv("TOKEN"))
