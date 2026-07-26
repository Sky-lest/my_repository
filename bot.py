import discord
from bot_settings import settings
from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import gen_emodji
from bot_logic import yes_no


# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$password'):
            await message.channel.send(gen_pass(10))
    elif message.content.startswith('$coin'):
            await message.channel.send(flip_coin())
    elif message.content.startswith('$emoji'):
                await message.channel.send(gen_emodji())
    elif message.content.startswith('$choice'):
                await message.channel.send(yes_no())
    else:
        await message.channel.send("Comando não encontrado")

client.run(settings['TOKEN'])
