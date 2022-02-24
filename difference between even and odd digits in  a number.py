n = list(input())
l = [int(i) for i in n if(int(i)%2==0)]
m = [int(i) for i in n if(int(i)%2!=0)]
print(abs(sum(l)-sum(m)))
