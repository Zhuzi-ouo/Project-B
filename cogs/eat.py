from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import random

class Eat(Cog_Extension):
    
    @commands.command()
    async def eat(self, ctx):
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
    bot.add_cog(Eat(bot))