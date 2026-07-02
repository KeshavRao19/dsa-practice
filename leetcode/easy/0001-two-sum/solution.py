"""
Two Sum

LeetCode link: https://leetcode.com/problems/two-sum/

Approach:
    Use a hashmap to store each number and its index while iterating once.
    For each number, check whether its complement (target - num) has
    already been seen. If so, the pair is found.

Time complexity:  O(n) — single pass, O(1) average hashmap lookups
Space complexity: O(n) — hashmap holds up to n elements
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of the two numbers in nums that add up to target.

        Args:
            nums: List of integers.
            target: Target sum.

        Returns:
            A list of two indices [i, j] such that nums[i] + nums[j] == target.

        Raises:
            ValueError: If no valid pair exists in the input.
        """
        seen = {}  # num -> index, tracks numbers we've already visited

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        raise ValueError("No two sum solution exists for this input")