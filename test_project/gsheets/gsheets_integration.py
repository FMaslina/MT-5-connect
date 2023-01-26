import pygsheets


def init(secret_path, sheet_name):      # Получение нужной таблицы
    gc = pygsheets.authorize(client_secret=secret_path)
    sh = gc.open(sheet_name)
    wks = sh.sheet1
    return wks


def get_all_table_data(wks, fild_start, fild_end):      # Получение всех данных с таблицы
    data_list = wks.get_values(fild_start, fild_end)
    #for row in data_list:
        #print(row)
    return data_list


#def get_rows_ids(data):     # Получение id всех записей
    #ids = []
    #for row in data:
        #ids.append(row[2])
    #return ids


def get_row_data_by_id(data, id):      # Получение нужной записи по id
    for row in data:
        if row[2] == str(id):
            return row
    return 'Запись не найдена'


def update_row_data_by_id(wks, id, value_update, field_start, field_end):   # Обновление нужной записи по id
    data = wks.get_values(field_start, field_end)
    for i in range(len(data)):
        print(data[i])
        if str(id) in data[i]:
            wks.update_value(f'J{i+1}', value_update)


wks = init('client_secret.json', 'Test')
table_data = get_all_table_data(wks, 'A1', 'K5')
print(get_row_data_by_id(table_data, 2028))
update_row_data_by_id(wks, 202, 'test', 'A1', 'K5')