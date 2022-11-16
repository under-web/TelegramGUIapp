import random
import time
from tkinter import *

from telethon.sync import TelegramClient
import asyncio
from telethon.errors import FloodWaitError, PeerFloodError

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import ChannelParticipantsAdmins

from telethon import functions, types, errors


def get_api():
    try:
        with open('api.txt', 'r', encoding='utf8') as auth_file:
            api_data = auth_file.readlines()
        return api_data
    except FileNotFoundError:
        file_ex = open('api.txt', 'w', encoding='utf8')
        file_ex.close()
        api_data = []


def get_authorization():
    global client
    api_data = get_api()
    try:
        client = TelegramClient('MyClient', int(api_data[0].strip()), api_data[1].strip())  # Настройки прокси
        if not client:
            print("Еще не авторизован")
        client.start()
        if client:
            print("авторизован")
        return True
    except Exception as err:
        print(err)
        return False





def clicked():
    print('Отправляю сообщения')
    with open('message.txt', 'r', encoding='utf-8', errors='ignore') as file2_txt:
        message = file2_txt.read()
        if not message:
            input('Файл message.txt пуст! Введите текст для рассылки.')
            sys.exit(0)
    with open('all_user.txt', 'r', encoding='utf-8', errors='ignore') as file_txt:
        new_list = file_txt.readlines()
        if not new_list:
            input('Файл all_user.txt пуст! Введите никнеймы для рассылки.')
            sys.exit(0)

    dead_line = 0

    while True:
        for user in new_list:
            try:
                user_clear = int(user.strip())
            except Exception:
                user_clear = user.strip()
            try:
                client.send_message(user_clear, message=random.choice(message))

                print(f'Отправил сообщение в {user}')

                dead_line += 1


            except PeerFloodError as fl:
                print(
                    'Слишком много запросов к серверу Telegram.Возможно превышены лимиты, подождите или смените '
                    'аккаунт!')
                print(fl)
                input('Нажмите ENTER чтобы закрыть..')
                break

            except FloodWaitError as e:
                print(f'Превышен лимит запросов, сервер вас отсоединил на  {e.seconds} секунд')
                input('Нажмите ENTER чтобы закрыть..')
                break

            except Exception as err:
                if 'Could not find the input entity for PeerUser' in str(err):
                    print(f'Не удалось отправить на {user.strip()} используйте USERNAME для рассылки!')
                    time.sleep(random.randint(5, 10))
                    continue
                else:
                    print(f'Не смог отправить на {user.strip()} ', err)

                    time.sleep(random.randint(5, 10))
                    continue




window = Tk()

window.title("Добро пожаловать в приложение PythonRu")
window.geometry('1x1')
window.resizable(False, False)

lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

btn = Button(window, text="Отправить сообщение!", command=clicked)
btn.grid(column=1, row=0)

btn = Button(window, text="Отправить сообщение!", command=clicked)
btn.grid(column=2, row=0)

while True:
    if get_authorization():
        print('вышел из цикла')
        window.geometry('550x400')
        break

window.mainloop()