# find the largest elemnt in arrat
nums=[5,3,8,44,3,99,5,-66667,6,22,4,6]
largest=nums[0]
n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])
    
print(largest)