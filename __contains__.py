class A:
    def __init__(self, x):
        self.arr = list(range(x))

'''
Yes
No
'''

# __contains__メソッドがないとarr列も指定しなければならない！
a = A(10)
print(("No", "Yes")[3 in a.arr])
print(("No", "Yes")[23 in a.arr])

class A:

    def __init__(self, x):
        self.arr = list(range(x))

    def __contains__(self, item):
        return item in self.arr


'''
Yes
No
'''
a = A(10)

# __contains__メソッドがあるとクラス名のみでよい
print(("No", "Yes")[3 in a])
print(("No", "Yes")[23 in a])

