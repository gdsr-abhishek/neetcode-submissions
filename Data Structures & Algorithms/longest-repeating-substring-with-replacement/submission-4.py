from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 1
        hashMap = defaultdict(int)
        hashMap[s[left]] = 1
        max_chars = 0
        count = 1
        while right < len(s) and left < right:
            hashMap[s[right]]+=1
            if (right - left + 1) - max(hashMap.values()) > k:
                max_chars = max(max_chars,right - left)
                hashMap[s[left]] -=1
                left +=1
            else:
                max_chars = max(max_chars, right - left + 1)
            right +=1
        return max_chars






