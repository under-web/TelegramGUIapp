# 'coding: utf-8'
import json
import os
import logging
import random
import socket
import time
import sys
# для корректного переноса времени сообщений в json
from datetime import datetime
import asyncio
from telethon.errors import FloodWaitError, PeerFloodError

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import ChannelParticipantsAdmins


from telethon import functions, types, errors
from telethon.sync import TelegramClient

graf = """                
  _____         _   ___                   _               __  __            _ 
 |_   _|  ___  | | / __|  ___   _ _    __| |  ___   _ _  |  \/  |  ___   __| |
   | |   / -_) | | \__ \ / -_) | ' \  / _` | / -_) | '_| | |\/| | / _ \ / _` |
   |_|   \___| |_| |___/ \___| |_||_| \__,_| \___| |_|   |_|  |_| \___/ \__,_|
 ----------------------------------------------------------------------------------
 Автор: Artem K     My Telegram: @artymeus                   (LXI)   v0.6.2
 ----------------------------------------------------------------------------------"""

print(graf)
print('[1]-Извлечениe (id/nickname) пользователей групп.')
print('[2]-Извлечение пользователей (id/nickname) , с последующей отправкой сообщений.')
print('[3]-Только отправка сообщения. ')
print('[4]-Присоединяться к группам. ')
print('[5]-Добавлять пользователей в канал - INVITE (работает только по USERNAME).')
print('[6]-Отправить только  файл  (из папки dir/), пользователям.')
print('[7]-Отправить  файл  (из папки dir/) и текст-сообщение пользователям.')
print('[8]-Извлечь Администраторов группы (из file_channel --> all_user.txt).')
print('[9]-Извлечь номера телефонов участников групп (из file_channel --> all_user.txt).')
print('[10]- Чекер номеров телефонов на наличие аккаунта телеграм (из phones.txt --> all_user.txt).')
logging.disable(level=logging.CRITICAL)


def connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


# while True:
#     if connected():
#         break
#     else:
#         print('ОШИБКА: Проблемы с подключением проверьте настройки сети, прокси или vpn')
#         input()
#
# try:
#     put_ftp()
# except Exception as err:
#     print('Возможны проблемы обратитесь к разработчику (code 9)', err)
#
# try:
#     os.remove('win.txt')
# except Exception:
#     pass
#
# while True:
#     if get_html_lic():
#         break
#     else:
#         time.sleep(2)
#         input()

while True:
    print(' "Используя данную программу вы соглашаетесь с договором офертой-> http://pythonbot.tilda.ws/offerta" ')
    mode_work = input('Введите цифру от 1 до 10 : ').strip()

    if mode_work == '1':
        break
    elif mode_work == '2':
        break
    elif mode_work == '3':
        break
    elif mode_work == '4':
        break
    elif mode_work == '5':
        break
    elif mode_work == '6':
        break
    elif mode_work == '7':
        break
    elif mode_work == '8':
        break
    elif mode_work == '9':
        break
    elif mode_work == '10':
        break
    else:
        print(f'{mode_work} значение некорректно! Введите цифру от 1 до 10')

try:
    with open('api.txt', 'r', encoding='utf8') as auth_file:
        api_data = auth_file.readlines()
except FileNotFoundError:
    file_ex = open('api.txt', 'w', encoding='utf8')
    file_ex.close()
    api_data = []

try:
    client = TelegramClient('MyClient', int(api_data[0].strip()), api_data[1].strip())  # Настройки прокси
    client.start()
    if not client.is_user_authorized():
        client.sign_in(password=input('Password: '))
except IndexError as e:
    client = None
    print('Возможно файл api.txt пуст или данные [api_id api_hash] введены некорректно!')
    input()

except Exception as e:
    if 'SendCodeRequest' in str(e):
        print('Некорректные [api id api hash] (code 7) ')
        input()


async def delete_duplicate():
    with open('all_user.txt', 'r', encoding='utf8', errors='ignore') as file_duplicate:
        all_data_users = set(file_duplicate.readlines())
        print('Всего юзеров', len(all_data_users), 'записано в файле all_user.txt')
    os.remove('all_user.txt')
    with open('all_user.txt', 'w', encoding='utf8', errors='ignore') as file_write:
        for i in list(set(all_data_users)):
            file_write.write(i)


