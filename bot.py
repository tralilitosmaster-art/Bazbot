import discord
from discord.ext import commands

# Настройки бота
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Событие готовности
@bot.event
async def on_ready():
    print(f"✅ Бот {bot.user} запущен и готов к работе!")

# Команда !некитбаз
@bot.command()
async def некитбаз(ctx):
    await ctx.send("Я создан @nekitbazik")
