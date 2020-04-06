import os
import json
from dotenv import load_dotenv
import discord
from discord.ext import commands


#load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
client = commands.Bot(command_prefix='!')


@client.listen()
async def on_ready():
    print('Bot loaded and ready!')

@client.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")


@client.event
async def status (member):
    with open('package.json',"r") as j:
        users = json.load(j)
        await update_me(users, member)
        with open("package.json", "w") as j:
            json.dump(users, j)

@client.event
async def message_p(message):
    with open ("package.json", "r") as j:
        users = json.load(j)
        await update_me(users, message.author)

        await plus_xp(users, message.author, 2)
        await level_up(users, message.author, message.channel)
        with open("package.json", "w") as j:
            json.dump(users, j)


async def update_me(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['exp'] = 0
        users[user.id]['level'] = 1


async def plus_xp(users, user, xp):
    users[user.id]['exp'] += xp


async def level_up(users, user, channel):
    exp = users[user.id]["exp"]
    start = users[user.id]['level']
    end = int(exp ** (1/8))

    if start < end:
        await client.send_message(channel, "{} has level up congrats you are level {}".format(user.mention, end))
        users[user.id]['level'] = end


client.run(TOKEN)