async def dumper_all_participants():
    mod_user = input('''
    [1] - Получить ID 
    [2] - Получить USERNAME (Выбрать 1 или 2): ''')
    print('')

    with open('file_channel.txt') as file_all_channel:
        for url in file_all_channel.readlines():
            channel = await client.get_entity(url)

            if mod_user.strip() == '1':
                print(f'Собираю ID пользователей {url}')
            else:
                print(f'Собираю USERNAME пользователей {url}')

            offset_user = 0  # номер участника, с которого начинается считывание
            limit_user = 100  # максимальное число записей, передаваемых за один раз

            all_participants = []  # список всех участников канала
            filter_user = ChannelParticipantsSearch('')

            while True:
                participants = await client(GetParticipantsRequest(channel,
                                                                   filter_user, offset_user, limit_user, hash=0))
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

                # сбрасывает данные в формате JSON
                # with open('channel_users.json', 'w', encoding='utf8') as outfile:
                #     json.dump(all_users_details, outfile, ensure_ascii=False)
                # сбрасывает данные только имена юзеров
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

                # сбрасывает данные в формате JSON
                # with open('channel_users.json', 'w', encoding='utf8') as outfile:
                #     json.dump(all_users_details, outfile, ensure_ascii=False)
                # сбрасывает данные только имена юзеров
                with open('all_user.txt', 'a', encoding='utf8') as out_user_file:
                    for pos in all_users_details:
                        if str(pos.get("user")) == 'None':
                            continue
                        else:
                            out_user_file.write(str(pos.get("user")) + '\n')

        print('________________________________________')
        input('Готово. Нажмите любую клавишу для выхода')
        exit()


async def dumper_all_messages(channel):
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    offset_msg = 0  # номер записи, с которой начинается считывание
    limit_msg = 100  # максимальное число записей, передаваемых за один раз

    all_messages = []  # список всех сообщений
    total_messages = 0
    total_count_limit = 0  # поменяйте это значение, если вам нужны не все сообщения

    class DateTimeEncoder(json.JSONEncoder):
        """Класс для сериализации записи дат в JSON"""

        def default(self, o):
            if isinstance(o, datetime):
                return o.isoformat()
            if isinstance(o, bytes):
                return list(o)
            return json.JSONEncoder.default(self, o)

    while True:
        history = await client(GetHistoryRequest(
            peer=channel,
            offset_id=offset_msg,
            offset_date=None, add_offset=0,
            limit=limit_msg, max_id=0, min_id=0,
            hash=0))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
        offset_msg = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break

    with open('channel_messages.json', 'w', encoding='utf8') as outfile:
        json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)


#
def get_randomazer(message):
    block_chain_list = message.split('+++')
    return block_chain_list


async def get_send_message(target_user=None):
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
                    await client.send_message(user_clear, message=random.choice(get_randomazer(message)))
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

    else:
        while True:
            try:
                user_clear = int(target_user.strip())
            except Exception:
                user_clear = target_user.strip()

            try:
                await client.send_message(user_clear, message=random.choice(message))
                if mode_del == 'y':
                    new_list.remove(target_user)
                    with open('all_user.txt', 'w', encoding='utf-8', errors='ignore') as f_txt:
                        f_txt.writelines(new_list)
                print(f'Отправил сообщение в {target_user}')

                dead_line += 1
                print(f'Ждём {timing} секунд')
                time.sleep(timing)

            except PeerFloodError as fl:
                print('Слишком много запросов к серверу Telegram, подождите или смените аккаунт!')
                print(fl)
                input('Нажмите ENTER чтобы закрыть..')
                break

            except FloodWaitError as e:
                print(f'Превышен лимит запросов сервер вас отсоединил на  {e.seconds} секунд')
                input('Нажмите ENTER чтобы закрыть..')
                break

            except Exception as err:
                if 'Could not find the input entity for PeerUser' in str(err):
                    print(f'Не удалось отправить на {user_clear.strip()} используйте USERNAME для рассылки!')
                    time.sleep(random.randint(5, 10))
                    continue
                else:
                    print(f'Не смог отправить на {user_clear.strip()} ', err)

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


async def join_channel(client):
    print('Выбран режим присоединения')
    try:
        timing = int(input('Укажите время задержки между присоединениями в секундах: '))
    except Exception:
        timing = 5

    try:
        with open('file_channel.txt', 'r', encoding='utf-8', errors='ignore') as file_txt:
            for channel in file_txt.readlines():
                try:
                    await client(JoinChannelRequest(channel.strip()))
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


async def get_invite_channel():
    with open('file_channel.txt', 'r') as file_chanel:
        channels = file_chanel.readlines()
    with open('all_user.txt', 'r') as file_users:
        users = file_users.readlines()
    timing = input('Введите паузу между добавлениями (сек): ')
    for channel in channels:
        print(f'Добавляю пользователей в {channel}')
        for usr in users:
            try:
                await client(InviteToChannelRequest(channel=channel, users=[usr]))
                print(f'Добавил {usr}')
                time.sleep(int(timing))
            except Exception as e:
                print('Не смог добавить, причина -', e)
                time.sleep(random.randint(5, 9))


async def get_send_file(user):
    dirname = r'dir/'
    path_file = dirname + ''.join(os.listdir(dirname))
    try:
        await client.send_file(user, path_file)
        print(f'Отправил файл {user}')
    except Exception as e:
        print('Не удалось отправить файл', e)


async def get_sand_mes_file(user, message):
    try:
        await client.send_message(user, message=message)
        print(f'Отправил сообщение в {user}')

    except FloodWaitError as e:
        print(f'Превышен лимит запросов сервер вас отсоединил на  {e.seconds} секунд')
        input('Нажмите ENTER чтобы закрыть..')

    except Exception as err:
        if 'Could not find the input entity for PeerUser' in str(err):
            print(f'Не удалось отправить на {user.strip()} используйте USERNAME для рассылки!')

        else:
            print(f'Не смог отправить на {user.strip()} ', err)


