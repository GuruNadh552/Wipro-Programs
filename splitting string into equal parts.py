import textwrap as t
n = input()
c = int(input())
s = (len(n)//c)*c
r = n[s:]
m = n[:s]
res = t.wrap(m, c)
res.append(r)
print(*res)
