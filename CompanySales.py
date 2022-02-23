n = int(input())
li = list(map(int,input().split()))
m = int(input())
c = 0
for i in li:
    if(i%m==0 or m%i==0):
        c+=1
print(c)

        
