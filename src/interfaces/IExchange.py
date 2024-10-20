from abc import ABC, abstractmethod

class IExchange(ABC):
    @abstractmethod
    def checkKeys(self) -> bool:
        pass

    @abstractmethod
    def getBalance(self) -> dict:
        pass

    @abstractmethod
    def getPrice(self, symbol: str) -> float:
        pass

    @abstractmethod
    def buy(self, symbol: str, amount: float):
        pass

    @abstractmethod
    def sell(self, symbol: str, amount: float):
        pass

    @abstractmethod
    def getSymbolList(self) -> list:
        pass

    @abstractmethod
    def getMinimumPrice(self) -> float:
        pass