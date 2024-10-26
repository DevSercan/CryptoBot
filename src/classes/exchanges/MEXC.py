from src.interfaces import IExchange
from src.classes import Color, Log
import ccxt
from src.utils.helper import extractJsonFromText, getConfig, getLanguage
import json

log = Log()
CONFIG = getConfig()
LANG = getLanguage(CONFIG["language"])

class MEXC(IExchange):
    def __init__(self, accessKey, secretKey):
        try:
            log.debug("The '__init__' function of the 'MEXC' class has been executed.")
            self.mexc = ccxt.mexc({
                'apiKey': accessKey,
                'secret': secretKey,
                'enableRateLimit': True, # API istek sınırlarına uyulmasını sağlar
                'options': {
                    'recvWindow': 10000, # Sunucu ile istemci arasındaki farkın kaç milisaniyeye kadar tolere edileceğini belirler.
                },
            })
            self.errorMap = {
                400: LANG['amountCantLessZero'],
                10007: LANG['symbolNotSupportAPI'],
                30005: LANG['oversold'],
                30002: LANG['minTransactionVolumeBelowThreshold'],
                700006: LANG['ipNotInWhiteList'],
            }
        except Exception as e:
            log.error(f"Unexpected error in '__init__' function of the 'MEXC' class:\n{e}")
    
    def syncExchangeTime(self) -> bool:
        """ Sunucu ile istemci arasındaki zaman farkını yükler. Her 'recvWindow' zamanı aşıldığında bu fonksiyon kullanılmalıdır. """
        try:
            log.debug("The 'syncExchangeTime' function of the 'MEXC' class has been executed.")
            serverTime = self.mexc.fetch_time()
            self.mexc.nonce = lambda: serverTime
            self.mexc.load_time_difference()
            return True
        except Exception as e:
            if not self.handleError(e):
                log.error(f"Unexpected error in 'syncExchangeTime' function of the 'MEXC' class:\n{e}")
            return False

    def checkKeys(self) -> bool:
        """ API Anahtarlarının geçerliliğini kontrol eder. """
        try:
            log.debug("The 'checkKeys' function of the 'MEXC' class has been executed.")
            self.syncExchangeTime()
            self.mexc.fetch_balance()
            return True
        except Exception as e:
            if not self.handleError(e):
                log.error(f"Unexpected error in 'checkKeys' function of the 'MEXC' class:\n{e}")
            return False

    def getBalance(self) -> dict:
        """ Hesabın bakiye bilgisini döndürür. """
        try:
            log.debug("The 'getBalance' function of the 'MEXC' class has been executed.")
            self.syncExchangeTime()
            balance = self.mexc.fetch_balance()['total']
            return balance
        except Exception as e:
            if not self.handleError(e):
                log.error(f"Unexpected error in 'getBalance' function of the 'MEXC' class:\n{e}")
            return {}

    def getPrice(self, symbol:str) -> float:
        """ Belirli bir sembol için son fiyatı döndürür. """
        try:
            log.debug(f"[symbol={symbol}] The 'getPrice' function of the 'MEXC' class has been executed.")
            self.syncExchangeTime()
            ticker = self.mexc.fetch_ticker(symbol)
            price = ticker['last']
            return price
        except Exception as e:
            if not self.handleError(e):
                log.error(f"Unexpected error in 'getPrice' function of the 'MEXC' class:\n{e}")
            return None

    def buy(self, symbol:str, amount:float) -> dict:
        """ Kripto alım işlemi gerçekleştirir. """
        try:
            log.debug(f"[symbol={symbol}, amount={amount}] The 'buy' function of the 'MEXC' class has been executed.")
            self.syncExchangeTime()
            order = self.mexc.create_market_buy_order(symbol, amount)
            return order
        except Exception as e:
            if not self.handleError(e):
                log.error(f"Unexpected error in 'buy' function of the 'MEXC' class:\n{e}")
            return {}

    def sell(self, symbol:str, amount:float) -> dict:
        """ Kripto satış işlemi gerçekleştirir. """
        try:
            log.debug(f"[symbol={symbol}, amount={amount}] The 'sell' function of the 'MEXC' class has been executed.")
            self.syncExchangeTime()
            order = self.mexc.create_market_sell_order(symbol, amount)
            return order
        except Exception as e:
            if not self.handleError(e):
                log.error(f"Unexpected error in 'sell' function of the 'MEXC' class:\n{e}")
            return {}
    
    def getSymbolList(self) -> list:
        """ Borsada desteklenen sembolleri döndürür. """
        try:
            log.debug("The 'getSymbolList' function of the 'MEXC' class has been executed.")
            symbolList = self.mexc.symbols
            return symbolList
        except Exception as e:
            if not self.handleError(e):
                log.error(f"Unexpected error in 'getSymbolList' function of the 'MEXC' class:\n{e}")
            return []
    
    def getMinimumPrice(self, symbol:str) -> float:
        """ Minimum miktar bilgisini döndürür. """
        try:
            log.debug("The 'getMinimumPrice' function of the 'MEXC' class has been executed.")
            self.syncExchangeTime()
            return 1 / self.getPrice(symbol)
        except Exception as e:
            if not self.handleError(e):
                log.error(f"Unexpected error in 'getMinimumPrice' function of the 'MEXC' class:\n{e}")
            return None
    
    def getOrderStatus(self, order:dict) -> str:
        """ Al-Sat işleminin mevcut durumunu döndürür. """
        try:
            log.debug("The 'getOrderStatus' function of the 'MEXC' class has been executed.")
            self.syncExchangeTime()
            orderStatus = self.mexc.fetch_order(order.get('id'), order.get('symbol')).get('status')
            return orderStatus
        except Exception as e:
            if not self.handleError(e):
                log.error(f"Unexpected error in 'getOrderStatus' function of the 'MEXC' class:\n{e}")
            return None
    
    def handleError(self, error:Exception) -> str:
        try:
            try:
                errorData = json.loads(error.args[0])
            except json.decoder.JSONDecodeError:
                errorData = extractJsonFromText(error.args[0])
                errorData = json.loads(errorData) if errorData else None
            if errorData:
                errorMessage = self.errorMap.get(errorData.get("code"))
                print(f"{Color.lred}{errorMessage}{Color.reset}")
                return errorMessage
            return None
        except Exception as e:
            log.error(f"Unexpected error in 'handleError' function of the 'MEXC' class:\n{e}")
            return None