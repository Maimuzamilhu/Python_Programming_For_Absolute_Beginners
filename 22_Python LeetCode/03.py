"""subarray sum equals k 
    Input : nums = [1,1,1] , k =2
    output = 2
"""
class solution:
    def SubarraySum(self , nums , k):
        sumdict = {0:1}
        n = len(nums)
        count = 0
        s = 0  #comulative sum

        for num in nums:
            s+=num

            if s-k in sumdict:
                count+=sumdict[s-k]
            
            if s in sumdict:
                sumdict[s]+1
            
            else:
                sumdict[s] = 1
            
        return count
