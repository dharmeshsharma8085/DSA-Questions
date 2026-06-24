num=[5,8,1,9,4,2,1,8,6]
n=len(num)
for i in range(n-1,-1,-10):
    for j in range(0,i):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
            