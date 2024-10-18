from src.utils.helper import getConfig, clear, getLanguage, getAPIKeys
from src.classes import Color, Log, TradingBot
from src.classes.exchanges import MEXC

log = Log() # Log sınıfını nesne olarak tutar.
CONFIG = getConfig()
LANG = getLanguage(CONFIG["language"])

def main():
    """ Ana fonksiyondur. """
    try:
        clear()
        apiKeys = getAPIKeys()
        accessKey = apiKeys["accessKey"]
        secretKey = apiKeys["secretKey"]

        exchange = MEXC(accessKey, secretKey)
        tradingBot = TradingBot(exchange)

        tradingBot.displayPrice('BTC/USDT')
        tradingBot.displayBalances()

        symbol = 'SHIB/USDT'
        amount = 100000
        tradingBot.executeSell(symbol, amount)
    except Exception as e:
        log.error(f"Unexpected error in 'main' function:\n{e}")

if __name__ == "__main__":
    main()
    input(f"{Color.lblack}\n{LANG['enterToExit']}{Color.reset}")
