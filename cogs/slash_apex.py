from discord.ext import commands
import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, SlashCommand
from discord_slash.utils.manage_commands import create_choice,create_option
from core.any import Cog_Extension

import requests
from bs4 import BeautifulSoup

class slash_apex(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
    name="apex",
    description="查詢Apex戰績",
    options=[
        create_option(
            name="platform",
            description="選擇你的平台",
            required=True,
            option_type=3,
            choices=[
                create_choice(
                    name="Origin",
                    value="PC"
                ),
                create_choice(
                    name="Xbox",
                    value="X1"
                ),
                create_choice(
                    name="PlayStation",
                    value="PS4"
                )
            ]
        ),
        create_option(
            name="user",
            description="輸入你的Origin名稱",
            required=True,
            option_type=3 #6是使用者 3是隨意填
            )
        ]
    )
    async def _apex(self, ctx: SlashContext, platform, user):
        def AT(Platform,User):
            response=requests.get(f"https://api.jumpmaster.xyz/user/Stats?platform={Platform}&player={User}").json()
            global AT_Username, AT_Platform, AT_Level, AT_Rank_BR, AT_Rank_BR_Name, AT_Rank_AR, AT_Rank_AR_Name
            AT_Username=response["user"]["username"]
            AT_Platform=response["user"]["platform"]
            AT_Level=response["account"]["level"]
            AT_Rank_BR=response["ranked"]["BR"]["score"]
            AT_Rank_BR_Name=response["ranked"]["BR"]["name"]
            AT_Rank_AR=response["ranked"]["Arenas"]["score"]
            AT_Rank_AR_Name=response["ranked"]["Arenas"]["name"]

        embed=discord.Embed(description=f"正在搜尋 {user} 的數據")
        message=await ctx.send(embed=embed)
        try:
            AT(platform,user)
            embed=discord.Embed(title=AT_Username)
            embed.add_field(name="等級", value=AT_Level, inline=True)
            embed.add_field(name="平台", value=AT_Platform, inline=True)
            embed.add_field(name="大逃殺積分", value=f"{AT_Rank_BR_Name}\n{AT_Rank_BR}", inline=False)
            embed.add_field(name="競技場積分", value=f"{AT_Rank_AR_Name}\n{AT_Rank_AR}", inline=False)
            await message.edit(embed=embed)
        except:
            embed=discord.Embed(title="Error", description="此玩家ID不存在")
            await message.edit(embed=embed)

def setup(bot):
    bot.add_cog(slash_apex(bot))