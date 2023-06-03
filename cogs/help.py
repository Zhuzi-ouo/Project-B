from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension

class Help(Cog_Extension):
    
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="關於機器人指令", description="使用 -help")
        embed.add_field(name="-gay", value="你有多甲", inline=False)
        embed.add_field(name="-say", value="讓機器人說句話", inline=False)
        embed.add_field(name="-ask", value="這件事有多大機率發生", inline=False)
        embed.add_field(name="-info", value="機器人資訊", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))