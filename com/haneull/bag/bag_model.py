from dataclasses import dataclass

@dataclass
class BagModel:
    total : int
    it_w1 : int
    it_w2 : int
    it_w3 : int
    it_w4 : int
    it_p1 : int
    it_p2 : int
    it_p3 : int
    it_p4 : int
    # items: dict ??
    result : str

    @property
    def total(self) -> str: return self._total
    @total.setter
    def total(self,total): self._total = total
    @property
    def it_w1(self) -> int: return self._it_w1
    @it_w1.setter
    def it_w1(self,it_w1): self._it_w1 = it_w1
    @property
    def it_w2(self) -> int: return self._it_w2
    @it_w2.setter
    def it_w2(self,it_w2): self._it_w2 = it_w2
    @property
    def it_w3(self) -> int: return self._it_w3
    @it_w3.setter
    def it_w3(self,it_w3): self._it_w3 = it_w3
    @property
    def it_w4(self) -> int: return self._it_w4
    @it_w4.setter
    def it_w4(self,it_w4): self._it_w4 = it_w4
    @property
    def it_p1(self) -> int: return self._it_p1
    @it_p1.setter
    def it_p1(self,it_p1): self._it_p1 = it_p1
    @property
    def it_p2(self) -> int: return self._it_p2
    @it_p2.setter
    def it_p2(self,it_p2): self._it_p2 = it_p2
    @property
    def it_p3(self) -> int: return self._it_p3
    @it_p3.setter
    def it_p3(self,it_p3): self._it_p3 = it_p3
    @property
    def it_p4(self) -> int: return self._it_p4
    @it_p4.setter
    def it_p4(self,it_p4): self._it_p4 = it_p4
    @property
    def result(self) -> int: return self._result
    @result.setter
    def result(self,result): self._result = result