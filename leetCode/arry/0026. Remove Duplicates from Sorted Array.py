# 此題使用快慢指針法解決
def removeDuplicates(nums):
    # 初始化慢指針
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            # 慢指針移動一次
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1  # 慢指針要到最後一個，這時快指針=None，所以要加 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
