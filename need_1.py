from telethon.sync import TelegramClient
from telethon import connection
from selenium import webdriver
import time
import re
import os
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.tl.functions.bots import SetBotCommandsRequest
from telethon.tl.functions import messages
from telethon.tl.functions.messages import SendMessageRequest
# для корректного переноса времени сообщений в json
from telethon.errors.rpcerrorlist import BotResponseTimeoutError
from telethon.tl.functions import GetFutureSaltsRequest
from telethon.tl.custom import messagebutton
import webbrowser
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions import test
import urllib.request
import os
import sqlite3
s = 0
sess = 'Armian'
while s != 1:
    api_id = '1403015'
    api_hash = 'a42142a28f0d44bc1cb524ca86948ee6'
    n = 0
    client = TelegramClient(sess, api_id, api_hash)
    client.start()
    dlgs = client.get_dialogs()
    #class RunChromeTests():
    #    def testMethod(self):
    #        selenium_url = f"http://localhost:4444/wd/hub"
    #        caps = {'browserName': 'chrome'}
    #        driver = webdriver.Remote(command_executor=selenium_url, desired_capabilities=caps)
    #        driver.maximize_window()
    #        driver.get(url_rec)
    #        time.sleep(30)
    #        driver.close()
    #        driver.quit()
    async def Val():
        n = 0
        for dlg in dlgs:
            if dlg.title == 'Valley of money | VIEWS':
                ms = dlg
                c = 0
        while n != 1:
            n += 1
            all_mess = client.get_messages(ms, limit=100000)
            for message in await all_mess:
                if message.reply_markup is not None:
                    texts = message.reply_markup.rows[0].buttons[0].text
                    if texts == '💰' or texts == '💰 +0.03RUB':
                        button_data = message.reply_markup.rows[0].buttons[0].data
                        message_id = message.id
                        print(button_data, message_id)
                        resp = await client(messages.GetBotCallbackAnswerRequest(
                            ms,
                            message_id,
                            data=button_data
                        ))
                        print(resp)
                        if resp.message != 'Вы уже просматривали этот пост!' and resp != 'Задание недоступно!':
                            print(resp.message)
                            c += 1
                    else:
                        print('None')
        print(c)
        if c == 800:
            for dlg in dlgs:
                if dlg.title == 'Valley of Money':
                    ms = dlg
                    print(dlg)
            await client.send_message('Valley of Money', "📱 Мой кабинет")
            time.sleep(20)
            all_mess = client.get_messages(ms, limit=1)
            await client.send_message('Valley of Money', "+7983*******")
            time.sleep(12)
            await client.send_message('Valley of Money', "16")
        return
    async def Perf():
        n = 0
        c = 0
        for dlg in dlgs:
            if dlg.title == 'Flibasta1bot просмотры':
                ms = dlg
        while n != 1:
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
                            print(resp)
                            if resp.message != 'Вы уже просматривали этот пост!' and resp != 'Задание недоступно!':
                                print(resp.message)
                                c += 1
                    else:
                        print('None')

        for dlg in dlgs:
            if dlg.title == 'FlibastaBot - 💵Заработай 🎯Раскрути Канал или Бота':
                ms = dlg
                print(dlg)
        time.sleep(20)
        await client.send_message('FlibastaBot - 💵Заработай 🎯Раскрути Канал или Бота', "+7983*******")
        time.sleep(12)
        await client.send_message('FlibastaBot - 💵Заработай 🎯Раскрути Канал или Бота', "20")
        return

    async def flib():
        n = 0
        for dlg in dlgs:
            if dlg.title == 'Flibasta канал':
                ms = dlg
                c = 0
        while n != 1:
            n += 1
            all_mess = client.get_messages(ms, limit=10000)
            att = 21966
            for message in await all_mess:
                if message.reply_markup is not None:
                    texts = message.reply_markup.rows[0].buttons[0].text
                    message_id = message.id
                    if texts == '💰' or texts == '💰 +0.03RUB' or texts == '💰 +0.02RUB':
                        button_data = message.reply_markup.rows[0].buttons[0].data
                        message_id = message.id
                        if message_id == att:
                            att -= 2
                            print('Nnone')
                        else:
                            print(button_data, message_id)
                            resp = await client(messages.GetBotCallbackAnswerRequest(
                                ms,
                                message_id,
                                data=button_data
                            ))
                            print(resp)
                    else:
                        print('None')
                        if message_id == att:
                            att -= 2
        for dlg in dlgs:
            if dlg.title == 'FlibastaBot - 🚀Раскрутка и 💰Заработок':
                ms = dlg
                print(dlg)
        time.sleep(20)
        await client.send_message('FlibastaBot - 🚀Раскрутка и 💰Заработок', "+7983*******")
        time.sleep(12)
        await client.send_message('FlibastaBot - 🚀Раскрутка и 💰Заработок', "15")
        return

    async def perf_sub():
        n = 0
        for dlg in dlgs:
            if dlg.title == 'Продвижение и заработок 👑 ™LIID':
                ms = dlg
                print(dlg)
        while n != 1:
            n += 1
            all_mess = client.get_messages(ms, limit=1)
            print(all_mess)
            for message in await all_mess:
                if message.reply_markup is not None:
                    texts = message.reply_markup.rows[0].buttons[0].text
                    print(texts)
                    if texts == '1️⃣ Перейти к каналу':
                        button_data = message.reply_markup.rows[0].buttons[0].url
                        message_id = message.id
                        print(button_data)
                    else:
                        print('None')
                    channel = await client(JoinChannelRequest(button_data))
                    all = await client.get_messages(button_data, limit=20)
                    for dlg in dlgs:
                        if dlg.title == 'Продвижение и заработок 👑 ™LIID':
                            ms = dlg
                            print(dlg)

                    all_mess = await client.get_messages(ms, limit=1)
                    print(all_mess)
                    for mess in all_mess:
                        if mess.reply_markup is not None:
                            texts = mess.reply_markup.rows[1].buttons[0].text
                            print(texts)
                            if texts == '2️⃣ Проверить подписку':
                                button_data = mess.reply_markup.rows[1].buttons[0]
                                message_id = mess.id
                                resp = await client(messages.GetBotCallbackAnswerRequest(
                                    ms,
                                    message_id,
                                    data=ms
                                ))
                            else:
                                print('None')
        return
    #async def ltc():
    #    for dlg in dlgs:
    #        if dlg.title == 'LTC Click Bot':
    #            tegmo = dlg
    #            print(tegmo)
    #    await client.send_message('LTC Click Bot', "🖥 Visit sites")
    #    time.sleep(20)
    #    msgs = client.get_messages(tegmo, limit=1)
    #    for mes in await msgs:
    #        print("Найдено reward")
    #        str_a = str(mes.message)
    #        zz = str_a.replace('You must stay on the site for', '')
    #        qq = zz.replace('seconds to get your reward.', '')
    #        await client.send_message('LTC Click Bot', "/visit")
    #        time.sleep(3)
    #        msgs2 = client.get_messages(tegmo, limit=1)
    #        for mes2 in await msgs2:
    #            button_data = mes2.reply_markup.rows[0].buttons[0].text
    #            print(button_data)
    #            message_id = mes2.id
    #            print("Перехожу по ссылке")
    #            time.sleep(2)
    #            url_rec = str(mes2.reply_markup.rows[0].buttons[0].url)
    #            ch = RunChromeTests()
    #            ch.testMethod()
    #            time.sleep(6)
    #            fp = urllib.request.urlopen(url_rec)
    #            mybytes = fp.read()
    #            mystr = mybytes.decode("utf8")
    #            fp.close()
    #            if re.search(r'\bSwitch to reCAPTCHA\b', mystr):
    #                from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
    #                resp = client(GetBotCallbackAnswerRequest(
    #                    'LTC Click Bot',
    #                    message_id,
    #                    data=button_data
    #                ))
    #                print(resp)
    #                time.sleep(2)
    #                print("КАПЧА!")
    #
    #    return
    async def main():
        #await Val()
        await Perf()
        #await flib()
        #await perf_sub()
        #await ltc()

    with client:
        s += 1
        client.loop.run_until_complete(main())
