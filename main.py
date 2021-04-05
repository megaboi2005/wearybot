import discord
from discord.ext import commands
import random
import os
import asyncio
import subprocess
import json
from pathlib import Path
import wget
import math
import requests
import time
import sys
import logging

client = discord.Client()
client = commands.Bot(command_prefix = '$')
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    print(message.author, ':', message.content)


#test command
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
#help
    if message.content.startswith('$help'):

        await message.channel.send(file=discord.File('help2.png'))
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
        await message.channel.send('You are such a baka')
        await message.channel.send(file=discord.File('baka.png'))
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
#emrickroll
    if message.content.startswith('$emrickroll'):
        await message.channel.send('https://cdn.discordapp.com/attachments/783589176943312929/821806055402766376/cache211910989.mp4')
#attract
    if message.content.startswith('$attract'):
        await message.channel.send('hi! I realize this might come off as a bit odd haha.. but before the whole quarantine thing I saw you around school, and you seem really cool. If you arent interested in talking thats alright, no worries!')
#randomperson
    if message.content.startswith('$randomperson'):
        os.system('curl -o person.png https://thispersondoesnotexist.com/image')
        await message.channel.send(file=discord.File('person.png'))
#pls bully me
    if message.content.startswith('pls bully me'):
        await message.channel.send('ok daddy :weary:')
#randomquote
    if message.content.startswith('$randomquote'):
        os.system('curl https://inspirobot.me/api?generate=true --output url.txt')
        url = open('url.txt', 'r').read().replace('\n', ' ')
        print(url)
        r = requests.get(url, allow_redirects=True)

        open('quote.png', 'wb').write(r.content)
        await message.channel.send(file=discord.File('quote.png'))
#spam
    #if message.content.startswith('spam'):
        #await message.channel.send('spam')
        #await message.channel.send('spam')
        #await message.channel.send('spam')
        #await message.channel.send('spam')
        #await message.channel.send('spam')
        #await message.channel.send('spam')
        #await message.channel.send('spam')
        #await message.channel.send('spam')
        #await message.channel.send('spam')
#joke
    if '$randomjoke' in message.content:
        r = requests.get('http://v2.jokeapi.dev/joke/Any?blacklistFlags=religious,racist,sexist&format=txt', allow_redirects=True)

        open('joke.txt', 'wb').write(r.content)
        joke = open('joke.txt', 'r').read().replace('\n', ' ')
        await message.channel.send(joke)
#test
    if message.content.startswith('!hello'):
        await message.channel.send("content", file=discord.File('help2.png'))

#test
    if message.content.startswith('$bingo'):
        await message.channel.send('bingo')
        await message.channel.send('- colton')
#randomnumber
    if message.content.startswith('$rolldice'):
        numbers = ["1", "2", "3", "4", "5", "6"]
        picked = random.choice(numbers)
        await message.channel.send('you rolled and got a '+ picked)
#8ball
    if message.content.startswith('$8ball'):
        outcomes = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.","Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]

        picked2 = random.choice(outcomes)
        await message.channel.send(picked2)
#yes
    if message.content.startswith('what is pi'):
        await message.channel.send(math.pi)
#whoami
    if message.content.startswith('who am I'):
        await message.channel.send(message.author)
#enn word :ban:
#forgive me mother for the swear
    if 'nigg' in message.content:
        await message.channel.send('HEY!!! NO Enn WORD >:((((( ')
        await message.channel.send(message.author)
        await message.delete()
        print('warned', message.author)
    if 'Nigg' in message.content:
        await message.channel.send('HEY!!! NO Enn WORD >:((((( ')
        await message.channel.send(message.author)
        await message.delete()
        print('warned', message.author)
#shutdown
    if message.content.startswith('$shutdown'):
        await message.channel.send('shutting down in 10 second(s)')
        time.sleep(1)
        await message.channel.send('shutting down in 9 second(s)')
        time.sleep(1)
        await message.channel.send('shutting down in 8 second(s)')
        time.sleep(1)
        await message.channel.send('shutting down in 7 second(s)')
        time.sleep(1)
        await message.channel.send('shutting down in 6 second(s)')
        time.sleep(1)
        await message.channel.send('shutting down in 5 second(s)')
        time.sleep(1)
        await message.channel.send('shutting down in 4 second(s)')
        time.sleep(1)
        await message.channel.send('shutting down in 3 second(s)')
        time.sleep(1)
        await message.channel.send('shutting down in 2 second(s)')
        time.sleep(1)
        await message.channel.send('shutting down in 1 second(s)')
        time.sleep(1)
        await message.channel.send('lol jk')










#async def on_ready():
    #await client.change_presence(activity=discord.Game('Dead by daylight'))

    #print('Connected to bot: {}'.format(client.user.name))
    #print('Bot ID: {}'.format(client.user.id))

async def ch_pr():
    await client.wait_until_ready()

    statuses = ["BALLS","Minecraft","and streaming seggsy girl plays dbd"]

    while not client.is_closed():

        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status,))

        await asyncio.sleep(5)
client.loop.create_task(ch_pr())







client.run('token')