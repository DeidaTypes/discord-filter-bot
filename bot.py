"""
Discord Bot

This is a simple Discord bot that blocks certain words.
"""
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

blocked_words = ['fag', 'faggot', 'retard', 'retarded']  # List of blocked words

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    """
    Event handler for processing incoming messages.

    Args:
        message (discord.Message): The message received.

    """
    if message.author == bot.user:
        return

    # Check if the message contains any blocked words
    for word in blocked_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f'{message.author.mention}, please refrain from using that language.')
            break

    await bot.process_commands(message)

def run_discord_bot():
    bot_token = os.getenv('BOT_TOKEN')
    bot.run(bot_token)

if __name__ == '__main__':
    run_discord_bot()


    
