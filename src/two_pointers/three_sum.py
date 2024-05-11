def run(nums: list[int]) -> list[list[int]]:
    nums.sort()

    triplets = set()
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
                triplet = (nums[j],  nums[l], nums[r])
                if triplet not in triplets:
                    triplets.add(triplet)
                l += 1
                r -= 1
        j += 1

    return [list(triplet) for triplet in triplets]