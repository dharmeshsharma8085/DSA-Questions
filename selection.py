num=[123,4,56,7,8,9]
def selection_sort(num):
    n=len(num)
    for i in range(0,n):
        mini=i
        for j in range(i+1,n):
            if num[j]<num[mini]:
                mini=j
        num[i],num[mini]=num[mini],num[i]
    return num
print(selection_sort(num))