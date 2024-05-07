def run(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) -1
    finalNums = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            finalNums.append(nums[left] ** 2)
            left += 1
        else:
            finalNums.append(nums[right] ** 2)
            right -= 1

    return finalNums[::-1]