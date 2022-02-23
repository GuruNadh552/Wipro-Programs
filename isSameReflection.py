def isSameReflection(x,y):
    if(x[len(x)//2:]+x[:len(x)//2]==y):
        return 1
    return 0
x = input()
y = input()
print(isSameReflection(x,y))
