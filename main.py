# p5
# import collections

# Card = collections.namedtuple("Card",["rank","suit"])

# class FrenchDeck:
#     ranks = [str(n) for n in range(2,11)] + list("JQKA")
#     # .split()で空欄ごとに分けて、リスト型にする
#     suits = "spades diamonds clubs hearts".split()

#     def __init__(self):
#         self._cards = [Card(rank,suit) for suit in self.suits
#                                       for rank in self.ranks]

#     def __len__(self):
#         return len(self._cards)
    
#     # __getitem__で場所の参照を行っている
#     def __getitem__(self,position):
#         return self._cards[position]

# deck = FrenchDeck()

# print(len(deck))
# print(deck[0])

# from random import choice
# print(choice(deck))

# print(deck[:3])
# print(deck[12:26:2])

# for card in deck:
#     print(card)

# 逆向きのreversed
# for card in reversed(deck):
#     print(card)

# suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# def spades_high(card):
#     # card.rankで数字を取り出している & .indexはリスト内での順番を表す(今回は２から始まる)
#     rank_value = FrenchDeck.ranks.index(card.rank) 
#     # suit_vlauesでマークに相当する数字を辞書型から取り出す & len(suit_vlaues)は4枚ずつの単位強さが周回することを表す
#     return rank_value * len(suit_values) + suit_values[card.suit] 

# print(deck.ranks)
# print(deck[31])
# print(FrenchDeck.ranks.index(deck[31].rank))

# for card in sorted(deck,key=spades_high):
#     print(card)

# print(deck[26])
# print(spades_high(deck[26]))

# from math import hypot

# class Vector:
    
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return 'Vector(%r, %r)' % (self.x, self.y)
    
#     def __abs__(self):
#         return hypot(self.x, self.y)
    
#     def __bool__(self):
#         return bool(abs(self))
    
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.x + other.y
#         return Vector(x,y)
    
#     def __mul__(self, scalar):
#         return Vector(self.x * scalar, self.y * scalar)
    
# print(Vector) # __repr__メソッドにより、オブジェクトの中身を調べることができる

# symbols = "$"
# beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols))) 
# print(beyond_ascii)
# filterは（引数１、引数２）の時に、引数１がTrueの場合にのみ、返り値を渡す
# map（引数１，引数２）で引数１で定義した関数を引数２に適応する

# symbols = "$#%$"
# print(tuple(ord(symbol) for symbol in symbols))


# import array
# print(array.array("I", (ord(symbol) for symbol in symbols)))

# colors = ["black", "white"]
# sizes = ["S", "M", "L"]
# for tshirt in ("%s %s" % (c, s) for c in colors for s in sizes):
#     print(tshirt)

# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ("Tokyo", 2003, 32.450, 0.66, 8014)
# traveler_ids = [("USA", "31195855"), ("BRA", "CE342567"),
#                 ("ESP", "XDA205856")]
# for passport in sorted(traveler_ids):
#     print("%s/%s" % passport)
#     # タプルのアンパック

# for country, _ in traveler_ids:
#     print(country)

# lax_coordinates = (33.945, -118.408056)
# latitude, longitude = lax_coordinates

# divmod(20, 8) #divmodは（商, 余り）をタプルで返す → 20/8 = 2 余り 4
# t = (20, 8)
# divmod(*t) #タプルのアンパック
# quotient, remainder = divmod(*t)
# print(quotient, remainder)

# import os
# _, filename = os.path.split("/home/luciano/.ssh/idrsa.pub")
# print(filename)

# a, b, *rest = range(5)
# s = a, b, *rest

# metro_areas = [
#     ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
#     ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
#     ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
#     ("New York-Newark", "US", 20.104, (40.808611, -74.0020386)),
#     ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833))
# ]

# print("{:15} | {:^9} | {:9}".format("", "lat.", "long."))
# fmt = "{:15} | {:9.4f} | {:9.4f}"
# for name, cc, pop, (latitude, longitude) in metro_areas:
#     if longitude <= 0:
#         print(fmt.format(name, latitude, longitude))

# from collections import namedtuple
# City = namedtuple("City", "name country population coordinates")
# tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
# print(tokyo.population)

# #クラス属性_fields
# print(City._fields)
# LatLong = namedtuple("LatLong", "lat long") #LatLongを使用した時、２つのインスタンスをlatとlongでおく
# delhi_data = ("Delhi NCR", "IN", 21.935, LatLong(28.613889, 77.208889))
# delhi = City._make(delhi_data)
# delhi._asdict()
# for key, value in delhi._asdict().items(): #named_tupleによって key:name, country,… | value:Delhi NCR, IN, …となった
#     print(key + ":", value)

# l = list(range(10))
# l[2:4] = [20, 30]
# print(l)