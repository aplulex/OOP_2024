import random
row=int(input())
col=int(input())
num=int(input())
T=[(sorted(random.randint(1, 10) for i in range(row)))]
for p in range(col-1):
    T.insert(p+1 , list(sorted(random.randint(T[p][-1], 10) for i in range(row))))
cor=T[0][-1]
r=0
while num != cor:
    if r <= row*col:
        if num > cor:
            col-=1
            cor=T[-col+1][-1]
            r+=1
        else :
            row-=1
            cor=T[0][row-1]
            r+=1
    else:
        print("НЕТ")
        break
print(T)
print(r)