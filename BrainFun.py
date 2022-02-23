n = int(input())
m = int(input())
li = list(map(int,input().split()))
s = 0
for i in li:
    s+=(i//m)
print(s)
