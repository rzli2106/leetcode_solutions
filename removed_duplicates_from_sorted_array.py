class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        insert = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[insert] = nums[i]
                insert += 1
        return insert

        