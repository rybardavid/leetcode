def run(nums: list[int]) -> bool:
    checkedNumbers = {}
    for num in nums:
        try:
            return checkedNumbers[num]
        except KeyError:
            checkedNumbers[num] = True
    return False