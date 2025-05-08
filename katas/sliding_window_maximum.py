def max_sliding_window(nums, k):
    """
    Given an array of integers and a sliding window size, your task is to find the maximum value
    in the window at each position as the window slides from left to right.

    For example, given the array [1, 3, -1, -3, 5, 3, 6, 7] and window size 3:
    The output should be [3, 3, 5, 5, 6, 7].

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

    Args:
        nums: list of integers
        k: the size of the sliding window

    Returns:
        A list of the maximum values in each window
    """
    return []


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    result = max_sliding_window(nums, k)
    print(f"Sliding window maximums: {result}")  # Expected: [3, 3, 5, 5, 6, 7]

    # Additional test cases
    nums2 = [9, 11, 3, 4, 8, 7]
    k2 = 2
    result2 = max_sliding_window(nums2, k2)
    print(f"Sliding window maximums: {result2}")  # Expected: [11, 11, 4, 8, 8]

    nums3 = [1, -1]
    k3 = 1
    result3 = max_sliding_window(nums3, k3)
    print(f"Sliding window maximums: {result3}")  # Expected: [1, -1]