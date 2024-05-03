""""
Brute force : runtime : 2080 ms; time complexity : O(n2)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
                

"""
using maps : runtime : 58 ms; time complexity : O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp not in comp_map:
                comp_map[n] = i
            else :
                return [i, comp_map[comp]]
            
# video ref : https://www.youtube.com/watch?v=MlgFhWvxuJk
            

