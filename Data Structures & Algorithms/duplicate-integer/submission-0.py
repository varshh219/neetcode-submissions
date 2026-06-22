class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for num in nums:
            if num not in d:
                d.add(num)
            else:
                return True
        return False