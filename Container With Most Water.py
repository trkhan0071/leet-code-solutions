class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0 
        l=0
        r=n-1
        while(l<r):
            area= min(height[l], height[r])*(r-l)
            max_area = max(max_area, area)
            if height[l]>height[r]:r-=1
            else:l+=1
                
        return max_area
