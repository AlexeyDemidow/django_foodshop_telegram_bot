from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram import F

from handlers.auth_handler import authorisation
from handlers.cart_handler import cart, delete_from_cart, minus_from_cart
from handlers.catalog_handler import add_to_cart
from keyboards.keyboards import cart_keyboard, back_keyboard, delete_from_cart_keyboard
from utils.callbacks import MainCallback, CartCallback
from utils.states import BotStates

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "cart"))
async def cart_view(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    cart_data = await cart(auth_token=list(token.values())[0])
    if not list(cart_data.get('results')):
        await call.message.answer(
            'Корзина пуста',
            reply_markup=await back_keyboard()
        )
    else:
        for i in range(len(list(cart_data.get('results')))):
            # Не работает локально, поэтому заменено случайным фото из интернета
            # photo_url = list(catalog_data.get('results')[0].values())[3]
            photo_url = 'https://s3-eu-west-1.amazonaws.com/straus/media/products2/22341.png'
            await call.message.answer_photo(
                photo=photo_url,
                caption=f"Название: {list(cart_data.get('results')[i].values())[3]}\n"
                f"Количество: {list(cart_data.get('results')[i].values())[4]}\n"
                f"Цена: {list(cart_data.get('results')[i].values())[5]}\n"
                f"Итоговая цена: {list(cart_data.get('results')[i].values())[6]}",
                reply_markup=await cart_keyboard(
                    cart_item_id=list(cart_data.get('results')[i].values())[0],
                    food_id=list(cart_data.get('results')[i].values())[1],
                )
            )
    await state.set_state(BotStates.access)


@router.callback_query(CartCallback.filter(F.ccb == "delete_from_cart"))
async def delete_from_cart_view(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    food_id = CartCallback.unpack(call.data).food_id
    await delete_from_cart(auth_token=list(token.values())[0], cart_item_id=food_id)
    await call.message.answer(
        'Товар удален из корзины',
        reply_markup=await delete_from_cart_keyboard()
    )
    await state.set_state(BotStates.access)


@router.callback_query(CartCallback.filter(F.ccb == "plus"))
async def plus_cart_view(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    food_id = CartCallback.unpack(call.data).food_id
    plus = await add_to_cart(auth_token=list(token.values())[0], food_id=food_id)
    await call.message.answer(
        'Количество товара увеличено на 1',
        reply_markup=await delete_from_cart_keyboard()
    )
    await state.set_state(BotStates.access)


@router.callback_query(CartCallback.filter(F.ccb == "minus"))
async def minus_cart_view(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    food_id = CartCallback.unpack(call.data).food_id
    minus = await minus_from_cart(auth_token=list(token.values())[0], cart_item_id=food_id)
    if minus == '-1':
        await call.message.answer(
            'Количество товара уменьшено на 1',
            reply_markup=await delete_from_cart_keyboard()
        )
    else:
        await call.message.answer(
            'Товар удален из корзины',
            reply_markup=await delete_from_cart_keyboard()
        )
    await state.set_state(BotStates.access)
