from src.utils.helper import getConfig, clear, getLanguage, getAPIKeys
from src.classes import Color, Log
from src.classes.exchanges import MEXC

log = Log() # Log sınıfını nesne olarak tutar.
CONFIG = getConfig()
LANG = getLanguage(CONFIG["language"])

def main():
    """ Ana fonksiyondur. """
    try:
        apiKeys = getAPIKeys()
        accessKey = apiKeys["accessKey"]
        secretKey = apiKeys["secretKey"]

        exchange = MEXC(accessKey, secretKey)

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
            print("API anahtarları geçersiz.")
            log.warning("API Keys are invalid.")
    except Exception as e:
        log.error(f"Unexpected error in 'main' function:\n{e}")

if __name__ == "__main__":
    main()
    input(f"{Color.lblack}\n{LANG['enterToExit']}{Color.reset}")
