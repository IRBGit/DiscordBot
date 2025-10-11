import random
import datetime
from datetime import timedelta
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("Set DISCORD_BOT_TOKEN environment variable first.")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="_", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (id={bot.user.id})")
    activity = discord.Streaming(name='my execution', url='https://twitch.tv')
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event
async def on_reaction_add(reaction: discord.Reaction, user):
    if user.bot:
        return
    try:
        await reaction.message.add_reaction(reaction.emoji)
    except discord.HTTPException:
        pass

# activates on every message the bot can see
@bot.event
async def on_message(message: discord.Message):
    # Ignore bots
    if message.author.bot:
        return
    #await message.author.voice.channel.connect() (working)
    if random.randint(1, 10) == 1:

        #Alex
        if message.author.id == 469252577326792704:
            await message.channel.send("Hey Twiddly")
            await message.author.timeout(datetime.timedelta(seconds=1))
            
        #Ian
        if message.author.id == 431111804157034496:
            await message.channel.send("Hey Corn Boy")
        #Adam
        if message.author.id == 424316398886715425:
            await message.channel.send("Hey Ham Boy")
        #Aaron
        if message.author.id == 349354952961032192:
            await message.channel.send("Hey piggy")
            if random.randint(1, 100000) == 1:
                await message.author.timeout(datetime.timedelta(weeks=3, days=6, hours=23, minutes=59, seconds=59))
        
    # Allow other commands to still work
    await bot.process_commands(message)

#Simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

#simple hello command
@bot.command()
async def hello(ctx):
    await ctx.typing()
    await ctx.send(f"Hello {ctx.author.mention}!")

#join voice channel command
@bot.command()
async def join(ctx):
    await ctx.author.voice.channel.connect()

#annoy the shit out of alex command
@bot.command()
async def ping_alex(ctx):
    for i in range(100):
        await ctx.typing()
        await ctx.send("<@469252577326792704>")

#leave voice channel command (not working)
# @bot.command()
# async def leave(ctx):
#     await ctx.voice_client.disconnect()

bot.run(TOKEN)