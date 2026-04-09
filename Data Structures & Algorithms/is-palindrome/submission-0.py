class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_string = ''
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    check_string += i.lower()
                else:
                    check_string +=i
        return check_string == check_string[::-1]

        