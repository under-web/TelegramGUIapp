# TODO: написать тесты к функциям
import os
import random
import sys
import time
from telethon.errors import PeerFloodError, FloodWaitError
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest, InviteToChannelRequest, JoinChannelRequest
from telethon.tl.types import ChannelParticipantsSearch, ChannelParticipantsAdmins


class Tsm(object):
    def __init__(self):
        self.client = TelegramClient('telethon', 9129594, "4f41399b8956057c331193762780892d").start()

    def _get_account_phone(self):
        print('[Режим парсинга Телефонов]')
        try:
            timing = int(input('Выберите время паузы в секундах: '))
        except Exception:
            timing = 5

        offset_user = 0
        limit_user = 100

        all_participants = []
        filter_user = ChannelParticipantsSearch('')

        with open('file_channel.txt', 'r', encoding='utf8', errors='ignore') as file_all_channel:
            for channel in file_all_channel.readlines():
                print(f'Обращаюсь к {channel}')
                while True:
                    participants = await self.client(GetParticipantsRequest(channel,
                                                                       filter_user, offset_user, limit_user, hash=0))
                    if not participants.users:
                        break
                    all_participants.extend(participants.users)
                    offset_user += len(participants.users)
                    time.sleep(2)
                all_users_details = []  # список словарей с интересующими параметрами участников канала

                for participant in all_participants:
                    all_users_details.append({"id": participant.id,
                                              "first_name": participant.first_name,
                                              "last_name": participant.last_name,
                                              "user": participant.username,
                                              "phone": participant.phone,
                                              "is_bot": participant.bot})

                with open('phones.txt', 'a', encoding='utf8') as out_user_file:
                    for pos in all_users_details:
                        if str(pos.get("phone")) == 'None':
                            continue
                        else:
                            out_user_file.write(str(pos.get("phone")) + '\n')
                time.sleep(timing)
        print('Телефоны юзеров сохранились в файле phones.txt')


    def _get_parsing_admins(self):
        print('[Режим парсинга Администраторов]')
        try:
            timing = int(input('Выберите время паузы в секундах: '))
        except Exception:
            timing = 5
        list_admin = []
        try:
            with open('file_channel.txt', 'r', encoding='utf8', errors='ignore') as file_all_channel:
                for channel in file_all_channel.readlines():
                    print(f'Обращаюсь к {channel}')
                    try:
                        for user in self.client.iter_participants(channel.strip(), filter=ChannelParticipantsAdmins):
                            print(user.username)
                            if user.username:
                                list_admin.append(user.username + '\n')
                        print(f'Ждем {timing} секунд')
                        time.sleep(timing)
                    except Exception:
                        print('..')
                        continue
            with open('all_user.txt', 'a', encoding='utf8', errors='ignore') as file_admin:
                file_admin.writelines(list_admin)
        except Exception as e:
            print('[8] Что то пошло не так..', e)
        print('Администраторы сохранились в файле all_user.txt')
    def _send_file_message(self):
        with open('all_user.txt', 'r', encoding='utf8', errors='ignore') as file_users:
            users = file_users.readlines()
            for user in users:
                try:
                    self._send_file(user, mode_sand=True)
                except Exception as e:
                    print(e)
                    time.sleep(5)


    def _send_file(self, mode_sand=False):
        try:
            timing = int(input('Укажите время задержки между сообщениями в секундах: '))
        except:
            timing = 5
        with open('all_user.txt', 'r', encoding='utf8', errors='ignore') as file_users:
            users = file_users.readlines()
            dirname = r'dir/'
            path_file = dirname + ''.join(os.listdir(dirname))
            for user in users:
                try:
                    await self.client.send_file(user, path_file)
                    print(f'Отправил файл {user}')
                    if mode_sand:
                        self._get_send_message(user)
                except Exception as e:
                    print('Не удалось отправить файл', e)
                print(f'Ждем {timing} секунд')
                time.sleep(timing)
    def _get_join_channel(self):
        print('Выбран режим присоединения')
        try:
            timing = int(input('Укажите время задержки между присоединениями в секундах: '))
        except Exception:
            timing = 5

        try:
            with open('file_channel.txt', 'r', encoding='utf-8', errors='ignore') as file_txt:
                for channel in file_txt.readlines():
                    try:
                        await self.client(JoinChannelRequest(channel.strip()))
                        print(f'Присоединился к {channel}')
                        time.sleep(timing)
                    except FloodWaitError as e:
                        print('Flood waited for', e.seconds)
                        input('Нажмите ENTER чтобы закрыть..')
                    except Exception as err:
                        print(f'Не смог подсоединиться {channel}', err)
                        time.sleep(timing)
        except Exception as e:
            print(e)

    def _get_invite_channel(self):
        with open('file_channel.txt', 'r') as file_chanel:
            channels = file_chanel.readlines()
        with open('all_user.txt', 'r') as file_users:
            users = file_users.readlines()
        timing = input('Введите паузу между добавлениями (сек): ')
        for channel in channels:
            print(f'Добавляю пользователей в {channel}')
            for usr in users:
                try:
                    await self.client(InviteToChannelRequest(channel=channel, users=[usr]))
                    print(f'Добавил {usr}')
                    time.sleep(int(timing))
                except Exception as e:
                    print('Не смог добавить, причина -', e)
                    time.sleep(random.randint(5, 9))

    def _delete_duplicate(self):
        with open('all_user.txt', 'r', encoding='utf8', errors='ignore') as file_duplicate:
            all_data_users = set(file_duplicate.readlines())
            print('Всего юзеров', len(all_data_users), 'записано в файле all_user.txt')
        os.remove('all_user.txt')
        with open('all_user.txt', 'w', encoding='utf8', errors='ignore') as file_write:
            for i in list(set(all_data_users)):
                file_write.write(i)
    def _dumper_all_participants(self):
        mod_user = input('''
                  [1] - Получить ID 
                  [2] - Получить USERNAME (Выбрать 1 или 2): ''')
        print('')

        with open('file_channel.txt') as file_all_channel:
            for url in file_all_channel.readlines():
                channel = await self.client.get_entity(url)

                if mod_user.strip() == '1':
                    print(f'Собираю ID пользователей {url}')
                else:
                    print(f'Собираю USERNAME пользователей {url}')

                offset_user = 0  # номер участника, с которого начинается считывание
                limit_user = 100  # максимальное число записей, передаваемых за один раз

                all_participants = []  # список всех участников канала
                filter_user = ChannelParticipantsSearch('')

                while True:
                    participants = await self.client(GetParticipantsRequest(channel,
                                                                            filter_user, offset_user, limit_user,
                                                                            hash=0))
                    if not participants.users:
                        break
                    all_participants.extend(participants.users)
                    offset_user += len(participants.users)
                    time.sleep(2)
                all_users_details = []  # список словарей с интересующими параметрами участников канала

                if mod_user.strip() == '1':
                    for participant in all_participants:
                        all_users_details.append({"id": participant.id,
                                                  "first_name": participant.first_name,
                                                  "last_name": participant.last_name,
                                                  "user": participant.username,
                                                  "phone": participant.phone,
                                                  "is_bot": participant.bot})

                    with open('all_user.txt', 'a', encoding='utf8') as out_user_file:
                        for pos in all_users_details:
                            if str(pos.get("id")) == 'None':
                                continue
                            else:
                                out_user_file.write(str(pos.get("id")) + '\n')


                elif mod_user.strip() == '2':
                    for participant in all_participants:
                        all_users_details.append({"id": participant.id,
                                                  "first_name": participant.first_name,
                                                  "last_name": participant.last_name,
                                                  "user": participant.username,
                                                  "phone": participant.phone,
                                                  "is_bot": participant.bot})

                    with open('all_user.txt', 'a', encoding='utf8') as out_user_file:
                        for pos in all_users_details:
                            if str(pos.get("user")) == 'None':
                                continue
                            else:
                                out_user_file.write(str(pos.get("user")) + '\n')

            print('________________________________________')
            input('Готово. Нажмите любую клавишу для выхода')
    def _get_send_message(self, target_user=None):
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
                        self.client.send_message(user_clear, message=random.choice(self._get_randomazer(message)))
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
    def _get_randomazer(self,message):
        block_chain_list = message.split('+++')
        return block_chain_list

    def func_1_parsing(self):
       self._dumper_all_participants()


    def func_2_parsing_send(self):
        self._dumper_all_participants()
        self._delete_duplicate()
        self._get_send_message()
    def func_3_send_mesg(self):
        self._get_send_message()

    def func_4_join_group(self):
        self._get_join_channel()
    def func_5_invite(self):
       self._get_invite_channel()

    def func_6_send_file(self):
        self._send_file()

    def func_7_send_file_message(self):
        self._send_file_message()

    def func_8_parsing_admin(self):
        self._get_parsing_admins()

    def func_9_check_phone(self):
        self._get_account_phone()
