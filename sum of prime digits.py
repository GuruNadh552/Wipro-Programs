def prime(n):
    c = 0
    for i in range(1,n):
        if(n%i==0):
            c+=1
    if(c==1):
        return True
    return False
s = input()
m = 0
for i in s:
    if(prime(int(i))):
        m+=int(i)
print(m)
