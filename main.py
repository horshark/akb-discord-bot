import os
import json

import discord
from discord.ext import commands
from attackerkb_api import AttackerKB

import utils.printer as printer

# Strings and config.
queryMaxTopics = 5
error = "Sorry, I could not find anything for this {}!"

token = os.environ.get('DISCORD_TOKEN')
api_key = os.environ.get('AKB_API_KEY')

if token == None or api_key == None:
    # if enviroment variables have not been set
    # stop execution
    print("DISCORD_TOKEN or AKB_API_KEY enviroment variables have not been set")
    exit(1)

# Setting up the bot and prefix.
prefix = "!akb "
bot = commands.Bot(command_prefix=prefix)

# Loads the bot's activity status.
status = prefix+"help"

# AKB api.
api = AttackerKB(api_key)

# Logging the starting of the bot into the console.
@bot.event
async def on_ready():
    # Sets activity message.
    await bot.change_presence(activity=discord.Game(status))

    # Removes default help command.
    print("\nLogged in as {0.user}".format(bot)+"\n")


# Commands.
## Ping command.
@bot.command(description="Ping the bot.")
async def ping(ctx):
    await ctx.send("Pong!")

## Topic command.
@bot.command(description="Get a topic.")
async def topic(ctx, id):
    try:
        query = api.get_single_topic(id)
        message = printer.topic(query)
    except:
        message = printer.not_found(error.format("topic"))

    await ctx.send(embed=message)

## Assessment command.
@bot.command(description="Get an assessment.")
async def assessment(ctx, id):
    try:
        query = api.get_single_assessment(id)

        author_name = api.get_single_contributor(query["editorId"])["username"]
        topic_name = api.get_single_topic(query["topicId"])["name"][:15]

        message = printer.assessment(query, author_name, topic_name)
    except:
        message = printer.not_found(error.format("assessment"))

    await ctx.send(embed=message)

## CVE command.
@bot.command(description="Get a CVE.")
async def cve(ctx, id):
    try:
        query = api.get_topics(name=id)
        message = printer.topic(query[0])
    except:
        message = printer.not_found(error.format("CVE"))

    await ctx.send(embed=message)

## User command.
@bot.command(description="Get a user.")
async def user(ctx, id):
    try:
        query = api.get_single_contributor(id)
        message = printer.user(query)
    except:
        message = printer.not_found(error.format("user"))
    
    await ctx.send(embed=message)

## Query command.
@bot.command(description="Query for topics.")
async def query(ctx, *, keywords):
    try:
        query = api.get_topics(q=keywords, size=queryMaxTopics)
        message = printer.topic_list(keywords, query, queryMaxTopics)
    except:
        message = printer.not_found(error.format("query"))

    await ctx.send(embed=message)

# Starting the bot.
bot.run(token)