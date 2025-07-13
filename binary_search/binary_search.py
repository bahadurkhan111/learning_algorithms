


def binary_search(nums, target):


    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:

        mid = (left_index + right_index) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left_index = mid + 1
        else:
            right_index = mid - 1

    return "NO found"



nums = [1, 3, 5, 7, 9, 11, 13]
target = 11
print(binary_search(nums, target))


