from com.haneull.exchange.exchange_model import ExchangeModel


class ExchangeService:

    def __init__(self):
        pass

    def execute(self, exchange: ExchangeModel) -> ExchangeModel:
        currency_list = []
        currency_unit = ''
        if exchange.currency == 'USD':
            currency_list = self.get_dollar_list()
            currency_unit = '달러'
            print("달러 전달 완료")
        elif exchange.currency == 'WON':
            currency_list = self.get_won_list()
            currency_unit = '원'
            print("원화 전달 완료")
        else:
            print("잘못된 화폐단위입니다.")

        currency_dict = self.get_currency_dict(exchange.total, currency_list)
        self.print_currency_dict(currency_dict, exchange.currency)
        exchange.result = self.format_currency_counts(currency_dict, currency_unit)
        return exchange

    def get_currency_dict(self, total, currency_list) -> dict:
        money = total
        currency_dict = {}
        for currency in currency_list:
            currency_dict[currency] = money // currency
            money %= currency
        return currency_dict

    def get_dollar_list(self):
        DOLLAR_100 = 100
        DOLLAR_50 = 50
        DOLLAR_20 = 20
        DOLLAR_10 = 10
        DOLLAR_5 = 5
        DOLLAR_2 = 2
        DOLLAR_1 = 1

        dollar_list = [DOLLAR_100, DOLLAR_50, DOLLAR_20, DOLLAR_10, DOLLAR_5, DOLLAR_2, DOLLAR_1]
        return dollar_list
    
    def get_won_list(self):
        WON_50000 = 50000
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10

        won_list = [WON_50000, WON_10000, WON_5000,
                        WON_1000, WON_500, WON_100, WON_50, WON_10]
        return won_list
    

    def format_currency_counts(self, currency_dict, currency_unit):
        temp = ''
        for currency, count in currency_dict.items():
            temp += f"{currency}{currency_unit}: {count}개<br/>"
        return temp

    def print_currency_dict(self, currency_dict, exchange):
        print("-------💰거스름돈💰-------") 
        if exchange == 'USD': 
            for currency, count in currency_dict.items():
                print(f"{currency}달러: {count}개")

        elif exchange == 'WON': 
            for currency, count in currency_dict.items():
                print(f"{currency}원: {count}개")
        else:
            print("잘못된 화폐단위입니다.")
        print("-------끝-------")
                            