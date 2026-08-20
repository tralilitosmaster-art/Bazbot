import os
import asyncio
from bot import bot

async def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("❌ DISCORD_TOKEN не найден!")
        return
    try:
        await bot.start(token)
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())
