import aiohttp
from bot_settings import config


async def authorisation(username: str, password: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(config.auth_url, json={'username': username, 'password': password}) as response:
            return await response.json()


async def profile(auth_token: str):
    headers = {'Authorization': f'Token {auth_token}'}
    async with aiohttp.ClientSession() as session:
        async with session.get(config.profile_url, headers=headers) as response:
            return await response.json()


async def account(auth_token: str):
    headers = {'Authorization': f'Token {auth_token}'}
    async with aiohttp.ClientSession() as session:
        async with session.get(config.account_url, headers=headers) as response:
            return await response.json()


async def edit_profile_customer_name(auth_token: str, customer_id: int, customer_name: str):
    headers = {'Authorization': f'Token {auth_token}'}
    name = {'customer_name': customer_name}
    cusomer_url = f'{customer_id}/'
    async with aiohttp.ClientSession() as session:
        async with session.put(config.profile_url + cusomer_url, headers=headers, json=name) as response:
            return await response.json()


async def edit_profile_customer_birthdate(auth_token: str, customer_id: int, customer_birthdate: str):
    headers = {'Authorization': f'Token {auth_token}'}
    birthdate = {'date_of_birth': customer_birthdate}
    customer_url = f'{customer_id}/'
    async with aiohttp.ClientSession() as session:
        async with session.put(config.profile_url + customer_url, headers=headers, json=birthdate) as response:
            return await response.json()


async def edit_profile_customer_telephone(auth_token: str, customer_id: int, customer_telephone: str):
    headers = {'Authorization': f'Token {auth_token}'}
    telephone = {'telephone': customer_telephone}
    customer_url = f'{customer_id}/'
    async with aiohttp.ClientSession() as session:
        async with session.put(config.profile_url + customer_url, headers=headers, json=telephone) as response:
            return await response.json()


async def edit_profile_customer_email(auth_token: str, customer_id: int, customer_username: str, customer_email: str):
    headers = {'Authorization': f'Token {auth_token}'}
    username_email = {'username': customer_username, 'email': customer_email}
    customer_url = f'{customer_id}/'
    async with aiohttp.ClientSession() as session:
        async with session.put(config.account_url + customer_url, headers=headers, json=username_email) as response:
            return await response.json()
