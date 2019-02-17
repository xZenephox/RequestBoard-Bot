from discord.ext import commands
from discord.voice_client import VoiceClient
import discord
import logging
from random import randint
import os

bot = commands.Bot(command_prefix="rb.", status=discord.Status.idle, activity = discord.Game(name="Booting..."))

###Events###

@bot.event
async def on_ready():
    print("Ready to go!")
    print(f"serving: {len(bot.guilds)} guilds.")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Prefix - rb."))


###Comands###

@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"My ping is {ping}ms")

@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
        role = member.top_role
        joined = member.joined_at
        await ctx.channel.send(f"{pronoun} name is {member}. {pronoun} rank is {role}. {pronoun} joined at {joined}.")
    else:
        pronoun = "Their"
    member = ctx.message.author
    name = f"{member.name}#{member.discriminator}"
    role = member.top_role
    joined = member.joined_at
    await ctx.channel.send(f"{pronoun} name is {name}. {pronoun} rank is {role}. {pronoun} joined at {joined}.")

@bot.command()
async def setup(ctx):
    guild = ctx.guild
    await guild.create_text_channel(name="Request-Channel")
    await ctx.channel.send("Request Channel complete!")

@bot.command()
async def request(ctx):
    
    author = ctx.message.author
    content = ctx.message.content[11:]
    rID = str(randint(1, 100000))
    request = f"{author} | {content} | {rID}"
    filename = rID + '.txt'
    with open(filename, "w") as f:
        f.write(request)
        info = request.split(' | ')
        author = info[0]
        request = info[1]
        rid = info[2]
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )

        embed.set_author(name='Request pending approval')
        embed.add_field(name='Requester ', value=author, inline=False)
        embed.add_field(name='Request ', value=request, inline=False)
        embed.add_field(name='ID', value=rid, inline=False )
        channel = bot.get_channel(id=545286951633158165)
        await channel.send(channel, embed=embed)

@bot.command()
@commands.has_role('S-Class')
async def approve(ctx):
    rID = ctx.message.content[11:]
    filename = rID + '.txt'
    with open(filename, 'r') as searchfile:
        for line in searchfile:
            print(line)
            info = line.split(' | ')
            author = info[0]
            request = info[1]
            rid = info[2]
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )

            embed.set_author(name='Request Available!')
            embed.add_field(name='Requester ', value=author, inline=False)
            embed.add_field(name='Request ', value=request, inline=False)
            embed.add_field(name='ID', value=rid, inline=False )
            channel = bot.get_channel(id=502213707045142528)
            await channel.send(channel, embed=embed)

@bot.command()
@commands.has_role('S-Class')
async def deny(ctx):
    rID = ctx.message.content[11:]
    filename = rID + '.txt'
    with open(filename, 'r') as searchfile:
        for line in searchfile:
            print(line)
            info = line.split(' | ')
            author = info[0]
            request = info[1]
            rid = info[2]
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )

            embed.set_author(name='Request Denied.')
            embed.add_field(name='Requester ', value=author, inline=False)
            embed.add_field(name='Request ', value=request, inline=False)
            embed.add_field(name='ID', value=rid, inline=False )
            channel = bot.get_channel(id=545299046848397349)
            await channel.send(channel, embed=embed)

@bot.command()
@commands.has_role('S-Class')
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)






@bot.command()
async def accept(ctx, user):
    rID = ctx.message.content[10:]
    filename = rID + '.txt'
    with open(filename, 'r') as searchfile:
        for line in searchfile:
            info = line.split(' | ')
            author = info[0]
            request = info[1]
            rid = info[2]
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )

            embed.set_author(name='Here is he request you accepted! Please contact the requester immediately!')
            embed.add_field(name='Requester ', value=author, inline=False)
            embed.add_field(name='Request ', value=request, inline=False)
            embed.add_field(name='ID', value=rid, inline=False )
            await ctx.author.send(embed=embed)




bot.run("NTQ0OTk4OTg0MjA1MjA1NTEx.D0jJzw.oZQ0hP__5IdSadynPdgzILb92Ao")
