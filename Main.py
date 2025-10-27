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

#Events
#-----------------------------------------------------------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (id={bot.user.id})")
    activity = discord.Streaming(name='my execution', url='https://twitch.tv')
    await bot.change_presence(status=discord.Status.online, activity=activity)
    # for guild in bot.guilds:
    #     for channel in guild.text_channels:
    #             await channel.send("Bot is now online!")

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

#Harass people who are typing
@bot.event
async def on_typing(channel:discord.TextChannel, user:discord.User, when: datetime.datetime):
    if user.bot:
        return
    else:
        if random.randint(1, 100) == 1:
            await channel.typing()
            await channel.send(f"Hey {user.mention}, nobody cares!")

#commands
#-----------------------------------------------------------------
#Simple ping command
@bot.command(name="ping")
async def ping(message: discord.Message):
    await message.channel.send(f"Pong! {round(bot.latency * 1000)}ms")

#simple hello command
@bot.command(name="hello")
async def hello(message: discord.Message):
    await message.channel.typing()
    await message.channel.send(f"Hello {message.author.mention}!")

#annoy the shit out of alex command
@bot.command(name="ping_alex")
async def ping_alex(message: discord.Message):
    for i in range(100):
        await message.channel.typing()
        await message.channel.send("<@469252577326792704>")

#join voice channel command
@bot.command(name="join")
async def join(message: discord.Message):
    await discord.VoiceChannel.connect(message.author.voice.channel, reconnect=True)

#leave voice channel command (not working)
@bot.command(name="leave")
async def leave(message: discord.Message):
    await message.author.voice.channel.disconnect()

# @bot.command(name="play")
# async def play(message: discord.Message):


bot.run(TOKEN)