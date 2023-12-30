class Sample:
    def __init__(self, val):
        self.val = val
        print(self.val)

    def __add__(self, other):
        return self.val + other.val
    # def __add__は自作クラスで"+"が定義されたときの挙動を定義する　→　これがないとクラス同士の足し算ができない

o1 = Sample(1)
o2 = Sample(3)
print(o1 + o2)


class Mamo:
    def __init__(self,value):
        self.value = value
    # 足し算が行われた時の挙動を定義
    def __add__(self,other):
        if isinstance(other,Mamo):
            return f"({self.value}{other.value})"
        else:
            return NotImplemented

class Mamo2:
    def __init__(self,value):
        self.value = value
    # __radd__で右側の要素を指定(l_otherで左側の要素を足す実行の定義)
    def __radd__(self,l_other):
        if isinstance(l_other,Mamo):
            return f"2:{l_other.value}{self.value}"
        else:
            return NotImplemented
        
a = Mamo(12)
b = Mamo2(14)

# a : self.vlaue, b: other.value
result = a + b
print(result)





