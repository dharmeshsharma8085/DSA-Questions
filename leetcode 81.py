class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # nums = set()
        # n  = len(set)
        # low = 0
        # high = n-1
        # while low <= high:
        #     mid = ( low + high)//2
        #     if set[mid]==target:
        #         return True
        #     elif set[mid] <= set[high]:
        #         if set[mid]<=target<=set[high]:
        #             low = mid +1
        #         else:
        #             high = mid -1
        #     else:
        #         if set[low]<= target<= set[mid]:
        #             high = mid -1
        #         else:
        #             low = mid +1

        # return False


        n = len(nums)
        low= 0
        high = n-1
        while low<=high:
            mid  = ( low + high)//2
            if nums[mid]== target:
                return True
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            if nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid -1
            else:
                if nums[low]<=target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
                    
        return False
            
            
                