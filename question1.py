"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2021
question1.py - DP planks with turtle
"""

### Longest Palindrome
test_cases = ["a", "rarfile", 'abaab', "0000000000000ooooo00ooooo", "windows", "saippuakivikauppias",
     "abrakadabra", "123412341234", "professordigbo", "tarattarat", "bab", "a123321a", "kd",
     "123232223388939389393837389393999999999999999999999999999999999338839", 'bullet',
     "ululululululululululululululululululululululullululululululululululululululul",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabkkkkkkl", 'racecar'
]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0  # Start position of longest palindrome
        end = 0  # End position of longest palindrome
        list = []
        diff = 0

        for i in range(0, len(s)):
            if i<len(s)-1 and s[i]==s[i+1]:
                list = self.expand_around(s,i-1,i+2)
            else:
                list = self.expand_around(s, i-1, i+1)
            if list is not None and (list[1] - list[0])> diff:
                diff = list[1] - list[0]
                start = list[0]
                end = list[1]

            # Palindome can be centered around 1 character or 2 characteres.
            # example aba  -> center is a
            #         abba -> center is bb
            # Try both methods and see which one gives the longer palindome.


            '''
            Fill your code here!
            '''

        return s[start: end + 1]

    def expand_around(self, s, left, right):
        if left >-1 and right < len(s):
            if s[left] == s[right]:
                return self.expand_around(s,left-1, right+1)

        return [left+1,right-1]

        pass


if __name__ == "__main__":
    solution = Solution()

    for test_case in test_cases:
        print(solution.longestPalindrome(test_case))
