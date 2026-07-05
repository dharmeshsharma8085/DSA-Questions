class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        low = 0
        high = n-1
        l_b=n
        u_b=n
        while low <= high :
            mid = (low+high)//2
            if nums[mid]>=target:
                l_b=mid
                high= mid-1
            else:
                low= mid+1
        if l_b == n or nums[l_b] != target:
            return [-1,-1]
        low = 0
        high = n - 1
        while low <= high :
            mid = (low+high)//2
            if nums[mid]>target:
                u_b=mid
                high=mid-1
            else:
                low= mid+1
        return[l_b,u_b-1] 