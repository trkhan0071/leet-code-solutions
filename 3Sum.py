class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        len_nums = len(nums)
        i=0
        while(i<len_nums-2):
            j=i+1
            k=len_nums-1
            while(j<k):
                s= nums[i]+nums[j]+nums[k]
                if s==0:
                    result.append([nums[i], nums[j],nums[k]])
                    while(j+1<len_nums and nums[j]==nums[j+1]): j+=1
                    while(k-1>j and nums[k]==nums[k-1]):k-=1
                    j+=1
                    k-=1
                elif s<0:j+=1
                else: k-=1
            while(i+1<len_nums-2 and nums[i+1]==nums[i]):i+=1
            i+=1
        return result
        
