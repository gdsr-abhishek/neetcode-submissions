from collections import defaultdict
class Solution:
    def compareDicts(self,s:defaultdict,t:defaultdict):
        for i in t.keys():
            if s[i] < t[i]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:

        if t == s:
            return t
        elif len(t) == 1 and (t in s):
            return t
        else:
            tMap = defaultdict(int)
            min_substring = ""
            min_value = float('inf')
            for i in t:
                tMap[i] +=1
            range_s = len(s)
            for left in range(range_s):
                sMap=defaultdict(int)
                if tMap[s[left]]:
                    sMap[s[left]] +=1
                    right = left + 1
                    while right < range_s:
                        if tMap[s[right]]:
                            sMap[s[right]] +=1
                            print(sMap, left , right)
                            if self.compareDicts(sMap,tMap):
                                print(left,right)
                                if right - left + 1 < min_value:
                                    min_value  = right -left + 1
                                    min_substring = s[left:right+1]
                                    break
                        right +=1
                    
        return min_substring

        

        