from bisect import bisect_left
from itertools import accumulate

def solve(nums):
    # Length of the input list
    n = len(nums)
    
    # Calculate the prefix sum of the input list
    prefix_sum = list(accumulate(nums, initial=0))
    
    # Initialize arrays to store maximum length, and index information
    max_length_array = [0] * (n + 1)
    prev_index_array = [0] * (n + 2)
    
    # Replace the subarray sum problem with the prefix sum
    for i in range(1, n + 1):
        prev_index_array[i] = max(prev_index_array[i], prev_index_array[i - 1])
        max_length_array[i] = max_length_array[prev_index_array[i]] + 1
        
        # Use binary search to find the index for the current element
        j = bisect_left(prefix_sum, prefix_sum[i] * 2 - prefix_sum[prev_index_array[i]])
        prev_index_array[j] = i
    
    # Return the maximum length
    return max_length_array[n]

# Input: Length of the list
n = int(input())
# Input: List of integers
nums = list(map(int, input().strip().split()))

# Output: Maximum length of subarray with sum at most twice its length
print(solve(nums))