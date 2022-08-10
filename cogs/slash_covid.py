from discord.ext import commands
import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, SlashCommand
from discord_slash.utils.manage_commands import create_choice,create_option
from core.any import Cog_Extension

import requests
from bs4 import BeautifulSoup

class Slash_covid(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
    name="covid",
    description="查詢台灣Covid-19疫情狀況")
    async def _covid(self, ctx: SlashContext):
        response=requests.get("https://www.worldometers.info/coronavirus/country/taiwan/")
        soup=BeautifulSoup(response.text,"html.parser")
        result=soup.find_all("div",attrs={"class":"maincounter-number"})
        msglist=["病例總數",
                "死亡人數",
                "康復人數"]
        listnum=0
        embed=discord.Embed(title="Covid-19疫情資訊", description="臺灣目前疫情狀況")
        for covid in result:
            covid[listnum]=covid.text
            embed.add_field(name=msglist[listnum], value=covid.text, inline=False)
            listnum=listnum+1
        embed.set_footer(text="請各位確實戴好口罩，可有效避免飛沫傳染，若口罩沒戴確實，甚至沒帶，不僅嚴重增加飛沫傳染機率，還可處3000~15000罰緩。")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Slash_covid(bot))