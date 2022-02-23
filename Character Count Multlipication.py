x = input()
y = int(input())
z = list(map(str,input().split()))
s = 0
for i in z:
    s+= x.count(i) * ord(i)
print(s)
