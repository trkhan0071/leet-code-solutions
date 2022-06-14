class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=1
        r=1
        len_nums = len(nums)
        p1,p2,output=[1]*len_nums,[1]*len_nums,[1]*len_nums
        p1[0]=nums[0]
        for i in range(1,len_nums,1):
            p1[i]=p1[i-1]*nums[i]
        p2[-1]=nums[-1]
        for i in range(len_nums-2,-1,-1):
            p2[i]=p2[i+1]*nums[i]
        output[0]=p2[1]
        output[-1]=p1[-2]
        for i in range(1,len_nums-1,1):
            output[i]=p1[i-1]*p2[i+1]
        return output
                
        
