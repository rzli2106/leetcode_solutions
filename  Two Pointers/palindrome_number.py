class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """x = str(x)
        opposite = len(x)
        for i in range(len(x)):
            if x[i] != x[opposite-1]:
                return False
            opposite -= 1
        return True"""
        s = str(x)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        