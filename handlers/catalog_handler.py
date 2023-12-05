import aiohttp
from bot_settings import config


async def catalog(auth_token: str):
    headers = {'Authorization': f'Token {auth_token}'}
    async with aiohttp.ClientSession() as session:
        async with session.get(config.catalog_url, headers=headers) as response:
            return await response.json()


async def add_to_cart(auth_token: str, food_id: int):
    headers = {'Authorization': f'Token {auth_token}'}
    url = f'{food_id}/add_to_cart/'
    async with aiohttp.ClientSession() as session:
        async with session.get(config.catalog_url + url, headers=headers) as response:
            return await response.json()
