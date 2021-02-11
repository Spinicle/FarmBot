# CONFIG
prefix = "|" # Change your prefix here.

import asyncio
from discord.ext import commands
import discord
import random
import re
import json
from colorama import Fore, Back, Style, init
import shutil
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Farm Bot v1.0 by Spinicle")
init(autoreset=True)
print(Fore.CYAN + Style.BRIGHT + """


 ▄▀▀▀█▄    ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▄▀▄      ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀█▀▀▄ 
█  ▄▀  ▀▄ ▐ ▄▀ ▀▄ █   █   █ █  █ ▀  █     ▐ ▄▀   █ █      █ █    █  ▐ 
▐ █▄▄▄▄     █▄▄▄█ ▐  █▀▀█▀  ▐  █    █       █▄▄▄▀  █      █ ▐   █     
 █    ▐    ▄▀   █  ▄▀    █    █    █        █   █  ▀▄    ▄▀    █      
 █        █   ▄▀  █     █   ▄▀   ▄▀        ▄▀▄▄▄▀    ▀▀▀▀    ▄▀       
█         ▐   ▐   ▐     ▐   █    █        █    ▐            █         
▐                           ▐    ▐        ▐                 ▐         

""")

print(Fore.CYAN +"-------------------------\n" + Fore.RED + "# " + Fore.BLUE + "Created by Spinicle   |\n" + Fore.RED + "# " + Fore.BLUE + "Farm Bot v1.0         |\n" + Fore.RED + "# " + Fore.BLUE + "Loading bot..         |\n" + Fore.CYAN + "-------------------------")

with open('config.json') as config_file:
    data = json.load(config_file)

token = data['TOKEN']
prefix = data['PREFIX']

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(Fore.CYAN + Style.BRIGHT + f"Connected as {bot.user.name} and ready on {len(bot.guilds)} servers!")
    print()
    print(Fore.RED + "Do NOT run more than one command at once as discord may ratelimit you.")
    print(Fore.RED + "To terminate a command close this program.")
    print()
    print(Fore.CYAN + Style.BRIGHT + "OwO Bot" + Fore.CYAN + " - |pray - Executes the 'owo pray' command.")
    print(Fore.CYAN + Style.BRIGHT + "Arcane" + Fore.CYAN + " - |arcane - Sends a message every 60 seconds to level up.")
    print(Fore.CYAN + Style.BRIGHT + "Mee6" + Fore.CYAN + " - |mee6 - Sends a message every 60-65 seconds to level up.")
    print(Fore.CYAN + Style.BRIGHT + "Disboard" + Fore.CYAN + "- |bump - Bumps the server every 2 hours.")
    print()
    ctypes.windll.kernel32.SetConsoleTitleW(f"Farm Bot v1.0 by Spinicle | Logged in as {bot.user.name}")

print()

@bot.command(pass_context=True)
async def pray(ctx, amount=100):
    await ctx.message.delete()
    print(f"{bot.user.name} is praying in {ctx.message.guild.name}")
    for r in range(amount):
        message = await ctx.send("owo pray")
        await asyncio.sleep(random.uniform(300,330))

@bot.command(pass_context=True)
async def arcane(ctx, amount=33500):
	await ctx.message.delete()
	print(f"{bot.user.name} is leveling up in Arcane in the server {ctx.message.guild.name}")
	for r in range(amount):
		message = await ctx.send(".")
		await asyncio.sleep(random.uniform(60, 62))

@bot.command(pass_context=True)
async def mee6(ctx, amount=10000):
	await ctx.message.delete()
	print(f"{bot.user.name} is leveling up in Mee6 in the server {ctx.message.guild.name}")
	for r in range(amount):
		message = await ctx.send(".")
		await asyncio.sleep(random.uniform(60, 62))

@bot.command(pass_context=True)
async def bump(ctx, amount=100):
	await ctx.message.delete()
	print(f"{bot.user.name} is bumping the server {ctx.message.guild.name}")
	for r in range(amount):
		message = await ctx.send("!d bump")
		await asyncio.sleep(random.uniform(7200, 7210))

bot.run(token, bot=False)
