import os
import asyncio
from bot import bot  # твой экземпляр commands.Bot

async def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("❌ Нет токена!")
        return
    try:
        await bot.start(token)
    except Exception as e:
        print(f"❌ Бот упал: {e}")

if __name__ == "__main__":
    asyncio.run(main())
