# Problem 41: Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.

def k_frequent_elements (nums, k):
    nums_set = set(nums)
    if len(nums_set) == 1:
        return [nums_set.pop()]
    occurences = {}
    for num in nums_set:
        count = 0
        for i in range(len(nums)):
            if num == nums[i]:
                count += 1
        occurences[num] = count

    occurences_list = sorted(occurences.items(), key=lambda item : item[1], reverse=True)
    frequent_elements = []
    for i in range(k):
        frequent_elements.append(occurences_list[i][0])

    return (frequent_elements)

nums = [1, 1, 1, 1, 2, 3, 4, 5, 6, 3]
print(k_frequent_elements(nums, 2))              # Output: [1, 3]