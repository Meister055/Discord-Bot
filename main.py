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
async def kick(ctx, member : discord.Member, *, reason='This action was preformed by a bot at the request of a moderator.'):
    await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason='This action was preformed by a bot at the request of a moderator.'):
    await member.ban(reason=reason)

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

### BOT RUN WITH KEY! DO NOT EDIT ###
if __name__ == '__main__':
    bot.run(dtok())