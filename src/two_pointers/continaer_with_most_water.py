def run(nums: list[int]) -> int:
    maxArea = 0
    l, r, = 0, len(nums) - 1
    while l < r:
        lenght = r - l
        height = min(nums[l], nums[r])

        area = lenght * height
        maxArea = max(maxArea, area)

        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return maxArea