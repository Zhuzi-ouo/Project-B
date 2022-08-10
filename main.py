import os
import discord
from discord import message
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice,create_option

import json
import time
import datetime
from datetime import datetime, timezone, timedelta
import requests
from bs4 import BeautifulSoup

intents = discord.Intents().all()
client = commands.Bot(command_prefix="-", owner_ids = [使用者ID], intents=intents)
slash = SlashCommand(client, sync_commands=True)
client.remove_command("help")

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"cogs.{name}")

@client.event
async def on_ready():
    print(str(datetime.utcnow().astimezone(timezone(timedelta(hours=16)))).split(".",1)[0],"機器人已啟動",client.user)

async def on_command_error(ctx, error):
    return

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"已成功載入 {extension} 套件")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'已成功卸載 {extension} 套件')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.send(f'已重新載入 {extension} 套件')

@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency*100000)/100}ms")

@client.command()
async def info(ctx):
    embed=discord.Embed(title="Project B")
    embed.add_field(name="Version", value="1.0", inline=True)
    embed.set_footer(text="In development")
    await ctx.send(embed=embed)

with open('token.json', "r") as file:
    data = json.load(file)
client.run(data['token'])
