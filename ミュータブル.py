s = []
# 参照を渡しているので同じ結果になる
t = s

for i in range(1,3):
    s.append(i)

print(s)
print(t)