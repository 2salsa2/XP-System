import os
import json
from dotenv import load_dotenv
import discord
from discord.ext import commands

git config --global user.email "sksky217@gmail.com"
git config --global user.name "2salsa2"

load_dotenv()
TOKEN = os.getenv('Njg2NzI3ODAzNjQyNTc2OTQx.XnvNHg.xhtb8tm5uRvcJrZyHoUx-SOTX28')
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
        members = json.load(j)

        


bot.run(TOKEN)
