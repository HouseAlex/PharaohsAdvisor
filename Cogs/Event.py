import discord
from discord.ext import commands
import config

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    add = ":heavy_plus_sign:"
    maybe = ":question:"


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == add:
            await client.send_message(person + "has reacted with " + add)
        if reaction.emoji == maybe:
            await client.send_message(person + "has reacted with " + maybe)

    @commands.command()
    async def event(self, ctx):
        await ctx.send("use and replace info: ~create Event-Name Hour:Min \nin one line seperate Event-Name and time with a space")

    @commands.command()
    async def create(self, ctx, eventName, eventTime):
        eventTime = "at: " + eventTime
        embed = discord.Embed(
            title = eventName,
            description = eventTime
        )

        messageSent = await ctx.send(embed = embed)
        await messageSent.add_reaction(add)
        await messageSent.add_reaction(maybe)



def setup(client):
    client.add_cog(events(client))
