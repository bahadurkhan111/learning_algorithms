


def linear_search(nums, target):

    for i in range(0,  len(nums)):


        if target == nums[i]:
            print("Number found at index: ", i)
            return True
        
    return False

nums = [5, 6,2,3,55,22, 55,11,323,55,33,666,9,103]

linear_search(nums, 22)