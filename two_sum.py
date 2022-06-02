class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l= len(nums)
        index=[]
        for i in range(l):
            num_2=target - nums[i]
            if num_2 in nums[i+1:]:
                index.append(i)
                index.append(nums.index(num_2,i+1,l))
                break
        return index
