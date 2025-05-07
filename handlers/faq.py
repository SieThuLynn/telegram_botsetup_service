from aiogram import types, Router
from data import faq_content
import os
from dotenv import load_dotenv

load_dotenv()
router = Router()

@router.message()
async def faq_handler(message: types.Message):
    text = message.text

    if text == "🛍 Online Store Bot":
        await message.answer(faq_content.ONLINE_STORE_FAQ)
    elif text == "🧾 E-Receipt OCR Bot":
        await message.answer(faq_content.ERECEIPT_FAQ)
    elif text == "🎓 Class Registration Bot":
        await message.answer(faq_content.CLASS_BOT_FAQ)
    elif text == "🖼 Watermark Bot":
        await message.answer(faq_content.WATERMARK_FAQ)
    elif text == "📬 Admin Notify Bot":
        await message.answer(faq_content.ADMIN_NOTIFY_FAQ)

def register_handlers(dp):
    dp.include_router(router)
