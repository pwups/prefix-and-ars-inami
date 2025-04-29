import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Important for on_message
intents.guilds = True  # Important for editing channels

bot = commands.Bot(command_prefix=";", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Commands
@bot.command(name="a")
async def approve(ctx):
    await ctx.send("_ _\n\n　　　　𝜗 　[**checkpoints required**]( https://discord.gg/SAzqaQuCQA )\n　　　　don't join if not posting yet\n-# _ _　　　⠀  **1w  to  post  ask  4  ext.**　<a:freedom:1350041904099889182> 　୧\n\n_ _")

@bot.command(name="d")
async def sep_over(ctx):
    await ctx.send("_ _\n\n\n\n　　　　　　♡　　₊　　*sep  over.*\n　　　　　　run　**` /regret `**  ৎ\n\n\n\n_ _")

    try:
        await ctx.channel.edit(name="done")
    except discord.Forbidden:
        await ctx.send("I don't have permission to rename the channel.", delete_after=5)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}", delete_after=5)

# Autoresponders
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Autoresponder for "rainbow sprinkles"
    if message.content.lower() == "rainbow sprinkles":
        await message.channel.send("_ _\n\n　　**send a song reco**　·　<a:star1:1365889441310179389>\n　　i like = free ovn　✿\n\n_ _")

    # Autoresponder for "freaky"
    if message.content.lower() == "freaky":
        await message.channel.send("_ _\n\n　　**pls send an eren gif heh.**　·　<:freaky:1365898553578487808>\n\n_ _")

    # Process commands (very important)
    await bot.process_commands(message)

@bot.event
async def on_ready():
    # Set the bot's status
    activity = discord.Activity(type=discord.ActivityType.watching, name="miel's tickets lolol")
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
