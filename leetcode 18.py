# brute
# n=len(nums)
# if n<4:
#     return []
# my_set=set()
# for i in range(0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             for l in range(k+1,n):
#                 total=nums[i] + nums[j] + nums[k] + nums[l]
#                 if total==target:
#                     temp=[nums[i],nums[j],nums[k],nums[l]]
#                     temp.sort()
#                     my_set.add(tuple(temp))
                    
# result=[]
# for ans in my_set:
#     result.append(list(ans))    
# return result

# better

# n=len(nums)
# my_set=set()
# for i in range(0,n):
#     for j in range(i+1,n):
#         hash_set=set()
#         for k in range(j+1,n):
#             remain=target-nums[i]+nums[j]+nums[k]
#             if remain in hash_set:
#                   temp=[nums[i],nums[j],nums[k],nums[remian]]
#                   temp.sort()
#                   my_set.add(tuple(temp))
#             hash_set.add(nums[k])
                    
# result=[]
# for ans in my_set:
#     result.append(list(ans))    
# return result
           
#optimal

def foursum(self ,nums: List[int], target : int)-> List[list[int]]leetcode