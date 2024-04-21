import random
K=random.randint(0,50)
N=int(input())
if N>50:
    N=49
i=sorted(random.sample(range(1,50),N))
def t(N,k):
    max=-1
    min=0
    m = []
    count=0
    while int(i[max])>int(i[min]):
        if int(i[max])+int(i[min])==k:
           m.append(i[min])
           m.append(i[max])
           print(m)
           m.clear()
           min+=1
           count+=1
        if int(i[max])+int(i[min])>k:
            max-=1
        if int(i[max])+int(i[min])<k:
            min+=1
    if count==0:
        print(-1)
print(K)
print(i)
t(N,K)