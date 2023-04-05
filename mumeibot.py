from time import ctime
import discord
import os
import time
from datetime import datetime, tzinfo
from discord import message
from discord import channel
from discord import mentions
from discord.ext import commands
from config import API_KEY, token

load_dotenv

client = discord.Client()
embed = discord.Embed()

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%M")
day = now.strftime("%D")

time = now.strftime("%I:%M:%S")

date_time = now.strftime("%b/%d/%Y")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="*help"))
    print('Currently logged in as ' + client.user.name, client.user.id) 

if (str(datetime.now()) >= '2021-08-31 17:50:00.000000'):
    print(datetime.now())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('*hello' or 'hello'):
            await message.channel.send('Hello!')

    if message.content.startswith('motherfucker' or 'mfker'):
        await message.channel.send('https://www.youtube.com/watch?v=3Njvr6-OVao&ab_channel=ZeroDuping')

    if message.content.startswith('*help'):
        help2 = discord.Embed(title='Help', description='Commands')
        help2.timestamp
        help2.color = 0x826d0e
        help2.set_thumbnail(url="https://i.imgur.com/ixlsPal.jpg")
        help2.add_field(
            name="*class", value="List of classes"
        )
        help2.add_field(
            name="command 2", value="Description of command 2", inline=True
        )
        help2.add_field(
            name="command 3", value="Description of command 3", inline=True
        )
        await message.channel.send(embed=help2)

    if message.content.startswith('who' or 'who?'):
        await message.channel.send('...who?')

    if message.content.startswith('time' or 'time?'):
        await message.channel.send(time)

    if message.content.startswith('date' or 'date?'):
        await message.channel.send(date_time)
    
    if message.content.startswith('*whoami' or 'whoami'):
        await message.channel.send('You are {}'.format(message.author.name))

    if message.content.startswith('*class' or 'class'):
        Sched = discord.Embed(title='Example', description='Embed')
        Sched.title = "Classes"
        Sched.description = "List of classes with Zoom Meetings"
        Sched.timestamp
        Sched.color = 0x826d0e
        Sched.set_thumbnail(url="https://i.imgur.com/ixlsPal.jpg")
        Sched.add_field(
            name="PED3", value="M 7:30 - 8:30 \n\n Zoon Meeting ID: 247 521 4872 \n Passcode: 1uiqbG"
        )
        Sched.add_field(
            name="Trigonometry", value="MWF 9:30 - 10:30 \n\n https://usls-edu-ph.zoom.us/j/3433808829?pwd=OHBHTkRxQnhGNUR6Q0tXaUVEVkdhdz09#success \n\n UPDATED", inline=True
        )
        Sched.add_field(
            name="CC104", value="MWF 3:30 - 4:30 \n\n https://l.facebook.com/l.php?u=https%3A%2F%2Fusls-edu-ph.zoom.us%2Fj%2F92137612838%3Fpwd%3DcWZaNkprVnN1aCtXbHRNTW14SXoydz09%26fbclid%3DIwAR2LLxeEmbCwyPRRsDIvL2VvsZgFcRkjgDaQPrLtcybSOY9x4-zCftk0PA0&h=AT3TGTngN8PyOEmWrPD5PSDl_Bd0h554PDw8TLpDJMd7ldQiRby10G91G1HO7TSnn4ZLlHDrwhV6499Pm3MsUuetKwQdsFyTKqfu49e-CzQ5mq9kqE0bNIf-2s8v-NGdW1PqwQ", inline=True
        )
        Sched.add_field(
            name="CC105", value="MWF 4:30 - 5:30 \n\n https://usls-edu-ph.zoom.us/j/94969661511?pwd=bmU2eEpzY200c2R1WXhYUkE1cjVoZz09&fbclid=IwAR1Oj8nZ-Czv6i3J4pNzFyi3aYVcJfq0_XZIrY808G0wZtGi6tbl4n2H9kA#success \n\n UPDATED", inline=True
        )
        Sched.add_field(
            name="CSE", value="TTH 4:30 - 5:30 \n\n https://usls-edu-ph.zoom.us/j/92561307381?pwd=VE5PZmpTaE9HM0tCWVdUSkdQUGdNZz09", inline=True
        )
        Sched.add_field(
            name="Discrete Structures", value=" TTH 11:30 - 12:30 \n\n https://us02web.zoom.us/j/85938449854?pwd=c2VEak5HRFBnWnlZNTNYbjJ6bDh4UT09&fbclid=IwAR1eKq2DwSdNB0-LGH--DrFLQKBG0aXEEP5asKjlleCFmIu6k_WFR8TEt9I", inline=True
        )
        Sched.add_field(
            name="OOP", value="TTH 6:30 - 7:30 \n\n https://usls-edu-ph.zoom.us/j/91909074311?pwd=TVJXa3NKUFZROEV3MTUvMDB3TVI4dz09", inline=True
        )
        Sched.add_field(
            name="NSTP", value="SAT 8:30 - 9:30 \n\n https://usls-edu-ph.zoom.us/j/95328196016?pwd=eEsxb1VBdXcyMmUwTU1rZVZLZ3dUUT09", inline=True
        )
        await message.channel.send(embed=Sched)

client.run('token')