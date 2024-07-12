import discord
from LarryandLorry_logic import *
from discord.ext import commands
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной bot и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! Im bot")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def my_game(ctx):
    await ctx.send(srl_game())

@bot.command()
async def bot_are_you_cool(ctx):
    await ctx.send('Yes, I AM THE COOL!1!')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
