import MetaTrader5 as mt


def start_mt5(username, password, server, path):

    if not mt.initialize(login=username, password=password, server=server, path=path):
        print("initialize() failed, error code =", mt.last_error())
        quit()
    if mt.login(login=username, password=password, server=server):
        data = [mt.terminal_info(), mt.account_info(), mt.symbols_total(), mt.symbol_info(1),
                mt.orders_total(),
                mt.positions_total()]
        return data
    else:
        return "Login Failed"


print(start_mt5(username=805061, password="weax5szp", server="OpenInvestments-Demo",
                path="C:/Program Files/MetaTrader 5/terminal64.exe"))
print(start_mt5(username=805060, password="bsccvba1", server="OpenInvestments-Demo",
                path="C:/Program Files/MetaTrader 5 2/terminal64.exe"))

