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

class Slash_eat(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
    name="eat",
    description="讓機器人幫你選食物")
    async def _eat(self, ctx):
        eatlist=["你應該要吃正太",
                 "你應該要吃ㄌㄌ",
                 "你應該要吃好市多麻辣鍋",
                 "你應該要吃炒飯",
                 "你應該要吃拉麵",
                 "你應該要吃麥當勞",
                 "你應該要吃新疆棉花",
                 "你應該要吃壽司",
                 "建議不要吃東西",
                 "你應該要吃TSJ薯餅",
                 "你應該要吃牛排",
                 "你應該要吃馬鈴薯燉肉",
                 "你應該要ㄔㄐㄐ"]
        await ctx.send(random.choice(eatlist))

def setup(bot):
    bot.add_cog(Slash_eat(bot))