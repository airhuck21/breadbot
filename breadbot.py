import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print(":bread:")

@client.command()
async def bread(ctx):
    await ctx.send(':bread:')
    
@client.command()
async def breadping(ctx):
    await ctx.send({round(client.latency * 1000)})




client.run('NjkxMzM1OTA0MjgzMDY2NDQ4.XnefCQ.ha-82PWQOs-rqC_dc_xnFVgL5NQ')
    
