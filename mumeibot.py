from time import ctime
import discord, os, time, asyncio
from chatGPT import chatgpt_response
from datetime import datetime, tzinfo
from discord import app_commands
from dotenv import load_dotenv
import random
import requests
import json
from bs4 import BeautifulSoup
load_dotenv()

TOKEN = os.getenv('TOKEN')
CANVAS_TOKEN = os.getenv('CANVAS_TOKEN')

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%M")
day = now.strftime("%D")
time = now.strftime("%I:%M:%S")
date_time = now.strftime("%b/%d/%Y")

course_id = ['27960', '27962', '27966', '26808', '26552']

def print_courseID(course_id):
    print(course_id)

async def assignment(message):    
    url = 'https://usls.instructure.com/api/v1/courses/{course_id}/assignments/'
    headers = {
    'Authorization': f'Bearer {CANVAS_TOKEN}'
    }
    for value in range(len(course_id)):
        if message:
            response = requests.get(url.format(course_id=course_id[value]), headers=headers)
            if response:
                assignments = response.json()
                courseurl = 'https://usls.instructure.com/api/v1/courses/'
                courseresponse = requests.get(courseurl, headers=headers)
                course_data = courseresponse.json()
                assembed = discord.Embed(title="{course_name}", description='Assignments', type='rich')
                assembed.timestamp = datetime.utcnow()
                assembed.color = 0x873e23
                assembed.set_footer(text="Data was yoinked from Canvas")

                for assignment in assignments:
                    course_name = assignment['course_id']
                    #assignment_id = assignment['id']
                    assignment_name = assignment['name']
                    assignment_maxpoint = assignment['points_possible']
                    assignment_fgi = assignment['omit_from_final_grade']
                    #assignment_description = assignment['description']
                    assignment_due = assignment['due_at']
                    assignment_url = assignment['html_url']
                    assignment_attempts = assignment['allowed_attempts']
                    #splitdesc = assignment_description.split()
                    #first25 = ' '.join(splitdesc[:25])
                    assembed.title=course_name
                    assembed.add_field(name=f"{assignment_name}", value=f"Points Possible: ```{assignment_maxpoint}```", inline=True)
                    assembed.add_field(name="Deadline", value=f"Due Date (YYYY-MM-DD): ```{assignment_due}```", inline=True)
                    assembed.add_field(name=f"Counted in Final Grade:", value=f"```{assignment_fgi}```", inline=False)
                    assembed.add_field(name=f"URL", value=f"[Link to assignment]({assignment_url})", inline=True)
                    assembed.add_field(name="Allowed Attempts: ", value=f"```{assignment_attempts}```", inline=True)
                    assembed.add_field(name='\u200B', value='\u200B', inline=False)
                await message.channel.send(embed=assembed)
                await asyncio.sleep(5)
        else:
            print("No message provided")

class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Game(name="Ready for your input!"))
        await tree.sync()
        print(f'Logged on as {self.user}!')

    if (str(datetime.now()) >= '2021-08-31 17:50:00.000000'):
        print(datetime.now())

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return

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

        if message.content.startswith('*assign' or 'assign'):
            await assignment(message)

        if message.content.startswith('*hello' or 'hello'):
            await message.channel.send('Hello!')

        if message.content.startswith('who' or 'who?'):
            await message.channel.send('...who?')

        if message.content.startswith('time' or 'time?'):
            await message.channel.send(time)

        if message.content.startswith('date' or 'date?'):
            await message.channel.send(date_time)
    
        if message.content.startswith('*whoami' or 'whoami'):
            await message.channel.send('You are {}'.format(message.author.name))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "currentdate", description = "displays the current date")
async def first_tree(interaction):
    await interaction.response.send_message(date_time)

@tree.command(name = "assignments", description = "displays current assignments assigned to you")
async def second_tree(interaction):
    await assignment(interaction)
    await interaction.response.send_message(date_time)

@tree.command(name = "chatgpt", description = "get an answer directly from ChatGPT")
@app_commands.describe(question = "What question would you like to get answered by ChatGPT?")
async def chatgpt(interaction: discord.Interaction, question: str):
    await interaction.response.defer(ephemeral=False)
    await asyncio.sleep(5)
    command, user_message = None, None
    command = ("/ai")
    user_message = question.replace('/ai', '')
    print(command, user_message)

    bot_response = chatgpt_response(prompt=user_message)
    chatgptembed = discord.Embed(type='rich')
    chatgptembed.timestamp = datetime.utcnow()
    chatgptembed.color = 0x873e23
    chatgptembed.add_field(
        name="Question: ", value=f"```{user_message}```", inline=False
    )
    chatgptembed.add_field(
        name="Answer: ", value=f"```{bot_response}```", inline=True
    )
    chatgptembed.set_footer(text="Answer Generated by ChatGPT")
    chatgptembed.set_author(url="https://chat.openai.com/auth/login", icon_url="https://pbs.twimg.com/profile_images/1598216720572829697/cu3LTrRl_400x400.jpg", name="ChatGPT")
    await interaction.followup.send(embed=chatgptembed)

client.run(TOKEN)