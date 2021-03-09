import discord
from discord.ext import commands
import random

insults = [
  "You dumb bitch",
  "Rat lookin ass",
  "شرموطة",
  "Quite cringe innit",
  "Baby Rage",
  "You have gone back to monke, but you've gone to far. Too much monke",
  "Bronze",
  "you suck almost as much as Mahmoud"
  "Silence wench"
]

advices = [
  "Maybe try heading North",
  "Get good loser",
  "Try turning on your monitor",
  "This is very easy yes",
  "Brother, do not eat pork",
  "That is حرام please don't eat it",
  "Click faster"
]

class messages(commands.Cog):

    def __init__(self, client):
        self.client = client

    #insults
    @commands.command()
    async def insult(self, ctx):
        await ctx.send(random.choice(insults))

    #advice
    @commands.command()
    async def advice(self,ctx):
        await ctx.send(random.choice(advices))

    #cringe messages
    @commands.command()
    async def ass(self, ctx):
        await ctx.send("Back when we walked on all fours there was a thing right in front of us, a butt. \nThen from the time mankind started walking on two legs, we stopped having butts sticking in our faces all the time. \nAnd in their place boobs appeared right in our faces. \nWomen grew larger breasts to take the place of buttocks. \nTHE ORIGINAL SOURCE OF LIFE IS THE BUTTOCKS! \nBoobs are just a substitute. \nBoobs are nothing more than a pale imitation of the buttocks! \nIf you asked would you rather have the copy or the original, I would take the original! Hips and ass indicate fertility! Boobs jut out forward due to the process of evolution, Keeping buttocks farther back and the rear hidden! \n\nTHIS IS WHY I AM AN ASS MAN!")


def setup(client):
    client.add_cog(messages(client))
