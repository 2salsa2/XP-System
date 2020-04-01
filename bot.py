import os
import json
from dotenv import load_dotenv
import discord
from discord.ext import commands



load_dotenv()
TOKEN = os.getenv('DISCORD TOKEN')
bot = commands.Bot(command_prefix='!')
os.chdir(r"C:\Users\khali\github\XP-System")

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")


@clinet.event
async def status (member):
    with open('discord.members.json',"r") as j:
        users = json.load(j)

        await update_data(users, member)

        with open("discord.member.json", "d") as j:
            json.dump(users, j)

@clinet.event
async def message_p(message):
    with open ("discord.member.json", "r") as j:
        users = json.load(j)

        await update_data(users, message.author)
        await add_xp(users, mmessage.author, 2)
        await level_up(users, message.author, message.channel)

        with open("discord.members.json", "d") as j:
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
        await clinet.send_message(channel, "{} has level up congrats you are level {}".format(user.mention, end))
        users[user.id]['level'] = end
        
bot.run(TOKEN)
