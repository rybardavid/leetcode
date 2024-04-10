def twoSum(nums: list[int], target: int) -> list[int]:
    discoveredNums = {}
    for idx, num in enumerate(nums):
        try:
            diff = target - num
            return [discoveredNums[diff], idx]
        except KeyError:
            discoveredNums[num] = idx