def run(nums: list[int]) -> int:
    maxArea = 0
    l, r, = 0, len(nums) - 1
    while l < r:
        lenght = r - l
        height = nums[l] if nums[l] < nums[r] else nums[r]

        area = lenght * height
        if area > maxArea:
            maxArea = area

        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return maxArea