import discord
import time
import io
import os
import psycopg2
import pika
import threading

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
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client), flush=True)

@client.event
async def on_message(message):
    print('Received message', flush=True)

    # never respond to own messages
    if message.author == client.user:
        return

    if message.content.startswith('-'):
        channel = connection.channel()
        channel.queue_declare(queue='commands')
        channel.basic_publish(exchange='',
                      routing_key='commands',
                      body=message.content[1:])

def connect_to_voice_channel():
    if len(client.voice_clients) == 0:
        # get the voice channel from the guild
        guild = client.get_guild(711529317313675264)
        voice_channel = guild.voice_channels[0]
        voice_client = await voice_channel.connect()
    else:
        voice_client = client.voice_clients[0]
    return voice_client

# Start consumer thread for the command consumer
def play_sound(ch, method, properties, body):
    cur = conn.cursor()
    query = f'SELECT filename FROM frontend_sound WHERE command LIKE \'%{body}%\' LIMIT 1'
    print(f'Running query - {query}', flush=True)
    cur.execute(query)
    row = cur.fetchone()
    cur.close()
    filename = None
    if row:
        filename = row[0]
        print(f'Found sound: {filename}', flush=True)

    if filename:
        # make sure bot is connected to voice chat
        voice_client = connect_to_voice_channel()
        filepath = f'/app/media/{filename}'
        sound_file = discord.FFmpegPCMAudio(executable='/usr/bin/ffmpeg', source=filepath)
        voice_client.play(sound_file)


def consume_commands():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='commands')
    channel.basic_consume(queue='commands',
                          auto_ack=True,
                          on_message_callback=play_sound)

thread = threading.Thread(target=consume_commands)
        
# Start the bot
client.run(TOKEN)
