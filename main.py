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
    symbol = ""
    while True:
        try:
            inputValue = str(input(f"\n{Color.yellow}> {LANG['pair']}: {Color.reset}"))
            if inputValue.upper() in symbolListUpper:
                symbol = inputValue.upper()
                break
            else:
                print(f"{Color.lred}{LANG['invalidPair']}{Color.reset}")
                getCloseMatches = difflib.get_close_matches(inputValue.upper(), symbolListUpper, n=6, cutoff=0.6)
                if getCloseMatches:
                    print(f"{Color.lcyan}{LANG['similarPairs']}: {', '.join(getCloseMatches)}{Color.reset}")
                else:
                    print(f"{Color.lred}{LANG['noSimilarPairs']}{Color.reset}")
        except:
            print(f"{Color.lred}{LANG['invalidPair']}{Color.reset}")
    return symbol

def inputAmount():
    amount = ""
    while True:
        try:
            inputValue = float(input(f"\n{Color.yellow}> {LANG['amount']}: {Color.reset}"))
            if inputValue < 0:
                print(f"{Color.lred}{LANG['cantLessZero']}{Color.reset}")
            else:
                amount = inputValue
                break 
        except:
            print(f"{Color.lred}{LANG['invalidAmount']}{Color.reset}")
    return amount

def buyCryptocurrency():
    exchange.syncExchangeTime()
    if exchange.checkKeys():
        symbol = inputSymbol()
        amount = inputAmount()
        minimumPrice = exchange.getMinimumPrice(symbol)
        if amount < minimumPrice:
            print(f"{Color.lred}{LANG['invalidMinAmount'].format(value=f'{minimumPrice:.20f}')}{Color.reset}")
        else:
            exchange.syncExchangeTime()
            exchange.buy(symbol, amount)
    else:
        print(f"{Color.lred}{LANG['invalidApiKeys']}{Color.reset}")

def sellCryptocurrency():
    exchange.syncExchangeTime()
    if exchange.checkKeys():
        symbol = inputSymbol()
        amount = inputAmount()
        minimumPrice = exchange.getMinimumPrice(symbol)
        if amount < minimumPrice:
            print(f"{Color.lred}{LANG['invalidMinAmount'].format(value=f'{minimumPrice:.20f}')}{Color.reset}")
        else:
            exchange.syncExchangeTime()
            exchange.sell(symbol, amount)
    else:
        print(f"{Color.lred}{LANG['invalidApiKeys']}{Color.reset}")

def menu():
    while True:
        try:
            print(f"{Color.yellow}--------------------------------------------------{Color.reset}")
            print(f"\n{Color.lblack}{LANG['enterTransactionNumber']}{Color.reset}")
            printOption(1, LANG['buyCryptocurrency'])
            printOption(2, LANG['sellCryptocurrency'])
            inputValue = int(input(f"\n{Color.yellow}> {LANG['transactionNumber']}: {Color.lyellow}"))
            print(Color.reset, end='\r')
            if inputValue == 1:
                buyCryptocurrency()
            elif inputValue == 2:
                sellCryptocurrency()
            else:
                print(f"{Color.lred}{LANG['invalidTransactionNumber']}{Color.reset}")
        except:
            print(f"{Color.lred}{LANG['invalidTransactionNumber']}{Color.reset}")

def main():
    """ Main function. """
    global exchange
    try:
        apiKeys = getAPIKeys()
        accessKey = apiKeys["accessKey"]
        secretKey = apiKeys["secretKey"]

        exchange = MEXC(accessKey, secretKey)

        menu()
    except Exception as e:
        log.error(f"Unexpected error in 'main' function:\n{e}")

if __name__ == "__main__":
    clear()
    main()
    input(f"{Color.lblack}\n{LANG['enterToExit']}{Color.reset}")
