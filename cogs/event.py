from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension

class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return

def setup(bot):
    bot.add_cog(Event(bot))
