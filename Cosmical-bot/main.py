from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests

token = '1579563970:AAHvSjjEmvjxY6N_lpoZXtUf3IFNE-xelmI' # Ключ


bot = Bot(token)
dp = Dispatcher(bot)
@dp.message_handler(content_types=['text'])
async def main(message : types.Message):
	if message.text == 'Фото':
        response = requests.get("http://127.0.0.1:8080/")
        file = open("sample_image.jpg", "wb")
        file.write(response.content)
        file.close()
        print ("123444")
        photo = r'G:\Program Files (x86)\Cosmical-bot\sample_image.jpg'.format(os.getcwd())
        img = open(photo)
        print(img)
        bot.send_photo(message.from_user.id, photo=img)



if __name__ == '__main__':
    executor.start_polling(dp)
