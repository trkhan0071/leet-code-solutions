'''
Input: strs = ["flower","flow","flight"]
Output: "fl"
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len_strs = len(strs)
        min_len = 201
        for i in range(len_strs):
            len_str = len(strs[i])
            if len_str<=min_len:
                min_str = strs[i]
        len_min_str = len(min_str)
        common_prefix=""
        ch=''
        for i in range(len_min_str):
            ch += min_str[i]
            found = 1
            for j in range(len_strs):
                if ch not in strs[j][:i+1]:
                    found = 0
                    break
            if found ==1:
                common_prefix=ch
            else:
                break
        return common_prefix
