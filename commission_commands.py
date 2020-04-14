# Knife-chan discord bot, bot for personal moderation of
# a discord server during the bot wars.
# Commission commands for the bot
# Author: Lucas Lin

import discord

####################################################
# COMISSIONED COMMAND ##############################
# COMMISSIONED BY Zachaccino:430382953659367425 ###
# PURRRGE: purges based on amount of Rs in command #
# without argument, purges X indiscrimantely, with #
# singular mention, purges X if specified user #####
####################################################
async def _process_PURRRGE(message):
    
    # Check command
    if (message.content.startswith('!PUR')):
        command = message.content.split(" ")[0]

        # Check command
        if (command.endswith('GE') and command[3:-2] == "R"*len(command[3:-2])):

            # Set limit
            limit = min([len(command[3:-2]), 5]) * 10

            # Check if zac                                                      or me
            if message.author.id == 430382953659367425 or message.author.id == 248410042498285569:
                if (len(message.mentions) > 0):
                    target = message.mentions[0].discriminator
                    deleted = await message.channel.purge(limit=limit, check=(lambda m : m.author.discriminator == target))
                    print(f"Deleted {len(deleted)}")
                    # Set target's name
                    target_name = message.mentions[0].nick if message.mentions[0].nick else message.mentions[0].name
                    await message.channel.send(f":knife: It would seem that Zac has had it with you {target_name}")
                else:
                    deleted = await message.channel.purge(limit=limit, check=(lambda m: True))
                    print(f"Deleted {len(deleted)}")
                    await message.channel.send(f":knife: It would seem that Zac has had it with this conversation.")
            else:
                print("Wait a minute, you aren't Zac. Go be Zac and try again")   
