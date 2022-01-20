import discord
import time
import io

TOKEN = 'ODAwMDA0MjEwNTA2MjAzMTM2.YALz-w.8oESh9gLTgk04iBSmA1YgXIXUvE'

discord.opus.load_opus('/usr/local/lib/libopus.dylib')

client = discord.Client()
voice_client = None
    
class Flag:
    def __init__(self, state):
        self.state = state

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global voice_client

    # never respond to own messages
    if message.author == client.user:
        return

    message_text = message.content
    print(message_text)
    filename = {
            '-callback': 'whats_a_callback.m4a',
            '-catchphrase': 'catchphrase.mp4',
            '-;)': 'winkyface.mp4',
            '-doctor': 'doctor.mp4',
            '-quack': 'quack.mp4',
            '-ooowee': 'ooowee.mp3',
            '-fart': 'fart.mp4',
            '-ree': 'ree.mp3',
            '-pog': 'pog.mp4',
            '-shape': 'shape.mp3',
            '-spaghetti': 'spaghet.mp3',
            '-ko': 'KO.mp3',
            '-100': '100.mp3',
    }.get(message_text)
    if filename:
        # make sure bot is connected to voice chat
        if voice_client is None or not voice_client.is_connected():
            voice_client = await message.author.voice.channel.connect()
        filepath = f'/Users/tom/new_bot/discord_bot/static/{filename}'
        print(filepath)
        sound_file = discord.FFmpegPCMAudio(executable='/usr/local/bin/ffmpeg', source=filepath)
        voice_client.play(sound_file)
        
client.run(TOKEN)
