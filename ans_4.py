def max_consecutive_sum(nums, k):
    if len(nums) < k:  # Handle edge case where k is larger than list length
        return "Invalid input: k is larger than the list size"

    max_sum = current_sum = sum(nums[:k])  # Compute the sum of first k elements

    for i in range(k, len(nums)):  
        current_sum += nums[i] - nums[i - k]  # Slide the window
        max_sum = max(max_sum, current_sum)  # Update max sum if current sum is greater

    return max_sum

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 27, 18, 19, 20]
b = max_consecutive_sum(nums, 5)  # Find max sum of 5 consecutive elements
print(b)
