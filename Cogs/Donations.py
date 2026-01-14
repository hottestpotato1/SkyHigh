import discord
from discord import app_commands
from discord.ext import commands
import typing
from typing import Any, Dict, List, Optional
import regex
Choice = app_commands.Choice

class Donations(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is ready.")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 270904126974590976:
            print(f"dank memer sent a message in {message.channel.id}")
            await message.channel.send(content=f"{message.content}, {message.components}", embeds=message.embeds)
            print(message.components)
            

async def setup(bot):
    await bot.add_cog(Donations(bot))