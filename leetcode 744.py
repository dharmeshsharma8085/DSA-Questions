class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        low = 0
        high = n-1
        u_b = n
        while low<=high:
            mid = (low+high)//2
            if letters[mid]>target:
                u_b = mid
                high = mid-1
            else:
                low = mid+1
        if u_b == n:
            return letters[0]
        return letters[u_b]

        