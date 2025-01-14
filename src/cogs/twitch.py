import discord
from discord.ext import commands

from src.twitchconn import TwitchInfo
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first

import nest_asyncio
import asyncio
import dotenv
import os
import icalendar

nest_asyncio.apply()
dotenv.load_dotenv()

twitch_client= str(os.getenv("TWITCH_CLIENT"))
twitch_id = str(os.getenv("TWITCH_USERID"))
twitch_secret = str(os.getenv("TWITCH_SECRET"))


class Twitch(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command(name="twitchid", description="Twitch test!")
    async def twitchall(self, ctx):        
        print("entering twitch info function.")
        twitchID = await TwitchInfo.twitch_test()
        print(twitchID.display_name)
        await ctx.respond(f"twitch id grabbed: {twitchID.display_name} - {twitchID.id}")

    @commands.slash_command(name="twitchcal", description="Twitch calendar test!")
    async def cally(self, ctx):        
        print("entering twitch calendar function.")
        twitchCal = await TwitchInfo.calendartwitch()
        print(twitchCal)
        await ctx.respond(f"twitch calendar grabbed: {twitchCal}")

def setup(bot):
    bot.add_cog(Twitch(bot))



