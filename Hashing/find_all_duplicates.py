class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        myMap = {}
        for n in nums:
            myMap[n] = 1 + myMap.get(n, 0)
        result = []
        for n in myMap:
            if myMap[n] > 1:
                result.append(n)
        return result
