from com.haneull.bag.bag_model import BagModel

class BagService:

    def __init__(self):
        pass

    def execute(self, bag: BagModel) -> BagModel:
        print("서비스 total: ", bag.total)
        print("서비스 it_w1:", bag.it_w1)
        print("서비스 it_p1:", bag.it_p1)
        print("가방 문제 풀기")

        w_list = [bag.it_w1, bag.it_w2, bag.it_w3, bag.it_w4] # 쌤은 없애심 ?!
        p_list = [bag.it_p1, bag.it_p2, bag.it_p3, bag.it_p4]

        item1 = {"weight": bag.it_w1, "profit": bag.it_p1}
        item2 = {"weight": bag.it_w2, "profit": bag.it_p2}
        item3 = {"weight": bag.it_w3, "profit": bag.it_p3}
        item4 = {"weight": bag.it_w4, "profit": bag.it_p4}
        items = [item1, item2, item3, item4]







        # temp = []
        # for i in range(4):
        #     temp.append("profit"[i] / "weight"[i])


        temp = [4, 3, 2, 5]
        item_p_per_w = [temp[0], temp[1], temp[2], temp[3]]
        item1 = {"name": "item1", "weight": bag.it_w1, "profit": bag.it_p1, "p_per_w": item_p_per_w[0]}
        item2 = {"name": "item2", "weight": bag.it_w2, "profit": bag.it_p2, "p_per_w": item_p_per_w[1]}
        item3 = {"name": "item3", "weight": bag.it_w3, "profit": bag.it_p3, "p_per_w": item_p_per_w[2]}
        item4 = {"name": "item4", "weight": bag.it_w4, "profit": bag.it_p4, "p_per_w": item_p_per_w[3]}
        
        items = [item1, item2, item3, item4]

        for i in range(4):
            for j in range(i+1, 4):
                if items[i].get("p_per_w") < items[j].get("p_per_w"):
                    items[i], items[j] = items[j], items[i]

        for i in items:
            print("중간 점검", i.get("name"))


             
     
        



