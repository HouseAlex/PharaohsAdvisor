import discord
from discord.ext import commands
import os

#testing out discord commands while messing with my friends
#eventually will make a useful bot once I get the hang of it

client = commands.Bot(command_prefix = '~')

#ready prompt
@client.event
async def on_ready():
    print("Pharaoh's Advisor is logged in")

#admin only bool function
def is_it_admin(ctx):
    return ctx.author.id == 397827519258165269 or ctx.author.id == 181600783043657728

#load commands
@client.command()
@commands.check(is_it_admin)
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')

#unload commands
@client.command()
@commands.check(is_it_admin)
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')

#reload commands
@client.command()
@commands.check(is_it_admin)
async def reload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    client.load_extension(f'Cogs.{extension}')

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')

client.run('ODE3ODAxMjg1NDQ0MzA0OTI2.YEOyzA.tC4y9-cOt1StKFQKS7XyqsDOQtk')
