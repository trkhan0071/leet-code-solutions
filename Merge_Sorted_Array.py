class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=m+n
        for i in range(n):
            v = nums2[i]
            if v>=nums1[m-1]:
                nums1[m]=v
                m+=1
            else:
                for j in range(l):
                    if v<=nums1[j]:
                        nums1[j+1:m+1]=nums1[j:m]
                        nums1[j]=v
                        m+=1
                        break
            
                
