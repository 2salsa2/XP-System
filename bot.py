import os
import json
from dotenv import load_dotenv
import discord
from discord.ext import commands


# load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = commands.Bot(command_prefix='!')


@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")


@bot.event(name="status", help="loads users")
async def status (member):
    with open('discord.members.json',"r") as j:
        users = json.load(j)
        await update_data(users, member)
        with open("discord.member.json", "d") as j:
            json.dump(users, j)

@bot.event(name="message players", help="messages players amount on xp into discord channel")
async def message_p(message):
    with open ("discord.member.json", "r") as j:
        users = json.load(j)
        await update_data(users, message.author)
        await add_xp(users, message.author, 2)
        await level_up(users, message.author, message.channel)
        with open("discord.members.json", "d") as j:
            json.dump(users, j)

@bot.event(name="update", help="updates json file")
async def update_me(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['exp'] = 0
        users[user.id]['level'] = 1

@bot.event(name="adds_exp", help="adds xp to player data")
async def plus_xp(users, user, xp):
    users[user.id]['exp'] += xp

@bot.event(name="level_up", help="everytime you add exp it makes it harder for one to level up")
async def level_up(users, user, channel):
    exp = users[user.id]["exp"]
    start = users[user.id]['level']
    end = int(exp ** (1/8))

    if start < end:
        await client.send_message(channel, "{} has level up congrats you are level {}".format(user.mention, end))
        users[user.id]['level'] = end


bot.run(TOKEN)
