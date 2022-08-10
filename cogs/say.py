from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension

class Say(Cog_Extension):
    
    @commands.command()
    async def say(self, ctx, msg):
        AllowedMentions = discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False)
        await ctx.message.delete()
        await ctx.send(msg, allowed_mentions=AllowedMentions)

def setup(bot):
    bot.add_cog(Say(bot))