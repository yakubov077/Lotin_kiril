from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("""Ushbu bot orqali siz o‘zbek tilidagi matnlarni Lotin-Kiril va Kiril-Lotin formatlari o‘rtasida osonlik bilan o‘gira olasiz. 😊

Bot imkoniyatlari:
- Lotin alifbosidan Kiril alifbosiga o‘girish.
- Kiril alifbosidan Lotin alifbosiga o‘girish.

Misollar:
- Kiriting: 'Salom, qalesiz?' -> 'Салом, қалесиз?'
- Kiriting: 'Салом, қалесиз?' -> 'Salom, qalesiz?'

Loyiha yaratuvchisi: [Sizning ismingiz yoki bot yaratuvchi haqida ma’lumot]
Qo‘shimcha ma’lumot uchun bog‘laning: [aloqa ma’lumotlari]

Botdan foydalanayotganingiz uchun rahmat! 😊""")