# Knife-Chan :knife:

This is a discord bot written using the discord.py library for personal use, but feel free to take parts of it for your own work.
This bot was created during the bot-wars period where other members had created discord bots with potential for mass destruction. This bot was created as a means to mitigate that damage.

# Hosting

My instance of this bot is being hosted on Heroku. To host it yourself, download the source code, upload it to a Heroku instance and set an environment variable: 
`BOT_TOKEN` = `<TOKEN>`

## Development branches

### Beta

- This version of the bot is for small scale testing of functionality. I run this one on my local machine on a private server to test and develop small functions quickly 

### Staging

- This version of the bot is for implementing beta functionality into the final bot. A version of this is usually hosted on a private server and is used to test the final implementation and iron out any issues. Once this is done, this version is merged up to the master branch and the bot is rehosted automatically. 

## Features implemented (or semi-implemented)

- Purging messages with smart detection of messages to delete
- Image rotation (plans to autodetect when images are sideways and rotate them)
- Webscraper for GeekHack.com to find groupbuys.