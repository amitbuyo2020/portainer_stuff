import os, time, asyncio
import nest_asyncio
# import pandas as pd
# import numpy as np
# ─── ⁡⁢⁣⁣𝗦𝗘𝗡𝗗 𝗠𝗦𝗚 𝗧𝗢 𝗔 𝗦𝗣𝗘𝗖𝗜𝗙𝗜𝗖 𝗚𝗥𝗢𝗨𝗣⁡ ───────────────────────────────────────────────────────────────────────
import asyncio
from telegram import Bot
from telegram.error import TelegramError
# from dotenv import load_dotenv

# load_dotenv()

nest_asyncio.apply()


async def send_message(bot, chat_id, msg):
    try:
        await bot.send_message(chat_id=chat_id, text=msg)
        print(f"Message sent to {chat_id} successfully.")
    except TelegramError as e:
        print(f"Failed to send message to {chat_id}. Error: {e}")

async def send_messages(bot, chat_ids, msg):
    async_tasks = [send_message(bot, chat_id, msg) for chat_id in chat_ids]
    await asyncio.gather(*async_tasks)

async def send_signal(msg, chat_ids):
    bot_token = "7323317945:AAHjuCJviPRhJnJQUTjbCagVwToT59wnzDQ"
    if not bot_token:
        print("Telegram bot token is not set in environment variables. Please set it up.")
        return

    bot = Bot(token=bot_token)
    print("Starting to send messages...")

    try:
        await send_messages(bot, chat_ids, msg)
    except Exception as e:
        print(f"An error occurred: {e}")

async def main_loop():
    while True:
        await send_signal(msg="Working from Portainer", chat_ids=["-4270402608"]
        await asyncio.sleep(30)
if __name__ == "__main__":
    try:
        asyncio.run(main_loop())
    except KeyboardInterrupt:
        print("Process interrupted by user. Exiting...")
#     while True:
#         send_signal(msg="Working from poratiner", chat_ids=["-4270402608"])
#         time.sleep(30)
