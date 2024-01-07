# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if target > nums[r] or target < nums[l]:
            return -1

        while l <= r:
            mid = ((r - l) // 2) + l

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

# Test cases
solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 12))


# def PrintResult(func, input, answer):
#     result = func(input)
#
#     print(
#         "Passed" if  answer == result else "Failed"
#     )

# PrintResult(solution.containsDuplicate, [10, 2], False)
# PrintResult(solution.containsDuplicate, [10, 2, 22, 15, 2], True)
# PrintResult(solution.containsDuplicate, [10, 2, -1, 342, -12], False)
# PrintResult(solution.containsDuplicate, [10], False)
# PrintResult(solution.containsDuplicate, [], False)
