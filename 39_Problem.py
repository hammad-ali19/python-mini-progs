# Problem 39: Container With Most Water
# You are given an array height where each element represents the height of a vertical line. The lines are 
# drawn at indices (i, height[i]). Find two lines that, together with the x-axis, form a container that holds 
# the most water. Return the maximum amount of water that can be contained.

# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]

# Output: 49
# Explanation: The two lines at indices 1 and 8 (with heights 8 and 7, respectively) form a container that 
# holds the most water (area = width × height = 7 × 7 = 49).

def max_water_container (height):
    if len(height) < 2:
        return "invalid width"
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        if area > max_area:
            max_area = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return (max_area)


print(max_water_container ([1, 3, 2, 5, 25, 24, 5]))