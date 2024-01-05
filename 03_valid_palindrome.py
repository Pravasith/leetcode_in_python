# Problem Link - https://leetcode.com/problems/valid-anagram/description/
import string

charset = set()

for ch in string.ascii_letters:
    charset.add(ch)

for ch in string.digits:
    charset.add(ch)

class Solution:
    def isAlphaNumeric(self, x: str) -> bool:
        if x in charset:
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        p1, p2 = 0, len(s) - 1

        while p2 > p1:
            l = s[p1]
            r = s[p2]


            if not self.isAlphaNumeric(l):
                p1 += 1
                continue
            if not self.isAlphaNumeric(r):
                p2 -= 1
                continue

            if l.lower() != r.lower():
                return False

            p1 += 1
            p2 -= 1

        return True

# Test cases
solution = Solution()

print(solution.isPalindrome("sex iSs x, ss+i xes"))
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(""))

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
