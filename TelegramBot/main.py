import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Initialize bot and dispatcher with new default property structure
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)
dp = Dispatcher()

# Register handlers
from handlers import start, contact, faq
start.register_handlers(dp)
contact.register_handlers(dp)
faq.register_handlers(dp)

# Optional: Set bot commands
async def set_commands():
    await bot.set_my_commands([
        BotCommand(command="start", description="Start the bot")
    ])

# Main function
async def main():
    await set_commands()
    print("🤖 Bot is Running ...")
    await dp.start_polling(bot)

# Run bot
if __name__ == "__main__":
    asyncio.run(main())
