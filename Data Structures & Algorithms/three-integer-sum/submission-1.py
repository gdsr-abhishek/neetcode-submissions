class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        combo_set =set()
        length_num = len(nums)
        for i in range(length_num):
            left = i+1
            right = length_num - 1
            while left < right:
                if sorted_nums[i] + sorted_nums[left] + sorted_nums[right] == 0:
                    combo_set.add((sorted_nums[i] ,sorted_nums[left] ,sorted_nums[right]))
                    left +=1
                elif sorted_nums[i] + sorted_nums[left] + sorted_nums[right] > 0:
                    right -=1
                else:
                    left +=1
        return [list(i) for i in combo_set]

                    




        
        