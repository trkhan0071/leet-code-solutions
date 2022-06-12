class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        len_set_nums = len(set(nums))
        if len_set_nums == len_nums:
            return False
        else:
            return True
