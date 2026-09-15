class Solution:
    def twoSum(self, nums, target):
        #brute force
        '''for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]'''

        #utilizing hashmaps
        myMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in myMap:
                return(myMap[diff], i)
            myMap[n] = i
            