class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_lens = len(set(nums))
        return True if len(nums) - new_lens > 0 else False 