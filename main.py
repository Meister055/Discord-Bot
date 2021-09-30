import discord
from discord.ext import commands
import random
import ffmpeg
import os
import sys
import discordtoken
from discordtoken import *


bot = commands.Bot(command_prefix='_')

### Preparing Bot ###
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("with my nuts 🤯"), status=discord.Status.idle)
    print('Ready')



### Bot Commands ###
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)} ms')


@bot.command()
async def clear(ctx, amount=5):
    try:
        float(amount)
    except ValueError:
        await ctx.send(f'Please use a valid number.')
    
    else:
        await ctx.channel.purge(limit=amount)

@bot.command()
async def kick(ctx, member : discord.Member, *, reason='This action was preformed by a bot at the request of a moderator.'):
    await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason='This action was preformed by a bot at the request of a moderator.'):
    await member.ban(reason=reason)

### BOT RUN WITH KEY! DO NOT EDIT ###
bot.run(dtok())