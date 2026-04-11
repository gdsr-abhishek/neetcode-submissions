class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_length =  len(s)
        left = 0
        unique_set = set()
        for right in range(char_length):
            while s[right] in unique_set:
                unique_set.remove(s[left])
                left +=1
            unique_set.add(s[right])
            max_length = max(max_length, right -left +1)

        return max_length

        