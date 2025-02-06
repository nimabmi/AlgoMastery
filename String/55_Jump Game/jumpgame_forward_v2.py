def canJump(nums):
    n = len(nums)
    farthest = 0  # This will track the farthest index we can reach

    # Iterate over each index
    for i in range(n):
        # If the current index is beyond our farthest reach, return False
        if i > farthest:
            return False
        
        # Update the farthest index we can reach
        farthest = max(farthest, i + nums[i])
        
        # If at any point we can reach the last index, return True
        if farthest >= n - 1:
            return True
    
    # If we exit the loop, check if we can reach the last index
    return farthest >= n - 1

print(canJump([2,3,1,1,4]))