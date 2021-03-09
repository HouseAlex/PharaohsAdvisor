import discord
from discord.ext import commands

class role(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def getRoles(self, ctx):
        roles = user.roles
        await ctx.send(roles)

def setup(client):
    client.add_cog(role(client))
