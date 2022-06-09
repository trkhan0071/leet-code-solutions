class Solution:
    def mySqrt(self, x: int) -> int:
        left=1
        right = x+1
        while left<right:
            mid = (left+right)//2
            if mid*mid==x:
                return mid
            elif x>mid*mid:
                left=mid+1
            else:
                right = mid
        return left-1
                
        
