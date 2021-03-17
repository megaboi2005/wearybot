import discord
from discord.ext import commands
import os

client = discord.Client()
client = commands.Bot(command_prefix = '$')
@client.command()
async def ping():
    await client.say('Pong!')
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output =+ word
        output += ' '

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#test command
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
#help
    if message.content.startswith('$help'):
        await message.channel.send('http://megastudios.69.mu/discord/help2.png')
        await message.channel.send('For more help')
        await message.channel.send('ask hammyouboi#6969')
#rickroll
    if message.content.startswith('$rickroll'):
        await message.channel.send('https://cdn.discordapp.com/attachments/786115426697478144/820413006377910282/yt1s.com_-_Rick_Astley_Never_Gonna_Give_You_Up_4K_60_FPS_Remastered_v720P.mp4')
#dmme
    if message.content.startswith('$dmme'):
        await message.author.dm_channel.send('h')
#nayfen
    if message.content.startswith('nayfen'):
        await message.channel.send('em')
#em
    if message.content.startswith('em'):
        await message.channel.send('Nayfen')
#balls
    if message.content.startswith('$balls'):
        await message.channel.send('BALLS')
#sendnudes
    if message.content.startswith('$sendnudes'):
        await message.channel.send('Nayfen :weary:')
#baka
    if message.content.startswith('$baka'):
        await message.channel.send('You are such a baka https://i.imgur.com/kgFp2gm.png')
#cheat
    if message.content.startswith('$cheat'):
        await message.channel.send('Not you cheating on me :worried:')
#watchaeating
    if message.content.startswith('$watcha eating'):
        await message.channel.send('Guys I’m eating a burger rn')
#canIhaveIt
    if message.content.startswith('$can I have it'):
        await message.channel.send('Sure Bestie')
#useggsy
    if message.content.startswith('$u seggsy'):
        await message.channel.send('no u')
#heybestie
    if message.content.startswith('$hey bestie'):
        await message.channel.send('Hey bestie!!!!')
#marioirl
    if message.content.startswith('marioirl'):
        await message.channel.send('https://cdn.discordapp.com/attachments/554704777548791829/821184817106386964/video0.mp4')
#icpoopy
    if message.content.startswith('I see poopy'):
        await message.channel.send('https://media.discordapp.net/attachments/725836813872267275/795444244088750150/poopy.gif?width=374&height=288')
    if message.content.startswith('i see poopy'):
        await message.channel.send('https://media.discordapp.net/attachments/725836813872267275/795444244088750150/poopy.gif?width=374&height=288')
@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Streaming(name='seggsy girl plays dbd', url='https://www.twitch.tv/eemmahamlet'))

    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


#async def on_ready():
    #await client.change_presence(activity=discord.Game('Dead by daylight'))

    #print('Connected to bot: {}'.format(client.user.name))
    #print('Bot ID: {}'.format(client.user.id))


client.run('token')