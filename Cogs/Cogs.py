import discord
from discord import app_commands
from discord.ext import commands
import os

class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.default_permissions(administrator=True)
    async def reload(self, interaction: discord.Interaction, extension: str = None):
        """Reloads a specific cog or all cogs."""
        if extension:
            extension = extension.capitalize()
            try:
                await self.bot.reload_extension(f"Cogs.{extension}")
                await interaction.response.send_message(f"✅ Reloaded `{extension}` cog!")
            except Exception as e:
                await interaction.response.send_message(f"❌ Failed to reload `{extension}`: `{e}`")
        else:
            # Reload all cogs
            reloaded = []
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py") and filename != "Functions.py":
                    name = filename[:-3]
                    try:
                        await self.bot.reload_extension(f"Cogs.{name}")
                        reloaded.append(name)
                    except Exception as e:
                        await interaction.response.send_message(f"❌ Failed to reload `{name}`: `{e}`")
            await interaction.response.send_message(f"🔄 Reloaded all cogs: {', '.join(reloaded)}")

async def setup(bot):
    await bot.add_cog(Cogs(bot))
