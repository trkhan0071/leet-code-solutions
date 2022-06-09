class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        x,y,i=1,2,3 
        while(i<=n):
            steps = x+y
            x=y
            y=steps
            i+=1
        return steps
        
