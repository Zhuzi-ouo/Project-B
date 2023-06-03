from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension

import json

class Snipe(Cog_Extension):
    
    @commands.command()
    async def snipe(self, ctx):
        with open("items\snipe.json") as f:
            snipe=json.load(f)
            if len(snipe["Message"])<=1:
                delmessage = "沒有文字可以狙擊"
                embed=discord.Embed(description=delmessage)
                await ctx.send(embed=embed)
            else:
                delchannel = "訊息來自 "+snipe["Channel"]+""+"訊息時間:"+snipe["SendTime"]
                embed=discord.Embed(description=snipe["Message"])
                embed.set_author(name=snipe["User_Name"],icon_url=snipe["User_Avatar"])
                embed.set_footer(text=delchannel)
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Snipe(bot))