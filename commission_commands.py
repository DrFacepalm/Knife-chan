# Knife-chan discord bot, bot for personal moderation of
# a discord server during the bot wars.
# Commission commands for the bot
# Author: Lucas Lin

import discord

####################################################
# COMISSIONED COMMAND ##############################
# COMMISSIONED BY Zachaccino:430382953659367425 ###
# PURRRGE: purges based on amount of Rs in command #
# without argument, purges X jayden, with ##########
# singular mention, purges X if specified user #####
# 'all; case insensitive purges indiscrimiately ####
####################################################
async def _process_PURRRGE(message):
    
    # Check command
    if (message.content.startswith('!PUR')):
        msg_list = message.content.split(" ")
        command = msg_list[0]

        # Check command
        if (command.endswith('GE') and command[3:-2] == "R"*len(command[3:-2])):

            # Set limit
            limit = min([len(command[3:-2]), 20])

            # Check if zac                                                      or me
            if message.author.id == 430382953659367425 or message.author.id == 248410042498285569:
                if (len(message.mentions) > 0):
                    target = message.mentions[0].discriminator
                    deleted = await message.channel.purge(limit=limit, check=(lambda m : m.author.discriminator == target))
                    print(f"Deleted {len(deleted)}")
                    # Set target's name
                    target_name = message.mentions[0].nick if message.mentions[0].nick else message.mentions[0].name
                    await message.channel.send(f":knife: It would seem that Zac has had it with you {target_name}")
                elif (len(msg_list) > 1):
                    if msg_list[1].lower() == "all":
                        deleted = await message.channel.purge(limit=limit, check=(lambda m: True))
                        print(f"Deleted {len(deleted)}")
                        await message.channel.send(f":knife: It would seem that Zac has had it with this conversation")
                else:
                    # does jayden's bot
                    target = 698107749166219284
                    deleted = await message.channel.purge(limit=limit, check=(lambda m: m.author.discriminator == target))
                    print(f"Deleted {len(deleted)}")
                    await message.channel.send(f":knife: It would seem that Zac has had it with you Jayden.")
            else:
                await message.channel.send("Wait a minute, you aren't Zac. Go be Zac and try again.\nThis incident has been reported to Administration.")   
