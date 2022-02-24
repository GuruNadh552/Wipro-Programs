a = ['a','e','i','o','u','A','E','I','O','U']
n = int(input())
m = input().split()
l = [i for i in m if i not in a]
print(len(l))
