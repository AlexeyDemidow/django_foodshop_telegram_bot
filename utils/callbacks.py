from aiogram.filters.callback_data import CallbackData


class MainCallback(CallbackData, prefix='main_callback'):
    mcb: str


class CartCallback(CallbackData, prefix='cart_callback'):
    ccb: str
    food_id: int
