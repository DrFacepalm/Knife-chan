# Knife-chan discord bot, bot for personal moderation of
# a discord server during the bot wars.
# Author: Lucas Lin
from discord.ext import commands
from discord import Embed
from discord import File
import rotater
import keyboard_scraper as ks

# Channel id and bot user
purge_target = {}
img_rotater = rotater.ImageRotate()


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
    if m.channel.id in purge_target.keys():
        result = m.author.discriminator == purge_target[m.channel.id]["discriminator"]
    else:
        purge_target[m.channel.id] = {"discriminator": m.channel.last_message.author.discriminator, "name": m.channel.last_message.author.name}
        result = m.author.discriminator == purge_target[m.channel.id]["discriminator"]
    return result

def get_limit(args):
    lim_set = False
    limit = 10
    for arg in args:
        try:
            if not lim_set:
                limit = int(arg)
                lim_set = True
        except ValueError:
            pass
    return limit

@commands.command(name='purge')
async def _purge(ctx, *args):
    if ("Moderator" in (r.name for r in ctx.author.roles)):

        # If a user is mentioned
        if (len(ctx.message.mentions) > 0):
            purge_target[ctx.message.channel.id] = {"discriminator": ctx.message.mentions[0].discriminator, "name": ctx.message.mentions[0].name}

        # Get the number argument if exist
        limit = get_limit(args)

        deleted = await ctx.channel.purge(limit=limit, check=is_target)

        name = purge_target[ctx.message.channel.id]["name"]
        await ctx.send(f"Purged {len(deleted)} messages from {name} out of the last {limit} messages", delete_after=5.0)
    else:
        await ctx.send("Sorry {} you don't have permission to do this".format(ctx.message.author.name), delete_after=60.0)

#####################
# KEYBOARDS COMMAND #
#####################
def create_message(list):
    message = ""
    i = 0
    max = 10
    if len(list) < 10:
        max = len(list)
    while i < max:
        message += f"`{i+1}.`[{list[i][1]}]({list[i][0]})\n"
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

##################
# ROTATE COMMAND #
##################
def _has_attachment(m) -> bool:
    return len(m.attachments) > 0;

@commands.command(name="rotate")
async def _rotate(ctx, *args):
    # get last 20 messages
    msges : list = ctx.channel.history(limit=20)

    # go through and if a message has an attachment, set it.
    msg = None
    i = 0
    async for m in msges:
        if (_has_attachment(m)):
            msg = m
            break
    
    # if there was no message found, finish.
    if (msg == None):
        ctx.channel.send("Couldn't find any images to rotate...")
        return

    path : str = img_rotater.img_convert(msg.attachments[0].url, 90)
    
    await ctx.channel.send(file=File(path))

    img_rotater.img_delete(path)
    print(msg.attachments[0].url)




if __name__ == "__main__":
    
    failed = 0
    # Purge testing
    if (get_limit([2, 3, 4, 5]) != 2):
        failed += 1
        print("get_limit: [2, 3, 4, 5] failed")
    if (get_limit([2, "bad type"]) != 2):
        failed += 1
        print("get_limit: [2, \"bad type\"] failed")
    if (get_limit(["username", 4]) != 4):
        failed += 1
        print("get_limit: [\"username\", 4]")
    if (get_limit(["username", 4, 5, 6, "bad"]) != 4):
        failed += 1
        print("get_limit: [\"username\", 4, 5, 6, \"bad\"]")
    print(f"Purge failed {failed}" if failed != 0 else "Purge Passed\n")

    failed = 0
    # Keybooards Testing
    input_long = [
            ("https://shelloworldhelloworld.com", "1....."), 
            ("https://shelloworldhelloworld.com", "2....."),
            ("https://shelloworldhelloworld.com", "3......"),
            ("https://shelloworldhelloworld.com", "namenamename"),
            ("https://shelloworldhelloworld.com", "naggggggname"),
            ("https://shelloworldhelloworld.com", "namenamename"), 
            ("https://shelloworldhelloworld.com", "namenamename"),
            ("https://shelloworldhelloworld.com", "namenasdfname"),
            ("https://shelloworldhelloworld.com", "namenamename"),
            ("https://shelloworldhelloworld.com", "naggggggname"),
            ("https://shelloworldhelloworld.com", "namenamename"), 
            ("https://shelloworldhelloworld.com", "namenamename"),
            ("https://shelloworldhelloworld.com", "namenasdfname"),
            ("https://shelloworldhelloworld.com", "namenamename"),
            ("https://shelloworldhelloworld.com", "naggggggname")
    ]
    input_short = [
            ("https://shelloworldhelloworld.com", "1......"), 
            ("https://shelloworldhelloworld.com", "2......."),
            ("https://shelloworldhelloworld.com", "3......"),
            ("https://shelloworldhelloworld.com", "namenamename"),
            ("https://shelloworldhelloworld.com", "naggggggname")
    ]
    print(create_message(input_long))
    print(create_message(input_short))
    print(f"Keyboard Passed (Please manually check ouput)")

