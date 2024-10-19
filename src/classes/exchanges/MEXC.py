from src.interfaces import IExchange
from src.classes import Log
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
    
    def checkKeys(self) -> bool:
        try:
            log.debug("The 'checkKeys' function of the 'MEXC' class has been executed.")
            self.mexc.fetch_balance()
            return True
        except Exception as e:
            log.error(f"Unexpected error in 'checkKeys' function of the 'MEXC' class:\n{e}")
            return False

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

    def getPrice(self, symbol:str):
        """ Belirli bir sembol için son fiyatı döndürür. """
        try:
            log.debug("The 'getPrice' function of the 'MEXC' class has been executed.")
            ticker = self.mexc.fetch_ticker(symbol)
            price = ticker['last']
            return price
        except Exception as e:
            log.error(f"Unexpected error in 'getPrice' function of the 'MEXC' class:\n{e}")
            return None

    def buy(self, symbol:str, amount:float):
        """ Market alım işlemi gerçekleştirir. """
        try:
            log.debug("The 'buy' function of the 'MEXC' class has been executed.")
            order = self.mexc.create_market_buy_order(symbol, amount)
            return order
        except Exception as e:
            log.error(f"Unexpected error in 'buy' function of the 'MEXC' class:\n{e}")
            return None

    def sell(self, symbol:str, amount:float):
        """ Market satış işlemi gerçekleştirir. """
        try:
            log.debug("The 'sell' function of the 'MEXC' class has been executed.")
            order = self.mexc.create_market_sell_order(symbol, amount)
            return order
        except ccxt.BaseError as e:
            errorMessage = e.args[0]
            if "code" in errorMessage and "symbol not support api" in errorMessage:
                log.error(f"The symbol '{symbol}' is not supported by MEXC API.")
            else:
                log.error(f"Unexpected error in 'sell' function of the 'MEXC' class:\n{e}")
            return None
        except Exception as e:
            log.error(f"Unexpected error in 'sell' function of the 'MEXC' class:\n{e}")
            return None
    
    def getSymbolList(self) -> list:
        """ Borsada desteklenen sembolleri liste olarak döndürür. """
        try:
            log.debug("The 'getSymbolList' function of the 'MEXC' class has been executed.")
            symbolList = self.mexc.symbols
            return symbolList
        except Exception as e:
            log.error(f"Unexpected error in 'getSymbolList' function of the 'MEXC' class:\n{e}")
            return None
    
    def getMinimumPrice(self, symbol:str) -> float:
        """ Minimum miktar bilgisini döndürür. """
        try:
            log.debug("The 'getMinimumPrice' function of the 'MEXC' class has been executed.")
            return 1 / self.getPrice(symbol)
        except Exception as e:
            log.error(f"Unexpected error in 'getMinimumPrice' function of the 'MEXC' class:\n{e}")
            return None