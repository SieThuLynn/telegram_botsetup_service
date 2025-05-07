from aiogram import types, Router
from aiogram.types import Message
from aiogram.filters import Command  # Import the Command filter
from utils.keyboard import main_menu_keyboard

router = Router()

@router.message(Command("start"))  # Use Command filter directly
async def cmd_start(message: Message):
    welcome_text = (
        "👋 မင်္ဂလာပါ❕\n"
        "*Telegram Bot Setup Service* မှ ကြိုဆိုပါတယ်\n"
        "✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤\n\n"
        
        "💡 ကျွန်တော်က Telegram Bot မျိုးစုံ setup ပေးနေတာ ဖြစ်ပြီး\n"
        "အောက်ပါ 🤖 Bot အမျိုးအစားတွေကို တည်ဆောက်ပေးနိုင်ပါတယ်\n"
        "\t🛒 Order Bot\n"
        "\t💬 Massage Auto Reply Bot\n"
        "\t💳 E-Receipt Payment Bot\n"
        "\t👨🏼‍💼 Training Class Manager Bot\n"
        "\t🖼 Watermark Bot\n"
        "✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤✤\n\n"
        
        "စတာတွေအပြင်...\n"
        "🤗 ကိုယ်ပိုင်သီးသန့်ဖန်တီးချင်ရင်လဲ Custom  အပ်နှံနိုင်ပါတယ်\n"
        "သင့်လုပ်ငန်းအတွက် ဘယ်လို Bot မျိုးလိုအပ်လဲသာ ပြောလိုက်ပါ 💪\n"
        "👇 စိတ်ဝင်စားရာ Bot ကို နှိပ်ပြီး အသေးစိတ်ကြည့်နိုင်ပါတယ်\n"
        "♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎\n\n"
        
        "နည်းပညာခေတ်ထဲမှာ ခေတ်သစ်နည်းပညာတွေကိုအမှီလိုက်ဖို့အတွက်\n"
        "👋 ကျွန်တော်တို့ Channel: https://t.me/it_helper_mm ကိုလဲ Subscribe လုပ်ထားပေးပါဦး 🙏"
    )
    await message.answer(welcome_text, reply_markup=main_menu_keyboard)

def register_handlers(dp):
    dp.include_router(router)
