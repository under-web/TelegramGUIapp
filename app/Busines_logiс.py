# TODO: написать тесты к функциям
import random
import sys
import time
from telethon.errors import PeerFloodError, FloodWaitError
from telethon.sync import TelegramClient

class Tsm(object):
    def __init__(self):
        self.client = TelegramClient('telethon', 22032145, "4f41399b8956057c331193762780892d").start()
# def get_authentification():
#     global client
#     while True:
#         try:
#             client = TelegramClient('telethon', 22032145, "4f41399b8956057c331193762780892d")  # Настройки прокси
#             client.start()
#             return client
#         except Exception as err:
#             print(err)
#             return client
    def get_send_message(self, target_user=None):
        mode_del = input('Удалять из файла тех кому отправили сообщение? (y/n) ')

        if mode_del == 'y':
            pass
        else:
            mode_del = 'n'
        print(mode_del)

        try:
            timing = int(input('Укажите время задержки между сообщениями в секундах: '))
        except Exception:
            timing = 5

        try:
            limits = int(input('Сколько сообщений отправить?: '))
        except Exception:
            limits = 30

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
        if not target_user:
            while True:
                for user in new_list:
                    try:
                        user_clear = int(user.strip())
                    except Exception:
                        user_clear = user.strip()
                    try:
                        self.client.send_message(user_clear, message=random.choice(self.get_randomazer(message)))
                        if mode_del == 'y':  # удаление
                            new_list.remove(user)
                            print(len(new_list))
                            with open('all_user.txt', 'w', encoding='utf-8', errors='ignore') as f_txt:
                                f_txt.writelines(new_list)
                        print(f'Отправил сообщение в {user}')

                        dead_line += 1
                        print(f'Ждём {timing} секунд')
                        time.sleep(timing)

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
                    if dead_line == limits:
                        input('Готово. Нажмите ENTER для выхода')
                        exit()
                if (mode_del == 'y') and (not new_list):
                    break
                elif mode_del == 'n':
                    break
            print('________________________________________')
            input('Готово. Нажмите ENTER для выхода')
            exit()
    def get_randomazer(self,message):
        block_chain_list = message.split('+++')
        return block_chain_list

    def func_1_parsing(self):
        print('Я работаю - Парсим')


    def func_2_parsing_send(self):
        pass

    def func_3_send_mesg(self):
        self.get_send_message()