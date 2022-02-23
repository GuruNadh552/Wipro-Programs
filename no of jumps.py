n1 = int(input())
n2 = int(input())
nof = int(input())
l = [n1]
for i in range(nof-1):
    l.append(l[-1]+n2)
print(*l)
