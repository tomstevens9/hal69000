import discord
import time
import io
import os
import psycopg2

REQUIRED_VARIABLES = ['DISCORD_TOKEN', 'POSTGRES_PASSWORD']
missing_variables = [var
                     for var
                     in REQUIRED_VARIABLES
                     if var not in os.environ]
if missing_variables:
    print(f'Environment variables {missing_variables} must be set before running bot.', flush=True)


TOKEN = os.environ['DISCORD_TOKEN']

print('Connecting to database\n', flush=True)
conn = psycopg2.connect(f"dbname='postgres' user='postgres' host='db' password='{os.environ['POSTGRES_PASSWORD']}'")

client = discord.Client()
voice_client = None
    
class Flag:
    def __init__(self, state):
        self.state = state

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client), flush=True)

@client.event
async def on_message(message):
    print('Received message', flush=True)
    global voice_client

    # never respond to own messages
    if message.author == client.user:
        return

    message_text = message.content
    if message.content.startswith('-'):
        cur = conn.cursor()
        query = f'SELECT filename FROM frontend_sound WHERE command LIKE \'%{message.content[1:]}%\' LIMIT 1'
        print(f'Running query - {query}', flush=True)
        cur.execute(query)
        row = cur.fetchone()
        cur.close()
        if row:
            filename = row[0]
            print(f'Found sound: {filename}', flush=True)

    if filename:
        # make sure bot is connected to voice chat
        if voice_client is None or not voice_client.is_connected():
            voice_client = await message.author.voice.channel.connect()
        filepath = f'/app/media/{filename}'
        sound_file = discord.FFmpegPCMAudio(executable='/usr/bin/ffmpeg', source=filepath)
        voice_client.play(sound_file)
        
client.run(TOKEN)
