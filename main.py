import os
import staypresent

# Запускаем простой веб-сервер с /health для Render
staypresent.web.json({
    "status": "running",
    "service": "my-discord-bot"
})

# Запускаем твоего основного бота (файл bot.py)
# PORT читаем из переменных окружения Render
staypresent.run(
    "bot.py",
    port=int(os.getenv("PORT", 8080)),
)
