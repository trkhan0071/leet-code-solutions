class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b!=0:
            tmp = (a&b)<<1
            a = (a^b) & mask
            b = tmp & mask
        if a > mask//2: # if a is negtive
            return ~(a ^ mask)
        else:
            return a
