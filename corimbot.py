import random
import discord
import re
import osu
import os
import menu
import weather

from discord.ext import commands
from urllib.parse import urlparse

# from bot_token import bot_token // No longer needed
from thanos_quotes import thanos_quotes

bot = commands.Bot(command_prefix="!corim ")
bot_token = os.environ.get("DISCORD_BOT_TOKEN")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "bruh":
        await message.channel.send("Bruh")

    if "osu.ppy.sh/u" in message.content or "osu.ppy.sh/users" in message.content:
        urls = re.findall(
            "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            message.content,
        )
        user_url = urls[0]
        user_path = urlparse(user_url).path
        if "user" not in user_path:
            user_id = user_path[3:]
        else:
            user_id = user_path[7:]
        user_info = osu.get_user_info(user_id)
        embed = discord.Embed(
            title="{0}'s profile".format(user_info["username"]),
            url=user_url,
            description="osu!",
            color=0x80FFFF,
        )
        embed.add_field(name="Country", value=user_info["country"], inline=False)
        embed.add_field(name="pp", value=user_info["pp_raw"], inline=False)
        embed.add_field(name="Global Ranking", value=user_info["pp_rank"], inline=False)
        embed.add_field(
            name="Country Ranking", value=user_info["pp_country_rank"], inline=False
        )
        embed.add_field(
            name="Accuracy", value="{0}%".format(round(float(user_info["accuracy"]), 2))
        )
        await message.channel.send(embed=embed)

    await bot.process_commands(message)


@bot.command(name="ping")
async def pong(ctx):
    await ctx.send("Pong")


@bot.command(name="win")
async def win(ctx):
    await ctx.send("I see this as an absolute win!")


@bot.command(name="thanos")
async def thanos(ctx):
    quote_num = random.randint(0, len(thanos_quotes) - 1)
    quote = thanos_quotes[quote_num]
    await ctx.send(quote)


@bot.command(name="flip")
async def flip(ctx):
    await ctx.send("I'm flipping a coin...")
    side = random.randint(0, 1)
    if side == 0:
        await ctx.send("The coin landed on heads!")
    else:
        await ctx.send("Looks like it's tails!")


@bot.command(name="snap")
async def snap(ctx):
    users = ctx.guild.members
    display_names = [
        user.display_name for user in users if user.display_name != "Corimbot"
    ]
    random.shuffle(display_names)
    snapped = display_names[: len(display_names) // 2]
    survived = display_names[len(display_names) // 2:]
    embed = discord.Embed(title="Thanos snap", description="", color=0x80FFFF)
    embed.add_field(name="Snapped", value=(", ".join(snapped) + "\r\n"), inline=False)
    embed.add_field(name="Survived", value=(", ".join(survived) + "\r\n"), inline=False)
    await ctx.send(embed=embed)


@bot.command(name="805")
async def menu_805(ctx):
    menu_list = await menu.get_menu()
    for emb in menu_list:
        await ctx.send(embed=emb)


@bot.command(name="weather")
async def get_weather(ctx, *args):
    pass


bot.run(bot_token)
