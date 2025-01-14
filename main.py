from src import BybbleBot

import os
import dotenv

dotenv.load_dotenv()
bybble = BybbleBot()

@bybble.command()
async def ping(ctx):
    await ctx.respond(f'Pong! Bybble ping is: {bybble.latency}')

bybble.load_extension('src.cogs.games')
bybble.load_extension('src.cogs.twitch')

bybble.run(os.getenv("COIN"))