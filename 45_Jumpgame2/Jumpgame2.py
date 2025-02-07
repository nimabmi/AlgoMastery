def jump2(nums):
    n = len(nums)
    j = 0
    out = 0
    while j < n - 1:
        far = max(nums[ j + 1 : j + nums[j] + 1])
        print(far)
        j = j + far
        out += 1
    return out
nums = [3, 1, 4, 2, 5, 6, 2, 1, 8, 7]
jump2(nums)