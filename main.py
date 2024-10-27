from src.utils.helper import getConfig, clear, getLanguage, getAPIKeys
from src.classes import Color, Log
from src.classes.exchanges import MEXC
import difflib

log = Log()
CONFIG = getConfig()
LANG = getLanguage(CONFIG["language"])

def printOption(number, text):
    print(f"{Color.yellow}[{Color.lyellow}{number}{Color.yellow}]{Color.reset} {text}")

def inputSymbol():
    symbolList = exchange.getSymbolList()
    symbolListUpper = list(map(str.upper, symbolList))
    while True:
        try:
            inputValue = str(input(f"\n{Color.yellow}> {LANG['pair']}: {Color.reset}")).upper()
            if inputValue in symbolListUpper:
                return inputValue
            else:
                print(f"{Color.lred}{LANG['invalidPair']}{Color.reset}")
                getCloseMatches = difflib.get_close_matches(inputValue, symbolListUpper, n=6, cutoff=0.6)
                if getCloseMatches:
                    print(f"{Color.lcyan}{LANG['similarPairs']}: {', '.join(getCloseMatches)}{Color.reset}")
                else:
                    print(f"{Color.lred}{LANG['noSimilarPairs']}{Color.reset}")
        except:
            print(f"{Color.lred}{LANG['invalidPair']}{Color.reset}")

def inputAmount():
    while True:
        try:
            inputValue = float(input(f"\n{Color.yellow}> {LANG['amount']}: {Color.reset}"))
            if inputValue < 0:
                print(f"{Color.lred}{LANG['cantLessZero']}{Color.reset}")
            else:
                return inputValue
        except:
            print(f"{Color.lred}{LANG['invalidAmount']}{Color.reset}")

def transactCryptocurrency(transactType):
    if not exchange.checkKeys():
        return print(f"{Color.lred}{LANG['invalidApiKeys']}{Color.reset}")
    
    symbol = inputSymbol()
    amount = inputAmount()
    minimumPrice = exchange.getMinimumPrice(symbol)
    
    if amount < minimumPrice:
        print(f"{Color.lred}{LANG['invalidMinAmount'].format(value=f'{minimumPrice:.20f}')}{Color.reset}")
    else:
        if transactType == 'buy':
            order = exchange.buy(symbol, amount)
        elif transactType == 'sell':
            order = exchange.sell(symbol, amount)
        if order:
            orderStatus = exchange.getOrderStatus(order)
            if orderStatus == 'closed':
                print(f"{Color.lgreen}{LANG['transactionOrderSuccess']}{Color.reset}")
            elif orderStatus == 'open':
                print(f"{Color.lyellow}{LANG['transactionOrderInProgress']}{Color.reset}")
            else:
                print(f"{Color.lred}{LANG['transactionOrderFailed']} (orderStatus: {orderStatus}){Color.reset}")
        else:
            print(f"{Color.lred}{LANG['transactionOrderFailed']}{Color.reset}")

def fetchWalletInfo():
    balance = exchange.getBalance()
    if balance:
        print(f"{Color.lyellow}----- {LANG['walletInformation']} -----{Color.reset}")
        for symbol, amount in balance.items():
            print(f"{Color.lyellow}{LANG['cryptocurrency']}{Color.reset}: {symbol} {Color.lblack}|{Color.lyellow} {LANG['amount']}{Color.reset}: {amount}")
    else:
        print(f"{Color.lred}{LANG['fetchWalletInfoFailed']}{Color.reset}")

def menu():
    while True:
        try:
            print(f"{Color.yellow}--------------------------------------------------{Color.reset}")
            print(f"\n{Color.lblack}{LANG['enterTransactionNumber']}{Color.reset}")
            printOption(0, LANG['clearConsole'])
            printOption(1, LANG['buyCryptocurrency'])
            printOption(2, LANG['sellCryptocurrency'])
            printOption(3, LANG['fetchWalletInfo'])
            inputValue = int(input(f"\n{Color.yellow}> {LANG['transactionNumber']}: {Color.lyellow}"))
            print(Color.reset, end='\r')
            if inputValue == 0:
                clear()
            elif inputValue == 1:
                transactCryptocurrency('buy')
            elif inputValue == 2:
                transactCryptocurrency('sell')
            elif inputValue == 3:
                fetchWalletInfo()
            else:
                print(f"{Color.lred}{LANG['invalidTransactionNumber']}{Color.reset}")
        except:
            print(f"{Color.lred}{LANG['invalidTransactionNumber']}{Color.reset}")

def main():
    """ Main function. """
    global exchange
    try:
        apiKeys = getAPIKeys()
        exchange = MEXC(apiKeys["accessKey"], apiKeys["secretKey"])
        menu()
    except Exception as e:
        log.error(f"Unexpected error in 'main' function:\n{e}")

if __name__ == "__main__":
    clear()
    main()
    input(f"{Color.lblack}\n{LANG['enterToExit']}{Color.reset}")
