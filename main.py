#imports
import discord, re, json, datetime, base64, traceback
from discord.ext import commands
from discord import Embed, app_commands, message
from typing import Optional, Literal
import aiosqlite as sql
from datetime import datetime
import asyncio, random
import os

#variables
BOT_TOKEN = "MTQ2MDg0NzM1ODY1NjExODgyNw.GjiAkX.dnuDN7faeyjL3HOQpbMntShlBDnTAcjRM2GWa4"
bot = commands.Bot(command_prefix="A!", intents = discord.Intents.all())
CHANNEL_ID = 1460845666434547752
Message = discord.Message
author = discord.Message.author or Message.author
guild = message.Guild.id



@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        for command in synced:
            bot.tree._global_commands[command.name].id = command.id
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    print("Hello there! Im ready to handle commands!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Separating heaven and hell.")

@bot.command(name="guilds", help="Shows all guilds the bot is in")
async def guilds(ctx):
    if ctx.author.id == 940337920009699340:
        guild_info_lines = []
        embed = discord.Embed(
            title=f"{bot.user.name} Guilds",
            color=discord.Color.blue()
        )

        for g in bot.guilds:
            created_at = g.created_at.strftime("%Y-%m-%d %H:%M:%S")
            line = (
                f"{g.name} -- {g.id}\n"
                f"- Owner: {g.owner}\n"
                f"- Member Count: {g.member_count}\n"
                f"- Created At: {created_at}\n"
            )
            guild_info_lines.append(line)

        # Put first few guilds in the embed (Discord embeds have character limits)
        description = "\n".join(guild_info_lines[:5])  # show only first 5 in the embed
        embed.description = description or "No guilds found."

        # Save everything into a txt file
        file_content = "\n".join(guild_info_lines)
        with open("guilds.txt", "w", encoding="utf-8") as f:
            f.write(file_content)

        file = discord.File("guilds.txt", filename="guilds.txt")

        await ctx.send(embed=embed, file=file)

async def load():
    for filename in os.listdir("./Cogs"):
        if filename.endswith('.py') and filename != 'functions.py':
            await bot.load_extension(f'Cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(BOT_TOKEN)
        #print('done')

asyncio.run(main())