# 🤖 Telegram Bot Setup Service – FAQ Auto Reply Bot

A Telegram bot that explains available bot services and provides FAQs using interactive buttons.

## 🚀 Features
- /start command to greet users and show service options
- Interactive reply keyboard for bot categories
- FAQ replies for each category
- Admin contact link
- Easily extendable to real bot flows (Online Store, E-Receipt OCR, etc.)

## 🧾 Available Bot Services
- 🛍 Online Store Order Bot
- 🧾 E-Receipt OCR Bot (KPay/CBPay)
- 🎓 Class Registration Bot
- 🖼 Photo Watermark Bot
- 📬 Admin Alert Bot
- 💬 FAQ Auto Reply Bot

## 📁 Project Structure

project/ ├── main.py ├── .env ├── handlers/ │ ├── start.py │ └── faq.py ├── utils/ │ └── keyboards.py ├── data/ │ └── faq_content.py