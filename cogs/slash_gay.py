from discord.ext import commands
import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, SlashCommand
from discord_slash.utils.manage_commands import create_choice,create_option
from core.any import Cog_Extension
import random

import requests
from bs4 import BeautifulSoup

class Slash_gay(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
    name="gay",
    description="測試你Gay的機率")
    async def _gay(self, ctx):
        ran = random.randrange(101)
        url=ctx.author.avatar_url
        embed=discord.Embed(title=" ", description=f"{ran}% Gay")
        embed.set_author(name=ctx.author,icon_url=url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Slash_gay(bot))