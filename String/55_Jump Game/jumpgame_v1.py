#class Solution:
#   def canJump(self, nums: list[int]) -> bool:
nums = [2,3,1,1,4]
n = len(nums)
goal = n - 1

for i in range(n - 2, -1, -1):
    if i + nums[i] >= goal:
        goal = i

# If the goal is the first index, return True
if goal == 0:
    print(True)
else:
    print(False)