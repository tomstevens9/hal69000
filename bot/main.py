import asyncio
import os
import time

import discord
import pika
import psycopg2

REQUIRED_VARIABLES = ["DISCORD_TOKEN", "POSTGRES_PASSWORD", "GUILD_ID"]
missing_variables = [var for var in REQUIRED_VARIABLES if var not in os.environ]
if missing_variables:
    print(
        f"Environment variables {missing_variables} must be set before running bot.",
        flush=True,
    )


TOKEN = os.environ["DISCORD_TOKEN"]

print("Connecting to database\n", flush=True)
conn = psycopg2.connect(
    f"dbname='postgres' user='postgres' host='db' password='{os.environ['POSTGRES_PASSWORD']}'"
)

client = discord.Client()

connected = False
while not connected:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
        print("connected to rabbit", flush=True)
        connected = True
    except Exception:
        time.sleep(1)


async def test_task():
    channel = connection.channel()
    while True:
        try:
            __, __, command_bytes = channel.basic_get("commands", auto_ack=True)
        except Exception as e:
            print(e)
            await asyncio.sleep(0.5)
        if command_bytes:
            command = command_bytes.decode()
            print(f"Picked up command from queue - {command}")
            cur = conn.cursor()
            query = f"SELECT filename FROM frontend_sound WHERE command LIKE '%{command}%' LIMIT 1"
            print(f"Running query - {query}", flush=True)
            cur.execute(query)
            row = cur.fetchone()
            cur.close()
            filename = None
            if row:
                filename = row[0]
                print(f"Found sound: {filename}", flush=True)

            if filename:
                # make sure bot is connected to voice chat
                if len(client.voice_clients) == 0:
                    # get the voice channel from the guild
                    guild = client.get_guild(int(os.environ["GUILD_ID"]))
                    voice_channel = guild.voice_channels[0]
                    await voice_channel.connect()
                voice_client = client.voice_clients[0]
                filepath = f"/app/media/{filename}"
                sound_file = discord.FFmpegPCMAudio(
                    executable="/usr/bin/ffmpeg", source=filepath
                )
                voice_client.play(sound_file)
                while voice_client.is_playing():
                    await asyncio.sleep(0.5)
        else:
            await asyncio.sleep(0.5)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client), flush=True)


@client.event
async def on_message(message):
    print("Received message", flush=True)

    # never respond to own messages
    if message.author == client.user:
        return

    if message.content.startswith("-"):
        channel = connection.channel()
        channel.queue_declare(queue="commands")
        channel.basic_publish(
            exchange="", routing_key="commands", body=message.content[1:]
        )


# Start consumer thread for the command consumer
print("Starting bot...", flush=True)
# Start the bot
client.loop.create_task(test_task())
client.run(TOKEN)
