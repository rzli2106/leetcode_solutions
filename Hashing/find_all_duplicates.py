class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Hashmaps
        myMap = {}
        result = []
        for n in nums:
            myMap[n] = 1 + myMap.get(n, 0)
            if myMap[n] == 2:
                result.append(n)
        return result"""
        """seen = set()
        result = []
        for n in nums:
            if n in seen:
                result.append(n)
            else:
                seen.add(n)
        return result"""

        result = []
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0:
                result.append(n)
            nums[n-1] *= -1
        return result

