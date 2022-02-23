n = int(input())
lis = list(map(int,input().split()))
m = int(input())
c = 0
for i in lis:
    if(m%i==0 or i%m==0):
        c+=1
print(c)
