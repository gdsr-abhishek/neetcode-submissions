class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left  = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            height = min(heights[left] ,heights[right])
            breadth = right - left
            max_area = max( height * breadth ,max_area)
            if heights[left] >= heights[right]:
                right -=1
            else:
                left +=1
        return max_area
