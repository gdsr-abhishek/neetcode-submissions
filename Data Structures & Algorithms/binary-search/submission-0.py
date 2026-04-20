class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        num_length = len(nums)
        right = num_length - 1
        middle = right // 2
        while left <= right and right < num_length:
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
                middle = (right + left) //2
            else:
                right = middle - 1
                middle = (right + left)//2
        return -1
        