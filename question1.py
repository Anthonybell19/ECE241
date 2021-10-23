"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2021
question1.py - DP planks with turtle
"""

### Longest Palindrome
test_cases = [
    "a", "abaab", "racecar", "bullet", "rarfile",
    "computer", "windows", "saippuakivikauppias",
    "aaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "kkkkkkkkkkkkkkkkkkkkkkdldkkkkkkkkkkkkkkkkkkkkkk",
    "ddddddddddddddddddddddddddddddddddddddddddddddddddks"
]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0  # Start position of longest palindrome
        end = 0  # End position of longest palindrome

        for i in range(0, len(s)):
            # Palindome can be centered around 1 character or 2 characteres.
            # example aba  -> center is a
            #         abba -> center is bb
            # Try both methods and see which one gives the longer palindome.

            '''
            Fill your code here!
            '''
            pass

        return s[start: end + 1]

    def expand_around(self, s, left, right):
        '''
        Fill your code here!
        '''
        pass


if __name__ == "__main__":
    solution = Solution()

    for test_case in test_cases:
        print(solution.longestPalindrome(test_case))
