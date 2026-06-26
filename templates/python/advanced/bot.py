import asyncio
import logging
import os
import aiosqlite
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Setup Logging
logging.basicConfig(level=logging.INFO)

# Database Setup
async def init_db():
    async with aiosqlite.connect('users.db') as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        await db.commit()

async def save_user(user_id, username, first_name):
    async with aiosqlite.connect('users.db') as db:
        await db.execute('''
            INSERT OR REPLACE INTO users (user_id, username, first_name)
            VALUES (?, ?, ?)
        ''', (user_id, username, first_name))
        await db.commit()

# Bot logic
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await save_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
    await message.answer(f"Hello {message.from_user.first_name}! You have been registered in our SQLite database.")

@dp.message(Command("stats"))
async def cmd_stats(message: types.Message):
    async with aiosqlite.connect('users.db') as db:
        async with db.execute('SELECT COUNT(*) FROM users') as cursor:
            row = await cursor.fetchone()
            count = row[0]
    await message.answer(f"Total registered users: {count}")

async def main():
    await init_db()
    print("Advanced bot (aiogram) is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
