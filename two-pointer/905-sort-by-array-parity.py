# Intuition: Swap only when even no. is encountered, After swapping increment left pointer (l)


def sortArrayByParity(nums: List[int]) -> List[int]:
    l, r = 0, 0
    while r < len(nums):
        if nums[r] % 2 == 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        r += 1
    return nums


nums = [0, 2, 1, 4]
result = sortArrayByParity(nums)
print(result)
