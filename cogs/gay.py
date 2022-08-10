from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import random

class Gay(Cog_Extension):
    
    @commands.command()
    async def gay(self, ctx):
        ran = random.randrange(101)
        embed=discord.Embed(title=" ", description=f"{ran}% Gay")
        embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Gay(bot))