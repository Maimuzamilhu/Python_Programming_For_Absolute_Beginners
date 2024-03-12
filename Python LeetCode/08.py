"""
3 Sum Closest (LeetCode Problem 16)

Given an array `num` and a target value, find three integers in `num` such that their sum is closest to the target. Return the sum of these three integers.

Example:
Input: nums = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:
- 3 <= len(nums) <= 500
- -1000 <= nums[i] <= 1000
- -104 <= target <= 104
"""

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()  # Sort the input array in ascending order
        res = sum(nums[:3])  # Initialize the result with the sum of the first three elements

        for i in range(len(nums) - 2):
            s = i + 1  # Pointer for the second element (starting from the next index)
            e = len(nums) - 1  # Pointer for the third element (starting from the end)

            while s < e:
                sum_here = nums[i] + nums[s] + nums[e]  # Calculate the sum of the three elements
                if abs(sum_here - target) < abs(res - target):
                    res = sum_here  # Update the result if the current sum is closer to the target

                if sum_here < target:
                    s += 1  # Move the second pointer to the right
                else:
                    e -= 1  # Move the third pointer to the left

        return res

# Example usage
nums = [-1, 2, 1, -4]
target = 1
sol = Solution()
result = sol.threeSumClosest(nums, target)
print(f"The sum closest to the target is: {result}")
