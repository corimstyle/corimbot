import random

from discord.ext import commands
from bot_token import bot_token
from thanos_quotes import thanos_quotes

bot = commands.Bot(command_prefix='!corim ')


@bot.command(name='ping')
async def pong(ctx):
    await ctx.send("Pong")


@bot.command(name='win')
async def win(ctx):
    await ctx.send("I see this as an absolute win!")


@bot.command(name='thanos')
async def thanos(ctx):
    quote_num = random.randint(0, len(thanos_quotes) - 1)
    quote = thanos_quotes[quote_num]
    await ctx.send(quote)


@bot.command(name='flip')
async def flip(ctx):
    await ctx.send("I'm flipping a coin...")
    side = random.randint(0, 1)
    if side == 0:
        await ctx.send("The coin landed on heads!")
    else:
        await ctx.send("Looks like it\'s tails!")


@bot.command(name='snap')
async def snap(ctx):
    users = ctx.guild.members
    display_names = [user.display_name for user in users]
    print(type(display_names))
    random.shuffle(display_names)
    snapped = display_names[:len(display_names) // 2]
    survived = display_names[len(display_names) // 2:]
    await ctx.send("Snapped: " + ", ".join(snapped) + "\r\n")
    await ctx.send("Survived: " + ", ".join(survived) + "\r\n")


bot.run(bot_token)
