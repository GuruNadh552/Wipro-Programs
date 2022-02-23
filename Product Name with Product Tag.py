x = ['a','e','i','o','u']
y = ['A','E','I','O','U']
s = list(input())
for i in range(len(s)):
    if s[i] in x:
        s[i] = x[(x.index(s[i])+1)%5]
    if s[i] in y:
        s[i] = y[(y.index(s[i])+1)%5]
print(''.join(s))
