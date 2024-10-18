from src.classes.IExchange import IExchange
from src.classes.Log import Log
import ccxt

log = Log()

class MEXC(IExchange):
    def __init__(self, accessKey, secretKey):
        try:
            log.debug("The '__init__' function of the 'MEXC' class has been executed.")
            self.mexc = ccxt.mexc({
                'apiKey': accessKey,
                'secret': secretKey,
                'enableRateLimit': True, # API istek sınırlarına uyulmasını sağlar
                'options': {
                    'recvWindow': 10000, # 10sn Sunucu zamanı ile sistem zamanı farkını ayarlama
                },
            })
            serverTime = self.mexc.fetch_time()
            self.mexc.nonce = lambda: serverTime # Zaman farkını eşitliyor
        except Exception as e:
            log.error(f"Unexpected error in '__init__' function of the 'MEXC' class:\n{e}")

    def getBalance(self):
        try:
            log.debug("The 'getBalance' function of the 'MEXC' class has been executed.")
            balance = self.mexc.fetch_balance() # Hesap bilgisini alır
            spotBalance = balance['total']
            nonZeroBalances = {currency: amount for currency, amount in spotBalance.items() if amount > 0} # Değeri 0 olmayan coinleri listeler
            return nonZeroBalances
        except Exception as e:
            log.error(f"Unexpected error in 'getBalance' function of the 'MEXC' class:\n{e}")
            return None

    def getPrice(self, symbol: str):
        """ Belirli bir sembol için son fiyatı döndürür. """
        try:
            log.debug("The 'getPrice' function of the 'MEXC' class has been executed.")
            ticker = self.mexc.fetch_ticker(symbol)
            price = ticker['last']
            return price
        except Exception as e:
            log.error(f"Unexpected error in 'getPrice' function of the 'MEXC' class:\n{e}")
            return None

    def buy(self, symbol: str, amount: float):
        """ Market alım işlemi gerçekleştirir. """
        try:
            log.debug("The 'buy' function of the 'MEXC' class has been executed.")
            order = self.mexc.create_market_buy_order(symbol, amount)
            return order
        except Exception as e:
            log.error(f"Unexpected error in 'buy' function of the 'MEXC' class:\n{e}")
            return None

    def sell(self, symbol: str, amount: float):
        """ Market satış işlemi gerçekleştirir. """
        try:
            log.debug("The 'sell' function of the 'MEXC' class has been executed.")
            order = self.mexc.create_market_sell_order(symbol, amount)
            return order
        except Exception as e:
            log.error(f"Unexpected error in 'sell' function of the 'MEXC' class:\n{e}")
            return None