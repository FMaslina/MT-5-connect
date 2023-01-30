import tinkoff_acquiring_api

init_data = {   # Словарь данных для инициализации
    "TerminalKey": "TinkoffBankTest",
    "Amount": 2000,
    "OrderId": "21080",
    "Description": "Подарочная карта на 1400.00 рублей",
    "DATA": {
        'Phone': "+79537650285",
        "Email": "FMaslina@yandex.ru"
    },
    "Receipt": {
        "Email": "FMaslina@yandex.ru",
        "Phone": "+79031234567",
        "EmailCompany": "b@test.ru",
        "Taxation": "osn",
        "Items": [{
            "Name": "Test",
            "Quantity": 1.00,
            "Amount": 1000,
            "Price": 1000,
            "Tax": "none"
        },
            {
                "Name": "test2",
                "Quantity": 1.00,
                "Amount": 1000,
                "Price": 1000,
                "Tax": "none"
            }]
    }
}

Acquiring = tinkoff_acquiring_api.TinkoffAcquiring(terminal="TinkoffBankTest",
                                                   secret_key="TinkoffBankTest")    # Создание объекта для подключения
init = Acquiring.init(payload=init_data)    # Инициализация, создание платежа
id = init['PaymentId']

authorize_data = {      # Данные для авторизации
    "PaymentId": id,
    "CardData": "PAN=4300000000000777;ExpDate=0519;CardHolder=IVAN PETROV;CVV=111",
    "TerminalKey": "TinkoffBankTest",
    "Token": "f5a3be479324a6d3a4d9efa0d02880b77d04a91758deddcbd9e752a6df97cab5"
}

print(init)
# authorize = Acquiring._call(method="FinishAuthorize",
# payload=authorize_data)     # Подтверждение платежа передачей реквизитов и списанием/блокировкой средств
# print(authorize)
token = Acquiring._get_token(request=init_data)     # Получение подписи запроса
print(token)
confirm_data = {    # Данные для подтверждения платежа
    "TerminalKey": "TinkoffBankTest",
    "PaymentId": id,
    "Token": token
}
# confirm = Acquiring._call(method="Confirm",
# payload=confirm_data)     # Подтверждение платежа и списывание ранее заблокированных средств
# print(confirm)

# cancel = Acquiring._call(method="Cancel", payload=confirm_data)   # Отмена платежа
# print(cancel)

# get_state = Acquiring._call(method="GetState", payload=confirm_data)      # Получение текущего статуса платежа
# print(get_state)

resend_data = {
    "TerminalKey": "TinkoffBankTest",
    "Token": token
}
# resend = Acquiring._call(method="Resend", payload=resend_data)    # Отправление неотправленных нотификаций
# print(resend)

co_data = {
    "TerminalKey": "TinkoffBankTest",
    "OrderId": 21080,
    "Token": token
}
check_order = Acquiring._call(method="CheckOrder", payload=co_data)     # Получение статуса заказа
print(check_order)
