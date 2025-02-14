from com.haneull.bag.bag_model import BagModel
from com.haneull.bag.bag_service import BagService


class BagController:

    def __init__(self, **kwargs):
        self.total = kwargs.get('total')
        self.it_w1 = kwargs.get('it_w1')
        self.it_w2 = kwargs.get('it_w2')
        self.it_w3 = kwargs.get('it_w3')
        self.it_w4 = kwargs.get('it_w4')
        self.it_p1 = kwargs.get('it_p1')
        self.it_p2 = kwargs.get('it_p2')
        self.it_p3 = kwargs.get('it_p3')
        self.it_p4 = kwargs.get('it_p4')
        print("용량: ", self.total)
        print("아이템 무게: ", self.it_w1)
        print("아이템 이익: ", self.it_p1)

    def get_result(self) -> BagModel:
        bag = BagModel()
        service = BagService()
        bag.total = self.total
        bag.it_w1 = self.it_w1
        bag.it_w2 = self.it_w2
        bag.it_w3 = self.it_w3
        bag.it_w4 = self.it_w4
        bag.it_p1 = self.it_p1
        bag.it_p2 = self.it_p2
        bag.it_p3 = self.it_p3
        bag.it_p4 = self.it_p4
        return service.execute(bag)

