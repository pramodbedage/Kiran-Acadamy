
def isArraySpecial(nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(nums)
        
        # prefix[i] stores the count of bad adjacent pairs up to index i
        #The pair will go to  in quires[i] [j] index
        prefix = [0] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1]
            # Bad pair: two adjacent numbers have the same parity (both even or both odd)

            # if nums[i] % 2 == nums[i - 1] % 2: means two adjacent numbers have the same parity (both even or both odd)
            # prefix[i] += 1: means we add 1 to the prefix sum at index i
            
            if nums[i] % 2 == nums[i - 1] % 2:
                prefix[i] += 1
    
        ans = []
        for start, end in queries:

            # If count of bad pairs between start and end is 0, subarray is special
            # prefix[end] - prefix[start] == 0: means there are no bad pairs between start and end

            # prefix[end] - prefix[start] != 0: means there are bad pairs between start and end
            
            if prefix[end] - prefix[start] == 0:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans

print(isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]))           # Output: [False]
print(isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]))      # Output: [False, True]


