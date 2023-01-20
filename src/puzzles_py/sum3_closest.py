import sys


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        diff = sys.maxsize
        solution = 0
        nums = sorted(nums)
        size = len(nums)
        for i in range(size):
            left = i + 1
            right = size - 1
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                if result == target:
                    # found the solution
                    return result
                if result < target:
                    left += 1
                else:
                    right -= 1
                if abs(result - target) < diff:
                    solution = result
                    diff = abs(result - target)
        return solution
