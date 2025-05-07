from aiogram import types, Router, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile

router = Router()

# 📞 Contact Admin main menu
@router.message(F.text == "📞 Contact Admin")
async def contact_menu(message: types.Message):
    contact_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📞 Call +95 9 986 999 250", callback_data='contact_call'),
            InlineKeyboardButton(text="📱 Telegram Contact", url='tg://resolve?domain=smartman_007')
        ],
        [
            InlineKeyboardButton(text="📲 Viber Contact 1", callback_data='viber_contact_1'),
            InlineKeyboardButton(text="📲 Viber Contact 2", callback_data='viber_contact_2')
        ]
    ])
    await message.answer("📞 ဆက်သွယ်ရန် option များ:", reply_markup=contact_keyboard)

@router.callback_query(F.data == "contact_call")
async def handle_contact_call(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("📞 ကျေးဇူးပြုပြီး +95 9 986 999 250 ကို ခေါ်ဆိုပါ။")

@router.callback_query(F.data == "viber_contact_1")
async def handle_viber_contact_1(callback_query: types.CallbackQuery):
    await callback_query.answer()
    photo = FSInputFile("images/viber_1_qr.jpg")
    await callback_query.message.answer_photo(photo, caption="📲 Viber QR Code 1")

@router.callback_query(F.data == "viber_contact_2")
async def handle_viber_contact_2(callback_query: types.CallbackQuery):
    await callback_query.answer()
    photo = FSInputFile("images/viber_2_qr.jpg")
    await callback_query.message.answer_photo(photo, caption="📲 Viber QR Code 2")

def register_handlers(dp):
    dp.include_router(router)
