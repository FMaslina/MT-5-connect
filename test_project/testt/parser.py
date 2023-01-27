import pygsheets
import sqlite3


def init(secret_path, sheet_name):
    """Авторизация через client_secret.json файл(ВАЖНО! При первом подключении просить подтвердить по ссылке и дать
    права), получение необходимой таблицы по названию """
    gc = pygsheets.authorize(client_secret=secret_path)
    sh = gc.open(sheet_name)
    wks = sh.sheet1
    return wks


def get_all_table_data(wks):      # Получение всех данных с таблицы, последний получаемый столбец - "Канал"
    data_list = []
    for row in wks.get_all_values():
        data_list.append(row[:4])
    return data_list


def get_row_data_by_id(data):      # Создание словаря {bothelp_id: Аккаунт}
    accounts = {}
    for row in data:
        if row[0] == 'BotHelp ID':
            continue
        accounts[row[0]] = row[1]
    return accounts


def update_db_record(data):
    con = sqlite3.connect(database='../db.sqlite3')     # Подключение к бд
    cursor = con.cursor()
    for key, value in data.items():     # Проходимся по всем аккаунтам в таблице
        try:    # Конструкция try except для проверки, переводится ли значение поля "Аккаунт" в число
            int(value)
            data_for_add = (value, key)     # Кортеж данных для вставки в запрос к бд
            cursor.execute('UPDATE testt_botusermodel SET id_telegram = ? WHERE id_bothelp = ?;', data_for_add)
            con.commit()    # Сохранение изменений
        except ValueError:
            data_for_add = (value, key)
            cursor.execute('UPDATE testt_botusermodel SET username = ? WHERE id_bothelp = ?;', data_for_add)
            con.commit()
    cursor.close()
    con.close()


wks = init('./client_secret.json', 'Testt')
table_data = get_all_table_data(wks)
accounts = get_row_data_by_id(table_data)
update_db_record(accounts)
