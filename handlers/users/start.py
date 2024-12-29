from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp,db
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram import F
@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz")
    except:
        await message.answer(text=f"""Assalomu alaykum, <b>{full_name}</b>! 😊
                             
Lotin-Kiril va Kiril-Lotin matn o‘girish botiga xush kelibsiz!  
Kerakli formatga matnni o‘girish uchun shunchaki xabar yuboring, men uni darhol o‘giraman.  

👉 Misollar  
                             
🔹 Kiriting: <b>Salom, do'stim!</b>
  Javob: Салом, дўстим!  

🔹 Kiriting: <b>Салом, дўстим!</b>  
  Javob: Salom, do'stim!
                             
Matnni yuboring va jarayonni kuzating! 😊
""",reply_markup=ReplyKeyboardRemove(),parse_mode='html')

@dp.message(~F.text)
async def reklama_rasm_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "✖️ Faqat so'z kiriting !")