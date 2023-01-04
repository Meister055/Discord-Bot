import discord
from discord.ext import commands
import random
import ffmpeg
import os
import sys
from discordtoken import dtok

### Bot Setup ###
description = 'A bot that does stuff'

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='_', description=description, intents=intents)

### Preparing Bot ###
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("with my nuts 🤯"), status=discord.Status.idle)
    print(f'Bot is ready to run commands!\n----------')



### Bot Commands ###
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)} ms')
    print(f'Pong! {round(bot.latency * 1000)} ms')


@bot.command()
async def clear(ctx, amount=5):
    try:
        float(amount)
    except ValueError:
        await ctx.send(f'Please use a valid number.')
    
    else:
        await ctx.channel.purge(limit=amount)

@bot.command()
async def kick(ctx, member : discord.Member, *, reason='This action was preformed by a bot at the request of a moderator.',):
    content=f'You have been kicked from the server with the reason of "{reason}".'
    await member.kick(reason=reason)
    print(f'Kicked {member} for {reason}.')
    channel = await member.create_dm()
    await channel.send(content)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason='This action was preformed by a bot at the request of a moderator.'):
    content=f'You have been banned from the server with the reason of "{reason}".'
    await member.ban(reason=reason)
    print(f'Banned {member} for {reason}.')
    channel = await member.create_dm()
    await channel.send(content)

@bot.command()
async def unban(ctx, *, id: int):
    content = f'You have been unbanned from {ctx.guild.name}.'
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f'Unbanned {user}.')
    print(f'Unbanned {user}.')
    channel = await user.create_dm()
    await channel.send(content)

@bot.command()
async def nono(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    await discord.VoiceClient.play(discord.FFmpegPCMAudio('./assets/nono.mp3'))
    await discord.VoiceClient.disconnect()
    
@bot.command()
async def disconnect(ctx):
    await discord.VoiceClient.disconnect()



### BOT RUN WITH KEY! DO NOT EDIT ###
if __name__ == '__main__':
    bot.run(dtok())