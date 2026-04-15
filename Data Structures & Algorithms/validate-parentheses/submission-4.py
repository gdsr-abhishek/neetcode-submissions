class Solution:
    def isValid(self, s: str) -> bool:
        hMap= {"(":")","{":"}","[":"]"}
        if len(s) % 2 ==1:
            return False
        stack = list()
        for i in range(len(s)):
            if i!=0 and stack :
                if  stack[-1] in hMap and hMap[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return len(stack) == 0

        