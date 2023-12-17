from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from core.database.core import DataBase

db = DataBase()
router = Router()


@router.message(Command("test"))
async def test(message: Message):
    stats = await db.view_statistics()
    await message.answer(
        f"User count: {stats['user count']}\n"
    )
