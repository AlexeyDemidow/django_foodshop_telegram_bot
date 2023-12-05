import aiohttp
from bot_settings import config


async def cart(auth_token: str):
    headers = {'Authorization': f'Token {auth_token}'}
    async with aiohttp.ClientSession() as session:
        async with session.get(config.cart_url, headers=headers) as response:
            return await response.json()


async def delete_from_cart(auth_token: str, cart_item_id: int):
    headers = {'Authorization': f'Token {auth_token}'}
    cart_item = f'{cart_item_id}/delete_from_cart/'
    async with aiohttp.ClientSession() as session:
        async with session.get(config.cart_url + cart_item, headers=headers) as response:
            return await response.json()


async def minus_from_cart(auth_token: str, cart_item_id: int):
    headers = {'Authorization': f'Token {auth_token}'}
    cart_item = f'{cart_item_id}/minus_cart_quantity/'
    async with aiohttp.ClientSession() as session:
        async with session.get(config.cart_url + cart_item, headers=headers) as response:
            return await response.json()
