from twitchAPI.twitch import Twitch
from twitchAPI.helper import first

import asyncio
import dotenv
import os

dotenv.load_dotenv()
twitch_client= str(os.getenv("TWITCH_CLIENT"))
twitch_id = str(os.getenv("TWITCH_USERID"))
twitch_secret = str(os.getenv("TWITCH_SECRET"))
twitch_name = str(os.getenv("TWITCH_NAME"))

class TwitchInfo:

    async def twitch_test():
        print("entering twitch test function.")
        twitch = await Twitch(twitch_client, twitch_secret)
        twitchuserID = await first(twitch.get_users(logins=twitch_name))
        await twitch.close()
        return(twitchuserID)
    
    async def calendartwitch():
        twitch = await Twitch(twitch_client, twitch_secret)
        twitchcalendar  = await twitch.get_channel_stream_schedule(broadcaster_id=twitch_id)
        ## twitchuserID = twitchuserID.id 
        await twitch.close()
        return(twitchcalendar)