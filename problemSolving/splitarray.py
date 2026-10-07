# You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:

# nums1.length == nums2.length == nums.length / 2.
# nums1 should contain distinct elements.
# nums2 should also contain distinct elements.
# Return true if it is possible to split the array, and false otherwise.
# xample 1:


class Solution(object):
    def isPossibleToSplit(self, nums):
       
        n = len(nums)
        
        # condition 1: Array must have even length
        # if array length is odd then return false

        if n % 2 != 0:
            return False
        
        # count occurrences of each number
        # if a element is present in array more than 2 times then return false
        # using dictionary
        y = {}
        for x in nums:
            y[x] = y.get(x, 0) + 1
        
        # condition 2: Each number must appear at most twice
        # if a element is present in array more than 2 times then return false
        
        for count in y.values():
            if count > 2:
                return False
        
        # if both conditions are met, it's always possible to split
        # return true
        return True

nums = [1,1,2,2,3,4]
sol = Solution()
print(sol.isPossibleToSplit(nums))
#output is True



# Thsi problem is an simple and it ths esay waay to solve the problem

#loop reduce the time complayciaty and increase the space complexity

#time complacity is an O(n)  and space complacity is an O(1)
