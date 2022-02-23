n = input()
s = ''
for i in range(len(n)//2):
    s+=str(int(n[i])+int(n[len(n)-i-1]))
print(s)
