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






bot.run(TOKEN)
