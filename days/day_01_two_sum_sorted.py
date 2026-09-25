"""
Day 01: Two Pointers - Two Sum II (Input Array Is Sorted)
Derivation & test cases.
"""

def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """
    Find two distinct elements in a sorted array that sum to target.
    Returns 0-indexed indices [left, right], or [] if no pair exists.
    Time Complexity: O(n)
    Auxiliary Space Complexity: O(1)
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


def test_two_sum_sorted():
    # Standard positive case
    assert two_sum_sorted([2, 7, 11, 15], 9) == [0, 1]

    # Negative numbers: -5 + 4 = -1 (indices [0, 4])
    assert two_sum_sorted([-5, -3, 0, 2, 4], -1) == [0, 4]

    # Duplicates present
    assert two_sum_sorted([1, 2, 2, 3, 5], 4) == [0, 3] or two_sum_sorted([1, 2, 2, 3, 5], 4) == [1, 2]

    # Target at opposite ends
    assert two_sum_sorted([1, 3, 5, 9], 10) == [0, 3]

    # Target does not exist
    assert two_sum_sorted([1, 2, 3, 9], 20) == []

    print("All Two Sum II test cases passed successfully!")


if __name__ == "__main__":
    test_two_sum_sorted()
