from com.haneull.exchange.exchange_model import ExchangeModel
from com.haneull.exchange.exchange_service import ExchangeService


class ExchangeController:
    
    def __init__(self, **kwargs):
        self.total = kwargs.get('total')
        self.currency = kwargs.get('currency')
        print("총 금액:", self.total)
        print("화폐:", self.currency)

    def get_result(self) -> ExchangeModel:
        exchange = ExchangeModel()
        service = ExchangeService()
        exchange.total = self.total
        exchange.currency = self.currency
        
        return service.execute(exchange)
        

