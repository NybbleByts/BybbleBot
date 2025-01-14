import discord
from discord.ext import commands

class Games(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command(name="hello", description="Say hello to Bybble!")
    async def hello(self, ctx):
        await ctx.respond("Hello there!")

def setup(bot):
    bot.add_cog(Games(bot))