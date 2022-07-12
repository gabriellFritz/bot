"""
Cyberspace bot core.

Functions are inside the `plugins` directory.
This file just initialize them all.
"""
import asyncio
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from pyrogram import Client, idle
from pyrogram.session import Session

from config import API_HASH, API_ID, BOT_TOKEN, WORKERS
from database import db, save

# Inicializa o cliente.
client = Client(
    "bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=WORKERS,
    parse_mode="Markdown",
    plugins={"root": "plugins"},
)

# Desativa a mensagem do Pyrogram no início.
Session.notice_displayed = True


async def main():
    await client.start()
    print("Bot rodando...")
    client.me = await client.get_me()

    await idle()

    await client.stop()
    save()
    db.close()


loop = asyncio.get_event_loop()

if __name__ == "__main__":
    loop.run_until_complete(main())
