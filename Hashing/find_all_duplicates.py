class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        myMap = {}
        result = []
        for n in nums:
            myMap[n] = 1 + myMap.get(n, 0)
            if myMap[n] == 2:
                result.append(n)
        return result
