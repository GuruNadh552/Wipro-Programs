n1 = int(input())
n2 = int(input())
m = list(map(int,input().split()))
l = [i//n2 for i in m]
print(sum(l))
