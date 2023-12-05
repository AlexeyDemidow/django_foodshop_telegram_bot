from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram import F
from aiogram.types import Message

from handlers.auth_handler import authorisation, profile, account, edit_profile_customer_name, \
    edit_profile_customer_birthdate, edit_profile_customer_telephone, edit_profile_customer_email
from keyboards.keyboards import profile_keyboard, edit_profile_keyboard, go_to_profile_keyboard
from utils.callbacks import MainCallback
from utils.states import BotStates

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "profile"))
async def profile_view(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    profile_data = await profile(auth_token=list(token.values())[0])
    account_data = await account(auth_token=list(token.values())[0])
    await call.message.answer(
        f'Данные пользователя:\n'
        f"Имя: {list(profile_data.get('results')[0].values())[1]}\n"
        f"Дата рождения: {list(profile_data.get('results')[0].values())[2]}\n"
        f"Телефон: {list(profile_data.get('results')[0].values())[3]}\n"
        f"Адрес электронной почты: {list(account_data.get('results')[0].values())[2]}\n",
        reply_markup=await profile_keyboard()
    )
    await state.set_state(BotStates.access)


@router.callback_query(MainCallback.filter(F.mcb == "edit_profile"))
async def edit_profile_view(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(
        f'Изменить данные пользователя:\n',
        reply_markup=await edit_profile_keyboard()
    )
    await state.set_state(BotStates.access)


@router.callback_query(MainCallback.filter(F.mcb == "edit_name"))
async def edit_name_view(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(
        f'Введите новое имя пользователя'
    )
    await state.set_state(BotStates.edit_name)


@router.message(BotStates.edit_name)
async def new_name_view(message: Message, state: FSMContext):
    await state.update_data(customer_name=message.text)
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    profile_data = await profile(auth_token=list(token.values())[0])
    edit_name = await edit_profile_customer_name(
        auth_token=list(token.values())[0],
        customer_name=data['customer_name'],
        customer_id=list(profile_data.get('results')[0].values())[0]
    )
    await message.answer(
        f'Имя успешно изменено на {edit_name["customer_name"]}\n',
        reply_markup=await go_to_profile_keyboard()
    )
    await state.set_state(BotStates.access)


@router.callback_query(MainCallback.filter(F.mcb == "edit_birthdate"))
async def edit_birthdate_view(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(
        f'Введите другую дату рождения в формате ГГГГ-ММ-ДД'
    )
    await state.set_state(BotStates.edit_birthdate)


@router.message(BotStates.edit_birthdate)
async def new_birthdate_view(message: Message, state: FSMContext):
    await state.update_data(customer_birthdate=message.text)
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    profile_data = await profile(auth_token=list(token.values())[0])
    edit_birthdate = await edit_profile_customer_birthdate(
        auth_token=list(token.values())[0],
        customer_birthdate=data['customer_birthdate'],
        customer_id=list(profile_data.get('results')[0].values())[0]
    )
    await message.answer(
        f'Дата рождения успешно изменена на {data["customer_birthdate"]}\n',
        reply_markup=await go_to_profile_keyboard()
    )
    await state.set_state(BotStates.access)


@router.callback_query(MainCallback.filter(F.mcb == "edit_tel"))
async def edit_tel_view(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(
        f'Введите новый номер телефона в формате +XXXXXXXXXXXX'
    )
    await state.set_state(BotStates.edit_tel)


@router.message(BotStates.edit_tel)
async def new_tel_view(message: Message, state: FSMContext):
    await state.update_data(customer_tel=message.text)
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    profile_data = await profile(auth_token=list(token.values())[0])
    edit_tel = await edit_profile_customer_telephone(
        auth_token=list(token.values())[0],
        customer_telephone=data['customer_tel'],
        customer_id=list(profile_data.get('results')[0].values())[0]
    )
    await message.answer(
        f'Телефон успешно заменен на {data["customer_tel"]}\n',
        reply_markup=await go_to_profile_keyboard()
    )
    await state.set_state(BotStates.access)


@router.callback_query(MainCallback.filter(F.mcb == "edit_username_email"))
async def edit_username_view(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(
        f'Введите новый псевдоним пользователя'
    )
    await state.set_state(BotStates.edit_username)


@router.message(BotStates.edit_username)
async def edit_email_view(message: Message, state: FSMContext):
    await state.update_data(customer_username=message.text)
    await message.answer(
        f'Введите новый адрес электронной почты'
    )
    await state.set_state(BotStates.edit_email)


@router.message(BotStates.edit_email)
async def new_username_email_view(message: Message, state: FSMContext):
    await state.update_data(customer_email=message.text)
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    account_data = await account(auth_token=list(token.values())[0])
    edit_date = await edit_profile_customer_email(
        auth_token=list(token.values())[0],
        customer_username=data['customer_username'],
        customer_email=data['customer_email'],
        customer_id=list(account_data.get('results')[0].values())[0]
    )
    print(edit_date)
    await state.update_data(
        username=edit_date['username']
    )
    await message.answer(
        f'Псевдоним пользователя успешно заменен на {data["customer_username"]}\n'
        f'Адрес электронной почты успешно заменен на {data["customer_email"]}\n',
        reply_markup=await go_to_profile_keyboard()
    )
    await state.set_state(BotStates.access)
