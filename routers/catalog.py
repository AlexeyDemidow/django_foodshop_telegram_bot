from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram import F

from handlers.auth_handler import authorisation, profile
from handlers.catalog_handler import catalog, add_to_cart
from keyboards.keyboards import catalog_keyboard, back_keyboard, delete_from_cart_keyboard
from utils.callbacks import MainCallback, CartCallback
from utils.states import BotStates

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "catalog"))
async def catalog_view(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    catalog_data = await catalog(auth_token=list(token.values())[0])
    for i in range(len(list(catalog_data.get('results')))):
        # Не работает локально, поэтому заменено случайным фото из интернета
        # photo_url = list(catalog_data.get('results')[0].values())[3]
        photo_url = 'https://s3-eu-west-1.amazonaws.com/straus/media/products2/22341.png'
        await call.message.answer_photo(
            photo=photo_url,
            caption=f"Название: {list(catalog_data.get('results')[i].values())[1]}\n"
                    f"Состав: {list(catalog_data.get('results')[i].values())[2]}\n"
                    f"Вес: {list(catalog_data.get('results')[i].values())[4]}\n"
                    f"Цена: {list(catalog_data.get('results')[i].values())[5]}",
            reply_markup=await catalog_keyboard(food_id=list(catalog_data.get('results')[i].values())[0])
        )
    await state.set_state(BotStates.access)


@router.callback_query(CartCallback.filter(F.ccb == "add_to_cart"))
async def add_to_cart_view(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    food_id = CartCallback.unpack(call.data).food_id
    await add_to_cart(auth_token=list(token.values())[0], food_id=food_id)
    await call.message.answer(
        'Товар добавлен в корзину',
        reply_markup=await delete_from_cart_keyboard()
    )
    await state.set_state(BotStates.access)
