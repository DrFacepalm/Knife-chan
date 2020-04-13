from discord.ext import commands
from discord import Embed
import keyboard_scraper as ks

# Channel id and bot user
last_bot = {}

################
# PING COMMAND #
################
@commands.command(name="ping")
async def _ping_pong(ctx):
    await ctx.send("pong")

################
# TEST COMMAND #
################
@commands.command(name='_test')
async def _testing(ctx, *args):
    embed = Embed(
        colour=0x0099ff,
        title="Hello World")
    embed.title = "This should work"
    embed.description = "`1.` nani nani nani\n\n`2.` nani nani nani nani"

    await ctx.channel.send(embed=embed)

#################
# PURGE COMMAND #
#################
def is_target(m):
    result = False
    if str(m.channel.id) in last_bot.keys():
        result = m.author.discriminator == last_bot[m.channel.id]["discriminator"]
    return result

@commands.command(name='purge')
async def _purge(ctx, *args):
    if ("Moderator" in (r.name for r in ctx.author.roles)):
        # for mention bot
        if (len(ctx.message.mentions) > 0):
            last_bot[str(ctx.message.channel.id)] = {"discriminator": ctx.message.mentions[0].discriminator, "name": ctx.message.mentions[0].name}

        deleted = await ctx.channel.purge(limit=10, check=is_target)
        for msg in deleted:
            print(msg.author.name)
        await ctx.send("Purged! {}".format(len(deleted)), delete_after=5.0)
    else:
        await ctx.send("Sorry {} you don't have permission to do this".format(ctx.message.author.name), delete_after=60.0)

#####################
# KEYBOARDS COMMAND #
#####################
def create_message(list):
    message = ""
    i = 1
    while i <= 10:
        message += f"`{i}.`[{list[i][1]}]({list[i][0]})\n"
        i += 1
    return message

@commands.command(name="keyboards")
async def _keyboard(ctx, *args):
    list = await ks.get_all_recent()
    message = create_message(list)

    embed = Embed(colour=0x0099ff)
    embed.title = "GBs from GeekHack."
    embed.description = message
    await ctx.channel.send(embed=embed)

##################
# IMAGUS COMMAND #
##################
@commands.command(name="imagus")
async def _troll(ctx):
    await ctx.send("Jayden's bot sucks")


if __name__ == "__main__":
    pass
