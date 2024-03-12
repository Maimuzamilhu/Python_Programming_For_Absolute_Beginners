"""Maximum Subarray leetcode 53"""

class solution:
    def maxSubArray(self , nums ):
        CurrentSum = max_sum = nums[0] 

        for i in nums[1:]:

            CurrentSum = max(i , CurrentSum+i)
            max_sum = max(max_sum, CurrentSum) #Mxsum will Trach max sum

        return max_sum
    
"""
Class Definition:
The code defines a Python class named solution.
This class contains a single method called maxSubArray.

Method Signature:
The maxSubArray method takes a single argument: a list of integers called nums.

Initialization:
Two variables are initialized:


CurrentSum: This variable keeps track of the current sum of the subarray being considered. It is initialized with the first element of nums.


max_sum: This variable keeps track of the maximum sum encountered so far. It is also initialized with the first element of nums.
Loop Iteration:
The method iterates over the elements of nums, starting from the second element (since the first element is already considered).
For each element i in nums (excluding the first element):

Update CurrentSum:
Calculate the maximum of i and the sum of CurrentSum and i.
This step effectively decides whether to start a new subarray at the current element i (if i is greater) or to continue the current subarray by adding i to CurrentSum.


Update max_sum:
Calculate the maximum of the current max_sum and the updated CurrentSum.
This step ensures that max_sum always holds the largest sum encountered so far.

Final Result:
After the loop, max_sum will contain the largest sum of any contiguous subarray within nums.
The method returns this value as the result

"""