class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {'I':1, 'V':5,'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        len_s = len(s)
        ans = 0
        i=0
        while(i<len_s):
            v=dict_roman[s[i]]
            if i<len_s-1:
                if v>=dict_roman[s[i+1]]:
                    ans+=v
                else:
                    ans+=dict_roman[s[i+1]]-v
                    i+=1
            else:
                ans+=v
            i+=1
        return ans
