class Solution:
    def findMin(self, nums: List[int]) -> int:
        len_nums = len(nums)
        left= 0
        right = len_nums - 1
        result = nums[0]
        while (left<=right):
            if nums[left]<nums[right]:
                result = min(result, nums[left])
                break
            else:
                mid = (left+right)//2
                print(left, mid, right)
                result=min(result, nums[mid])
                if nums[mid]<nums[left]:
                    right = mid-1
                else: left=mid+1
        return result
        
