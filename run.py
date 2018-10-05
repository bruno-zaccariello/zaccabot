# Work with Python 3.6
import discord
import asyncio
import os
from random import choice
from time import sleep

from modules.vote import Vote

TOKEN = os.getenv('token')

this = os.path.dirname(__file__)
print(this)
path_to_messages = os.path.join(this, 'mensagens.txt')

with open(path_to_messages, encoding='utf-8') as f:
    msg_dicas = [l for l in f]

print(msg_dicas)

bot = discord.Client()

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return None

    if message.content.startswith('gay'):
        msg = 'Gay é vc {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)

    if message.content.startswith('rico'):
        msg = f'Esse ai eh fresco'
        await bot.send_message(message.channel, msg)

    if message.content.startswith('chebel'):
        msg = f'Bate punheta pra anime'
        await bot.send_message(message.channel, msg)

    if message.content.startswith('!openvote'):
      async def ERROR(msg):
        await bot.send_message(message.channel, msg)

      try:
        setup = message.content.split(' ')
        goal = setup[1]
        print(goal)
        if int(goal) == 1:
          await ERROR('Você não pode iniciar uma votação com meta de 1 voto.')
        
        objective = " ".join(word for word in setup[2:])
        print(objective)
        
        votacao = Vote(goal, objective, client, message.author)
        await votacao.voting()
        votacao = None
      except Exception:
        await ERROR('Por favor utilize o seguinte formato:\n\
        !openvote meta mensagem\
        ')

    if message.content.startswith('::dica'):
        msg = choice(msg_dicas)
        await bot.send_message(message.channel, msg)

    if message.content.startswith('mini'):
        msg = f'Curte uma encruzilhada gay'
        await bot.send_message(message.channel, msg)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

async def dicas():
    await bot.wait_until_ready()
    channel = bot.get_channel('495432153203736576')
    while not bot.is_closed:
        await bot.send_message(channel, choice(msg_dicas))
        await asyncio.sleep(60*60*2)

bot.loop.create_task(dicas())
bot.run(TOKEN)
