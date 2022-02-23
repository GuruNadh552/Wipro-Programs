x = input()
l = [i for i in x if int(i)%2==0]
print("NA" if len(l)==0 else ''.join(l))
