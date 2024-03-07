

import logging
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from .models import UserProfile, Token
from .utils import get_user, generate_code, get_token
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from asgiref.sync import sync_to_async

from django.utils import timezone

class AddUser(StatesGroup):
    phone_number = State()
    full_name = State()
    age = State()
    
TOKEN = "6533867106:AAH_KslLFEadE9rzBH4JOnTPhy5ulH5i8BU"

dp = Dispatcher()
@dp.message(F.text.casefold() == "Bekor qilish")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=types.ReplyKeyboardRemove(),
    )



@dp.message(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    r_contact = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Kontaktni yuborish", request_contact=True)
            ]
        ]
    )
    try:
        user = await get_user(message.from_user.id)
        if user.activate_user == True:
            logging.info("User already exists")
            await message.answer(
                text="Siz avval ro'yhatdan o'tgansiz, hozir esa parolni kiritishingiz kerak:  ",
            ) 
        else:

            # code = await sync_to_async(Token.objects.filter, thread_sensitive=True)(user=user)
            code = await get_token(user)
          
            if code and code.expiration_time > timezone.now():
                # Faol kod mavjud va hali muddati o'tmagan
                await message.answer(
                    text=f"Sizning aktivatsiya kodingiz: {code.code}",
                )
            else:
                if code is not None:
                    code.active = False
                    await sync_to_async(code.save, thread_sensitive=True)()
                    new_code = ''.join([str(i) for i in generate_code()])
                    new_token =await Token.objects.acreate(user=user, code=new_code, active=True)
                    await message.answer(
                        text=f"Sizning yangi aktivatsiya kodingiz: {new_token.code}",
                    )
                else:
                    # code is None, handle this case

                    new_code = ''.join([str(i) for i in generate_code()])
                    new_token =await Token.objects.acreate(user=user, code=new_code, active=True)
                    await message.answer(
                        text=f"Sizning yangi aktivatsiya kodingiz: {new_token.code}",
                    )
                 
    except UserProfile.DoesNotExist:
        logging.info("New user")
        await message.answer(
            text="Quyidagi tugmani bosib, telefon raqamingizni yuboring: ", reply_markup=r_contact
        )
        await state.set_state(AddUser.phone_number)

@dp.message(AddUser.phone_number)
async def get_phone_number(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    await state.set_state(AddUser.full_name)
    await message.answer("Ism va familiyangizni yuboring: ")
    await state.update_data(phone_number=phone)
    
@dp.message(AddUser.full_name)
async def get_full_name(message: Message, state: FSMContext):
    full_name = message.text
    await state.set_state(AddUser.age)
    await message.answer("Yoshingizni yozib yuboring: ")
    await state.update_data(full_name=full_name)
    
@dp.message(AddUser.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    user_info = await state.get_data()
    try:
        user = await UserProfile.objects.acreate(
            full_name=user_info.get('full_name'),
            username=message.from_user.username,
            tg_id=message.from_user.id,
            age = user_info.get("age"),
            phone_number=user_info.get('phone_number'),
        )
        code = ''.join([str(i) for i in generate_code()])
        await Token.objects.acreate(
            user=user,
            code = code,
            active=True
        )
        
        await message.answer(f"Ushbu parolni web saytga tering: \n\n```{code}```", parse_mode='Markdown')
        await state.clear()

    except Exception as es:
        logging.error(es)
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

