import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("MTQ1MTI3Nzk0MTI2MTU5ODgxNg.GUz3Dj.pBTdaBQBnp_r2GWxIcmLVo7wOq5MqKC1lavicE")
