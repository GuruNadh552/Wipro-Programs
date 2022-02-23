n = int(input())
lis = list(map(int,input().split()))
m = -999
for i in range(n-1):
    if(s<(lis[i]+lis[i+1])):
        s = lis[i]+lis[i+1]
print(s)
