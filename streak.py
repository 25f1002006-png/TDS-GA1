def longest_positive_streak(nums: list[int]) -> int:
    """
    Return the length of the longest consecutive run of values > 0.
    """
    longest = 0
    current = 0
    for n in nums:
        if n > 0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest
