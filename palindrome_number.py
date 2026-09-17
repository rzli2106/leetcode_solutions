class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        opposite = len(x)
        for i in range(len(x)):
            if x[i] != x[opposite-1]:
                return False
            opposite -= 1
        return True
        