import discord
from discord.ext import commands
from mcstatus import MinecraftServer

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def mcstatus(ctx, ip: str):
    try:
        server = MinecraftServer.lookup(ip)
        status = server.status()

        embed = discord.Embed(
            title="🟢 Minecraft Server Online",
            color=discord.Color.green()
        )
        embed.add_field(name="IP", value=ip, inline=False)
        embed.add_field(name="Players", value=f"{status.players.online}/{status.players.max}", inline=True)
        embed.add_field(name="Version", value=status.version.name, inline=True)
        embed.add_field(name="MOTD", value=status.description, inline=False)

    except Exception:
        embed = discord.Embed(
            title="🔴 Server Offline or Invalid",
            description=f"Could not connect to `{ip}`.",
            color=discord.Color.red()
        )

    await ctx.send(embed=embed)

# Read bot token from environment variable
import os
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)
