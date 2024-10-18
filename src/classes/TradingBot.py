from src.classes.IExchange import IExchange

class TradingBot:
    def __init__(self, exchange: IExchange):
        self.exchange = exchange

    def displayBalances(self):
        """ Hesap bakiyelerini ekrana yazdırır. """
        balances = self.exchange.getBalance()
        print("Mevcut Bakiyeler:")
        for currency, amount in balances.items():
            print(f"{currency}: {amount}")

    def displayPrice(self, symbol: str):
        """ Belirtilen sembolün fiyatını ekrana yazdırır. """
        price = self.exchange.getPrice(symbol)
        print(f"{symbol} Last Value: {price} USDT")

    def executeBuy(self, symbol: str, amount: float):
        """ Alım işlemini gerçekleştirir. """
        order = self.exchange.buy(symbol, amount)
        if order:
            print(f"Alım işlemi başarılı: {order}")
        else:
            print("Alım işlemi başarısız.")

    def executeSell(self, symbol: str, amount: float):
        """ Satım işlemini gerçekleştirir. """
        order = self.exchange.sell(symbol, amount)
        if order:
            print(f"Satım işlemi başarılı: {order}")
        else:
            print("Satım işlemi başarısız.")