class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = nums[0]
        last = nums[-1]
        distict = len(set(nums))
        k=0
        for i in range(first,last+1):
            if i in nums:
                nums[k]=i
                k+=1
        return k
