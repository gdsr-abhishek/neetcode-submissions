class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = 1
        num_of_zeroes = 0
        for i in nums:
            if i != 0:
                full_product *= i
            else:
                num_of_zeroes +=1
        response = []
        if num_of_zeroes > 1 :
            return [0 for i in range(len(nums))]
        else:
            for i in nums:
                if num_of_zeroes == 0:
                    response.append(full_product//i)
                else:
                    if i ==0:
                        response.append(full_product)
                    else:
                        response.append(0)
            return response
        