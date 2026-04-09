class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_string = ''
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    check_string += i.lower()
                else:
                    check_string +=i
        left = 0
        right  = len(check_string) - 1
        while left < right:
            if check_string[left] != check_string[right]:
                return False
            left +=1
            right -=1
        return True

        