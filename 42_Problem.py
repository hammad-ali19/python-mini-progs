# Problem 22: Subarray Sum Equals K
# Given an array of integers nums and an integer k, find the total number of continuous 
# subarrays whose sum equals to k.

def count_subarrays_sum_equalto_k (nums, k):
    counter = 0
    i = 0
    while i < len(nums):
        sum = 0
        for j in range(i, len(nums)):
            if nums[i] == k:
                counter += 1
                i += 1
                break
            sum += nums[j]
            if sum == k:
                counter += 1
                print(i, j)
                i += 1
                break
            elif sum > k:
                i += 1
                break
        else:
            return counter
    return counter


nums = [1, 1, 1, 3, 2, 1, 4, 5]
print(count_subarrays_sum_equalto_k(nums, 1))