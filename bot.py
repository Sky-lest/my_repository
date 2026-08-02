import discord
import asyncio
from discord.ext import commands
#importar funções de outros arquivos
from bot_settings import settings
from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import gen_emoji
from bot_logic import yes_no
from bot_logic import guess_number


# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)

@bot.event
#quando o bot estiver pronto
async def on_ready():
    print(f'Fizemos login como {bot.user}')



#oi
@bot.command()
async def hello(ctx):
    await ctx.channel.send("Olá!")

#tchau
@bot.command()
async def bye(ctx):
    await ctx.channel.send("\U0001f642")

#senha aleatória (de 10 caracteres)
@bot.command()
async def password(ctx):
    await ctx.channel.send(gen_pass(10))

#cara ou coroa
@bot.command()
async def coin(ctx):
    await ctx.channel.send(flip_coin())

#emoji aleatório
@bot.command()
async def emoji(ctx):
    await ctx.channel.send(gen_emoji())

#sim e não
@bot.command()
async def choice(ctx):
    await ctx.channel.send(yes_no())

#adivinhar o número (tentando fazer funcionar)
@bot.command()
async def guess(self, ctx):
    await ctx.channel.send('adivinhe o número de 1 a 10')

    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit()
    
    n = guess_number()

    try:
        guess = await self.wait_for('message', check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        return await ctx.channel.send(f'Desculpe, você demorou, a resposta era {n}.')

    if int(guess.content) == n:
        await ctx.channel.send('Correto!')
    else:
        await ctx.channel.send(f'Errado. Na verdade era {n}.')
    

#tenta fazer funcionar se não encontrar comando
@bot.command()
async def error(ctx):
    if discord.ext.commands.errors.CommandNotFound:
        await ctx.send('comando não encontrado')



#qual bot executar (está no token, que está nas configurações do bot)
bot.run(settings['TOKEN'])
