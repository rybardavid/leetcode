def run(nums: list[int]) -> list[list[int]]:
    nums.sort()

    triplets = []
    j = 0
    while j < len(nums):
        l, r = j + 1, len(nums) - 1
        while l < r:
            numSum = nums[j] + nums[l] + nums[r]
            if numSum < 0:
                l += 1
            elif numSum > 0:
                r -= 1
            else:
                triplets.append([nums[j],  nums[l], nums[r]])
                break
        j += 1
    return triplets