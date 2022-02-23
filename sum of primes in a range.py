def prime(n):
    c = 0
    for i in range(1,n):
        if(n%i==0):
            c+=1
    if(c==1):
        return True
    return False
low = int(input())
high = int(input())
s = 0
for i in range(low,high):
    if(prime(abs(i))):
       s+=i
print(s)
