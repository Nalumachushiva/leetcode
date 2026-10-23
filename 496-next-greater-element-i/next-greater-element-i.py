class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in nums1:
            ind=nums2.index(i)
            ng=-1
            for j in range(ind+1,len(nums2)):
                if nums2[j]>i:
                    ng=nums2[j]
                    break
            stack.append(ng)
        return stack