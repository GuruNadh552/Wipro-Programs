x = int(input())
y = list(map(int,input().spilt()))
z = [i for i in y if i<0]
print(len(z))
