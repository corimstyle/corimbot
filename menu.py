import aiohttp
import discord
import re

from bs4 import BeautifulSoup


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            return await r.text()


async def get_menu():
    r = await fetch("https://menus.calpolycorporation.org/805kitchen/")
    soup = BeautifulSoup(r, 'html.parser')
    embed = discord.Embed(title='805 Kitchen Menu')
    lst = []
    fname = ''
    fval = ''
    current_embed_empty = True
    for s in soup.find_all('h3'):
        if s.get_text() != 'Legend':
            embed.description = s.get_text()
    lst.append(embed)
    embed = discord.Embed(title='')
    embed_length = 0
    num_fields = 0
    for s in soup.find_all(['h2', 'h4', 'p']):
        premsg = s.get_text()
        premsg = premsg.replace('\t', '')
        premsg = re.sub('\n+', '', premsg)
        premsg = premsg.strip()
        if s.name == 'h2':
            if len(embed.title) > 0:
                if not current_embed_empty:
                    lst.append(embed)
                embed_length = 0
                embed = discord.Embed(title='')
                current_embed_empty = True
            embed.title = '**' + premsg + '**'
            embed_length += len(premsg) + 4
        elif s.name == 'h4':
            if len(fname) > 0:
                if len(fval) == 0:
                    fval += '[empty]'
                else:
                    current_embed_empty = False
                embed_length += len(fname) + len(fval)
                embed.add_field(name=fname, value=fval, inline=False)
                fval = ''
            fname = premsg
        elif s.name == 'p':
            if (len(fval) + len(premsg) + 64 > 1024):
                embed.add_field(name=fname, value=fval, inline=False)
                fval = ''
                fname = '--'
            for img in s.find_all('img'):
                if img['alt'] == 'Vegetarian':
                    premsg += ' <:vegetarian:499693084117041153>'
                if img['alt'] == 'Vegan':
                    premsg += ' <:vegan:499693108825554945>'
            fval += premsg + '\n'
        if embed_length + len(fname) + len(fval) > 5500 or len(embed.fields) > 23:
            # Add current embed to list and start a new one
            if not current_embed_empty:
                lst.append(embed)
            embed = discord.embed(title='')
            embed_length = 0
            current_embed_empty = True
    if len(fname) > 0:
        if len(fval) == 0:
            fval += '[empty]'
        embed.add_field(name=fname, value=fval, inline=False)
    if not current_embed_empty:
        lst.append(embed)
    return lst

