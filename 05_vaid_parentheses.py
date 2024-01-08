# https://leetcode.com/problems/binary-search/

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        i = 0

        while i < len(s):
            curr = s[i]
            if curr == '(' or curr == '{' or curr == '[':
                stack.append(curr)
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if curr == ')':
                    if x != '(':
                        return False
                if curr == '}':
                    if x != '{':
                        return False
                if curr == ']':
                    if x != '[':
                        return False

            i = i + 1
        if len(stack) == 0:
            return True
        return False

# Test cases
solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]{}"))


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
