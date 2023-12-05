import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers.signals import start_bot, stop_bot
from utils.commands import set_commands
from routers import auth, start, profile, menu, catalog, cart, unauth

from bot_settings import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


# Запуск бота
async def main():
    dp.startup.register(start_bot)
    dp.include_routers(
        start.router,
        auth.router,
        profile.router,
        menu.router,
        catalog.router,
        cart.router,
        unauth.router,

    )

    dp.shutdown.register(stop_bot)
    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
