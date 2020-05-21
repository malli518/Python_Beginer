
def sort(nums):
    for i in range(len(nums)):
        mispos = i
        for j in range(i, 6):
            if nums[j] < nums[mispos]:
                mispos = j
        temp = nums[i]
        nums[i] = nums[mispos]
        nums[mispos] = temp
        print(nums)


nums = [3, 5, 6, 8, 2, 4]
sort(nums)
print(nums)
