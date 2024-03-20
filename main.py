# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

rustWipeDateFile = open('./sudobot/wipe.txt', 'r')
rustWipeDate = rustWipeDateFile.read()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$rust'):
        if isinstance(message.channel, discord.DMChannel):
            Embed = discord.Embed(title="Сервер мишани Rust", description="Памятка по серверу в расте", color=0xF58A42)
            Embed.add_field(name='Информация о сервере', value=f'IP - 104.234.252.167:28055 \n Последний вайп - {rustWipeDate} \n ', inline=False)
            await message.author.send(embed=Embed)
    elif message.content.startswith('$connect'):
        if message.channel.id == 1219984758252240969:
            Embed = discord.Embed(title="Успешно подключено, дальнейшее пользование ботом будет происходить тут.", description="Напишите */help* чтобы узнать больше команд.", color=0x88fc03)
            await message.author.send(embed=Embed)
    elif message.content.startswith('$clear'):
        if isinstance(message.channel, discord.DMChannel):
            async for message in message.channel.history(limit=100):
                if message.author == client.user: #client.user or bot.user according to what you have named it
                    await message.delete()
        else:
            await message.channel.purge()

client.run('token')
