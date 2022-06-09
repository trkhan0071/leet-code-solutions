'''
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len_digits = len(digits)
        for i in range(len_digits-1, -1,-1):
            s = digits[i]+1
            if s>9:
                digits[i]=0
                if i==0:
                    digits[1:len_digits+1] = digits[:len_digits]
                    digits[0]=1
                    break
            else:
                digits[i]+=1
                break
        return digits
