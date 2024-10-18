from abc import ABC, abstractmethod

class IExchange(ABC):
    @abstractmethod
    def getBalance(self) -> dict:
        pass

    @abstractmethod
    def getPrice(self, symbol: str):
        pass

    @abstractmethod
    def buy(self, symbol: str, amount: float):
        pass

    @abstractmethod
    def sell(self, symbol: str, amount: float):
        pass