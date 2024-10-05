# Problem 38: Find 3SUM
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

def find_triplets (nums):
    length = len(nums)
    if length < 3:
        return "Not a valid array"
    nums.sort()
    triplets = []

    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                if nums[i] +  nums[j] + nums[k] == 0:
                    lst = []
                    lst.append(nums[i])
                    lst.append(nums[j])
                    lst.append(nums[k])
                    if lst not in triplets:
                        triplets.append(lst)

    return triplets


print(find_triplets([-1, 0, 1, 2, -1, -4]))