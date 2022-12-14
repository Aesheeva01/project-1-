from  aiogram import  Bot, Dispatcher, executor, types


TOKEN_API = "5976262148:AAHQLVUPO8FMDsBMNvIxqWUiHuPFZ8jdBlM"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message:types. Message):
    await message.answer(text=message.text)



if __name__ == '__main__':
    executor. start_polling(dp)