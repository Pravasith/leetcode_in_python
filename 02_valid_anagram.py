# Problem Link - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def validAnagram(self, nums: list[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            else:
                my_set.add(num)

        return False

# Test cases
solution = Solution()

def PrintResult(func, input, answer):
    result = func(input)

    print(
        "Passed" if  answer == result else "Failed"
    )

PrintResult(solution.containsDuplicate, [10, 2], False)
PrintResult(solution.containsDuplicate, [10, 2, 22, 15, 2], True)
PrintResult(solution.containsDuplicate, [10, 2, -1, 342, -12], False)
PrintResult(solution.containsDuplicate, [10], False)
PrintResult(solution.containsDuplicate, [], False)
