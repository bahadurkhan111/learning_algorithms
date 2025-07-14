


def bubble_sort(nums1):

    for i in range(0, len(nums1)):

        for j in range(0, len(nums1)):

            if nums1[i] <  nums1[j]:
                temp = nums1[i]
                nums1[i] = nums1[j]
                nums1[j] = temp

    return nums1


nums = [3, 5,1,8, 9, 33, 2, 4]

print(bubble_sort(nums))