async def get_send_phone(total_list_phone, timing):
    for number in total_list_phone:
        try:  # Добавляем контакт
            result = await client(functions.contacts.ImportContactsRequest(
                contacts=[types.InputPhoneContact(
                    client_id=random.randrange(-2 ** 63, 2 ** 63),
                    first_name=number,
                    last_name='',
                    phone=number
                )]
            ))
            # Если импорт успешен
            if len(result.imported) > 0:
                user = result.users[0]
                # Если в конфиге параметр send_user = True, то контакт отправляется в раздел "Избранное"

                # await client.send_file("me", types.InputMediaContact(
                #     phone_number=number,
                #     first_name=number,
                #     last_name='',
                #     vcard=''
                # ))
                # Получаем информацию о контакте
                result = await client(functions.contacts.GetContactsRequest(
                    hash=0
                ))
                # Удаление контакта
                await client(functions.contacts.DeleteContactsRequest(id=result.users))
                # Получаем информацию о только что удалённом контакте.
                full_user = await client(
                    functions.users.GetFullUserRequest(id=user))
                # Контакт получен, основная часть закончена

                # По желанию, выводим инфу о юзере на экран
                print_user(full_user)
                await asyncio.sleep(5)

            else:
                #  Если импорт без результата:
                print('Упс... Такого контакта в TG не обнаружено.')
                await asyncio.sleep(timing)
        except errors.FloodWaitError as e:
            print(f'Вы получили ограничение на испольование API на {e.seconds} секунд')
            time.sleep(e.seconds)


def get_save_username(username):
    if username:
        print(username)
        try:
            with open('all_user.txt', 'a', encoding='utf8', errors='ignore') as user_file:
                user_file.write(username + '\n')
        except Exception as e:
            print(e)


def print_user(full_user):
    '''
    Функция для вывода информации об импортируемом номере
    '''

    full_user = full_user.user
    # Разбиваем основную инфу по переменным
    user_id = full_user.id
    name = full_user.first_name
    if full_user.last_name is not None:
        name = f'{name} {full_user.last_name}'
    if full_user.username is not None:
        username = full_user.username
    else:
        username = ''
    # phone = full_user.phone
    # print(f'ID пользователя: {user_id}\n'
    #       f'Имя пользователя: {name}\n'
    #       f'Username: {username}\n'
    #       f'Номер телефона: {phone}\n')
    get_save_username(username)



async def main(mode_work):
    if mode_work == '1':
        await dumper_all_participants()

    elif mode_work == '2':
        await dumper_all_participants()
        await delete_duplicate()
        await get_send_message()

    elif mode_work == '3':
        await get_send_message()

    elif mode_work == '4':
        await join_channel(client)


    elif mode_work == '5':
        await get_invite_channel()

    elif mode_work == '6':
        try:
            timing = int(input('Укажите время задержки между сообщениями в секундах: '))
        except:
            timing = 5
        with open('all_user.txt', 'r', encoding='utf8', errors='ignore') as file_users:
            users = file_users.readlines()
            for user in users:
                try:
                    await get_send_file(user)
                except Exception as e:
                    print(e)
                    time.sleep(5)
                print(f'Ждем {timing} секунд')
                time.sleep(timing)

    elif mode_work == '7':
        try:
            timing = int(input('Укажите время задержки между сообщениями в секундах: '))
        except:
            timing = 5
        with open('all_user.txt', 'r', encoding='utf8', errors='ignore') as file_users:
            users = file_users.readlines()
        with open('message.txt', 'r', encoding='utf-8', errors='ignore') as file2_txt:
            message = file2_txt.read()
            for user in users:
                try:
                    await get_send_file(user)
                    await get_sand_mes_file(user, message)

                except Exception as e:
                    print(e)
                    time.sleep(5)
                print(f'Ждем {timing} секунд')
                time.sleep(timing)

    elif mode_work == '8':
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
                        async for user in client.iter_participants(channel.strip(), filter=ChannelParticipantsAdmins):
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
        input('Нажмите ENTER для выхода')

    elif mode_work == '9':
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
                    participants = await client(GetParticipantsRequest(channel,
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
        input('Нажмите ENTER для выхода')

    elif mode_work == '10':
        try:
            timing = int(input('Выберите время паузы в секундах: '))
        except Exception:
            timing = 5
        with open('phones.txt', 'r', encoding='UTF8', errors='ignore') as ph_file:
            total_list_phone = ph_file.readlines()
        await get_send_phone(total_list_phone, timing)


# await dump_all_messages(channel) // собирает все сообщения


with client:
    try:
        client.loop.run_until_complete(main(mode_work))
    except Exception as err:
        print('main()', err)
        print('')
        input('Нажмите ENTER для выхода')
