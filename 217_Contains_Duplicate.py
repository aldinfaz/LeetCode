class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set() #set and hashset are the same thing in python

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
