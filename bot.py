# Knife-chan discord bot, bot for personal moderation of
# a discord server during the bot wars.
# Author: Lucas Lin

import os
import discord
from discord.ext import commands
import bot_commands
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    if message.author.bot and message.author.name != "Knife-chan":
        # add to dictionary
        bot_commands.purge_target[message.channel.id] = {"discriminator": message.author.discriminator, "name": message.author.name}

    print("Marked bots for death")
    print(bot_commands.purge_target)
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))

bot.add_command(bot_commands._testing)
# bot.add_command(bot_commands._troll)
# bot.add_command(bot_commands._purge)
# bot.add_command(bot_commands._ping_pong)
bot.add_command(bot_commands._keyboard)

bot.run(os.getenv("BOT_TOKEN"))
