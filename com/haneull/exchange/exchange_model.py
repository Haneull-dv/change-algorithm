from dataclasses import dataclass

@dataclass
class ExchangeModel:
    total: int
    currency: str
    result: str


    @property
    def total(self) -> int: return self._total
    @total.setter
    def total(self,total): self._total = total
    @property
    def currency(self) -> str: return self._currency
    @currency.setter
    def currency(self,currency): self._currency = currency
    @property
    def result(self) -> str: return self._result
    @result.setter
    def result(self,result): self._result = result
