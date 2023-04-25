from aiogram import types
from loader import dp
import re
import requests

@dp.message_handler()
async def dog_sender(message: types.Message):
    pattern = 'ple+a+se+'
    if re.search(pattern, message.text.casefold()):
        dog = requests.get('https://random.dog/woof.json')
        await message.answer_photo(dog.json()['url'])
        # await message.answer(dog.json()['url'])
        return
    await message.answer('Be polite')