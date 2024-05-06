def run(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    nums.sort()
    count = 1
    idx = 1
    while idx < len(nums):
        if nums[idx - 1] == nums[idx]:
            count += 1
        else:
            count = 1

        if count >= len(nums) /2:
            return nums[idx]
        idx += 1