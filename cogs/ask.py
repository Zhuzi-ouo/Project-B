from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import random

class Ask(Cog_Extension):
    
    @commands.command()
    async def ask(self, ctx):
        asktmp = ctx.message.content.split(" ",1)
        if len(asktmp) == 1:
            embed=discord.Embed(title="Error", description="指令錯誤")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=str(asktmp[1]), description=f"{random.randrange(101)}%可能")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Ask(bot))