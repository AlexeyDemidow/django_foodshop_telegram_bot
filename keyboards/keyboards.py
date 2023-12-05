from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.callbacks import MainCallback, CartCallback


async def start_keyboard() -> InlineKeyboardMarkup:
    skb = InlineKeyboardBuilder()
    skb.button(
        text='Вход',
        callback_data=MainCallback(mcb='auth').pack(),
    )
    skb.button(
        text='Перейти на сайт SHAVASHOP',
        url='http://127.0.0.1:8000//',
    )
    skb.adjust(1)
    return skb.as_markup(resize_keyboard=True)


async def main_keyboard() -> InlineKeyboardMarkup:
    mkb = InlineKeyboardBuilder()
    mkb.button(
        text='Выбрать шавуху',
        callback_data=MainCallback(mcb='catalog').pack(),
    )
    mkb.button(
        text='Корзина',
        callback_data=MainCallback(mcb='cart').pack(),
    )
    mkb.button(
        text='Данные пользователя',
        callback_data=MainCallback(mcb='profile').pack(),
    )
    mkb.button(
        text='Выйти',
        callback_data=MainCallback(mcb='exit').pack(),
    )
    mkb.adjust(1)
    return mkb.as_markup(resize_keyboard=True)


async def profile_keyboard() -> InlineKeyboardMarkup:
    pkb = InlineKeyboardBuilder()
    pkb.button(
        text='Редактировать профиль',
        callback_data=MainCallback(mcb='edit_profile').pack(),
    )
    pkb.button(
        text='В главное меню',
        callback_data=MainCallback(mcb='back').pack(),
    )
    pkb.adjust(1)
    return pkb.as_markup(resize_keyboard=True)


async def catalog_keyboard(food_id: int) -> InlineKeyboardMarkup:
    ckb = InlineKeyboardBuilder()
    ckb.button(
        text='Добавить в корзину',
        callback_data=CartCallback(ccb='add_to_cart', food_id=food_id).pack(),
    )
    ckb.button(
        text='В главное меню',
        callback_data=MainCallback(mcb='back').pack(),
    )
    ckb.adjust(1)
    return ckb.as_markup(resize_keyboard=True)


async def back_keyboard() -> InlineKeyboardMarkup:
    back = InlineKeyboardBuilder()
    back.button(
        text='В главное меню',
        callback_data=MainCallback(mcb='back').pack(),
    )
    back.adjust(1)
    return back.as_markup(resize_keyboard=True)


async def cart_keyboard(cart_item_id: int, food_id: int) -> InlineKeyboardMarkup:
    ctkb = InlineKeyboardBuilder()
    ctkb.button(
        text='Плюс 1',
        callback_data=CartCallback(ccb='plus', food_id=food_id).pack(),
    )
    ctkb.button(
        text='Минус 1',
        callback_data=CartCallback(ccb='minus', food_id=cart_item_id).pack(),
    )
    ctkb.button(
        text='Удалить из корзины',
        callback_data=CartCallback(ccb='delete_from_cart', food_id=cart_item_id).pack(),
    )
    ctkb.button(
        text='В главное меню',
        callback_data=MainCallback(mcb='back').pack(),
    )
    ctkb.adjust(1)
    return ctkb.as_markup(resize_keyboard=True)


async def delete_from_cart_keyboard() -> InlineKeyboardMarkup:
    dfc = InlineKeyboardBuilder()
    dfc.button(
        text='В корзину',
        callback_data=MainCallback(mcb='cart').pack(),
    )
    dfc.button(
        text='В главное меню',
        callback_data=MainCallback(mcb='back').pack(),
    )
    dfc.adjust(1)
    return dfc.as_markup(resize_keyboard=True)


async def edit_profile_keyboard() -> InlineKeyboardMarkup:
    epc = InlineKeyboardBuilder()
    epc.button(
        text='Изменить имя',
        callback_data=MainCallback(mcb='edit_name').pack(),
    )
    epc.button(
        text='Изменить дату рождения',
        callback_data=MainCallback(mcb='edit_birthdate').pack(),
    )
    epc.button(
        text='Изменить телефон',
        callback_data=MainCallback(mcb='edit_tel').pack(),
    )
    epc.button(
        text='Изменить псевдоним пользователя и адрес электронной почты',
        callback_data=MainCallback(mcb='edit_username_email').pack(),
    )
    epc.adjust(1)
    return epc.as_markup(resize_keyboard=True)


async def go_to_profile_keyboard() -> InlineKeyboardMarkup:
    pkb = InlineKeyboardBuilder()
    pkb.button(
        text='В профиль',
        callback_data=MainCallback(mcb='profile').pack(),
    )
    pkb.button(
        text='В главное меню',
        callback_data=MainCallback(mcb='back').pack(),
    )
    pkb.adjust(1)
    return pkb.as_markup(resize_keyboard=True)