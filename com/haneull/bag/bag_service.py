from com.haneull.bag.bag_model import BagModel

class BagService:

    def __init__(self):
        pass

    def execute(self, bag: BagModel) -> BagModel:
        print("서비스 total: ", bag.total)
        print("서비스 it_w1: ", bag.it_w1)
        print("서비스 it_p1: ", bag.it_p1)
        print("가방 문제 풀기")

        item1 = {"weight": bag.it_w1, "profit": bag.it_p1}
        item2 = {"weight": bag.it_w2, "profit": bag.it_p2}
        item3 = {"weight": bag.it_w3, "profit": bag.it_p3}
        item4 = {"weight": bag.it_w4, "profit": bag.it_p4}
        items = [item1, item2, item3, item4]

         
        for i in range(4):
            items[i]["name"] = f"item{i+1}"
            items[i]["profit_per_weight"] = items[i]["profit"]/items[i]["weight"]

        for i in range(4):
            for j in range(i+1, 4):
                if items [i]["profit_per_weight"] < items[j]["profit_per_weight"]:
                    items[i], items[j] = items[j], items[i]

        for i in items:
            print("네임, 단위당 이익 추가: ", i)

        remain_weight = bag.total
        total_profit = 0

        for i in range(4):
            # 3, 4, 4, 3 -> 10. 7, 3, 0
            if items[i].get("weight") <= remain_weight: 
                remain_weight -= items[i].get("weight")
                total_profit += items[i].get("profit")
            else:
                total_profit = total_profit + remain_weight*items[i].get("profit_per_weight")
                break

        bag.total_profit = total_profit
        return bag


