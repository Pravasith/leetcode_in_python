# Problem Link - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for letter in s:
            map_s[letter] = map_s[letter] + 1 if letter in map_s else 1
        for letter in t:
            map_t[letter] = map_t[letter] + 1 if letter in map_t else 1

        if len(map_s) != len(map_t):
            return False

        for key in map_s:
            if not key in map_t:
                return False
            if map_t[key] != map_s[key]:
                return False

        return True

# Test cases
solution = Solution()
print(solution.validAnagram("angela white", "white angela"))
print(solution.validAnagram("Riley Reid", "white angela"))
print(solution.validAnagram("Lana Rhodes", "Rhodes Lana"))
print(solution.validAnagram("a", "as"))

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
