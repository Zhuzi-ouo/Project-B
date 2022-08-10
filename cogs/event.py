from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension

class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return

        if msg.content == "領域":
            await msg.channel.send("好好聊，或者道歉，不是炎上给你一天，时间选择一")

        if msg.content == "殺人":
            await msg.channel.send("這是領域的專長")

        if msg.content == "!tank":
            await msg.channel.send("我之前是在天安門開坦克的，而我輾人的原則是\n「幹你娘輾爆」\n沒錯，就是幹你娘輾爆，老子才不管甚麼人權三小的，每次輾的學生就是姬芭一大堆。一個人輾成三個，二個人輾成六個。大學生買一送一，跟把整個解放軍基地的坦克全壓在你身上沒兩樣。\n我還記得，我那個月上班25天，主席跑來跟我說，這個月履帶虧損二十六條，你有頭緒嗎？\n我他媽的怎麼會知道。")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 863269145981222942:
            channel = member.guild.system_channel
            embed=discord.Embed(description=f"嗨 {member.mention} 歡迎加入問號社(´･ω･`)?\n快來和大家一起聊天吧",color=0x4DFFFF)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863276193499054120/909041563890483260/bf40165f63bf72d6.png")
            await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 863269145981222942:
            channel = member.guild.system_channel
            embed=discord.Embed(description=f"{member.mention} 離開了伺服器qwq",color=0x4DFFFF)
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Event(bot))