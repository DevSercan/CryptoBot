from src.utils.helper import getConfig, clear, getLanguage, getAPIKeys
from src.classes import Color, Log
from src.classes.exchanges import MEXC

log = Log()
CONFIG = getConfig()
LANG = getLanguage(CONFIG["language"])

def printOption(number, text):
    print(f"{Color.yellow}[{Color.lyellow}{number}{Color.yellow}]{Color.reset} {text}")

def menu():
    while True:
        try:
            print(f"{Color.yellow}--------------------------------------------------{Color.reset}")
            print(f"\n{Color.lblack}{LANG['enterTransactionNumber']}{Color.reset}")
            printOption(1, LANG['buyCryptocurrency'])
            printOption(2, LANG['sellCryptocurrency'])
            inputValue = int(input(f"{Color.yellow}> {LANG['transactionNumber']}: {Color.lyellow}"))
            print(Color.reset)
            if inputValue == 1:
                pass
            elif inputValue == 2:
                pass
            else:
                print(f"{Color.lred}{LANG['invalidTransactionNumber']}{Color.reset}")
        except:
            print(f"{Color.lred}{LANG['invalidTransactionNumber']}{Color.reset}")

def main():
    """ Main function. """
    try:
        apiKeys = getAPIKeys()
        accessKey = apiKeys["accessKey"]
        secretKey = apiKeys["secretKey"]

        exchange = MEXC(accessKey, secretKey)

        menu()

        if exchange.checkKeys():
            symbol = "BTC/USDC"
            symbolList = exchange.getSymbolList()

            if symbol in symbolList:
                amount = 1
                minimumPrice = exchange.getMinimumPrice(symbol)
                if amount < minimumPrice:
                    print(f"Minimum miktar '{minimumPrice:.20f}' değerinden büyük olmalı.")
                else:
                    exchange.sell(symbol, amount)
            else:
                print("Sembol geçersiz.")
        else:
            print(f"{Color.lred}{LANG['invalidApiKeys']}{Color.reset}")
    except Exception as e:
        log.error(f"Unexpected error in 'main' function:\n{e}")

if __name__ == "__main__":
    clear()
    main()
    input(f"{Color.lblack}\n{LANG['enterToExit']}{Color.reset}")
