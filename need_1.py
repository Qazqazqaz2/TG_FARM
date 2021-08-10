from telethon.sync import TelegramClient
from telethon import connection
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.tl.functions import messages
s = 0
sess = 'Name_session'
api_id = '#######'
api_hash = '#################'
client = TelegramClient(sess, api_id, api_hash)
client.start()
dlgs = client.get_dialogs()

async def Farm():
    n = 0
    c = 0
    for dlg in dlgs:
        if dlg.title == 'Flibasta1bot просмотры':
            ms = dlg
        n += 1
        all_mess = client.get_messages(ms, limit=13000)
        for message in await all_mess:
            if message.reply_markup is not None:
                texts = message.reply_markup.rows[0].buttons[0].text
                if texts == '💰' or texts == '💰 +0.03RUB' or texts == '💰 +0.02RUB':
                        button_data = message.reply_markup.rows[0].buttons[0].data
                        message_id = message.id
                        print(button_data, message_id)
                        resp = await client(messages.GetBotCallbackAnswerRequest(
                            ms,
                            message_id,
                            data=button_data
                        ))
                        if resp.message != 'Вы уже просматривали этот пост!' and resp != 'Задание недоступно!':
                            print(resp.message)
                            c += 1
                else:
                    print('None')

        for dlg in dlgs:
            if dlg.title == 'FlibastaBot - 💵Заработай 🎯Раскрути Канал или Бота':
                ms = dlg
        time.sleep(10)
        await client.send_message('FlibastaBot - 💵Заработай 🎯Раскрути Канал или Бота', "+7983*******")
        time.sleep(5)
        await client.send_message('FlibastaBot - 💵Заработай 🎯Раскрути Канал или Бота', "20")
  
    async def main():
        await Farm()

    with client:
        s += 1
        client.loop.run_until_complete(main())
