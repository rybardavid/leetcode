def run(nums: list[int]) -> None:
   left = 0
   right = len(nums) -1

   while(left < right):
        if nums[left] == 0:
            nums.pop(left)
            nums.append(0)
            right -= 1
        else:
            left += 1