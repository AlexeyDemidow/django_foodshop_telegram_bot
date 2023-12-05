from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.auth_handler import authorisation, profile
from keyboards.keyboards import start_keyboard, main_keyboard
from utils.callbacks import MainCallback
from utils.states import BotStates

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "back"))
async def menu_view(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    profile_data = await profile(auth_token=list(token.values())[0])
    await callback.message.answer(
        f"{list(profile_data.get('results')[0].values())[1]}, выберите что отобразить:",
        reply_markup=await main_keyboard()
    )
    await state.set_state(BotStates.access)
