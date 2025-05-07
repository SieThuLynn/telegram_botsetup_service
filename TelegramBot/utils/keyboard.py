from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Define the main menu keyboard
main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Online Store Bot"),
            KeyboardButton(text="🧾 E-Receipt OCR Bot"),
        ],
        [
            KeyboardButton(text="🎓 Class Registration Bot"),
            KeyboardButton(text="🖼 Watermark Bot"),
        ],
        [
            KeyboardButton(text="📬 Admin Notify Bot"),
            KeyboardButton(text="📞 Contact Admin"),
        ],
    ],
    resize_keyboard=True  # Optional: Resizes the keyboard to fit the screen
)
