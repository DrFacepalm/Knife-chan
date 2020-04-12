from discord.ext import commands
last_bot = {}

@commands.command(name="ping")
async def _ping_pong(ctx):
    await ctx.send("pong")

@commands.command(name='test')
async def _testing(ctx, *args):
    response = ""
    for thing in args:
        response += "{} ".format(thing)
    await ctx.send("You said: {}".format(response))

def is_target(m):
    result = False
    if str(m.channel.id) in last_bot.keys():
        result = m.author.discriminator == last_bot[str(m.channel.id)]["discriminator"]
    return result

@commands.command(name='purge')
async def _purge(ctx, *args):
    if ("Moderator" in (r.name for r in ctx.author.roles)):
        # for mention bot
        if (len(ctx.message.mentions) > 0):
            last_bot[str(ctx.message.channel.id)] = {"discriminator": ctx.message.mentions[0].discriminator, "name": ctx.message.mentions[0].name}
        # for mention self
        deleted = await ctx.channel.purge(limit=10, check=is_target)
        for msg in deleted:
            print(msg.author.name)
        await ctx.send("Purged! {}".format(len(deleted)), delete_after=5.0)
    else:
        await ctx.send("Sorry {} you don't have permission to do this".format(ctx.message.author.name), delete_after=60.0)


@commands.command(name="imagus")
async def _troll(ctx):
    await ctx.send("Jayden's bot sucks")

@commands.command(name="apply")
async def _apply(ctx):
    pass
