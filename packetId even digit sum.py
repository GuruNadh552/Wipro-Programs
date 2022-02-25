n = int(input())
m = list(map(str,input().split()))
o = []
for i in m:
    s = [int(j) for j in i if int(j)%2==0]
    o.append(sum(s))
print(*o)
