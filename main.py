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

def executeTransaction(transactionType):
    exchange.syncExchangeTime()
    if not exchange.checkKeys():
        return print(f"{Color.lred}{LANG['invalidApiKeys']}{Color.reset}")
    
    symbol = inputSymbol()
    amount = inputAmount()
    minimumPrice = exchange.getMinimumPrice(symbol)
    
    if amount < minimumPrice:
        print(f"{Color.lred}{LANG['invalidMinAmount'].format(value=f'{minimumPrice:.20f}')}{Color.reset}")
    else:
        exchange.syncExchangeTime()
        if transactionType == 'buy':
            exchange.buy(symbol, amount)
        elif transactionType == 'sell':
            exchange.sell(symbol, amount)

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
                executeTransaction('buy')
            elif inputValue == 2:
                executeTransaction('sell')
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
