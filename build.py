def build(nums):
    if nums is None:
        return False
    pos = 0
    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1
    if pos < len(nums):
        nums[pos:] = [0] * (len(nums) - pos)
        print(nums)


