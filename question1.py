"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2021
question1.py - DP planks with turtle
"""

### Longest Palindrome
test_cases = [
     # "a", "abaab",
    "racecar",
    # "bullet", "rarfile",
    # "computer", "windows",
    "saippuakivikauppias",
    # "aaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    # "kkkkkkkkkkkkkkkkkkkkkkdldkkkkkkkkkkkkkkkkkkkkkk",
    # "ddddddddddddddddddddddddddddddddddddddddddddddddddks"
]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0  # Start position of longest palindrome
        end = 0  # End position of longest palindrome
        list = []
        str = ''
        tempStart = 0
        tempEnd=0

        for i in range(0, len(s)):
            list = self.expand_around(s, i-1, i+1)
            val = 1
            while list is not None:
                tempStart = list[0]
                tempEnd = list[1]
                list = self.expand_around(s, tempStart - val, tempEnd + val)
                val+=1

            if len(s[tempStart:tempEnd+1]) > len(str):
                str = s[tempStart:tempEnd+1]
                start = tempStart
                end = tempEnd

            # Palindome can be centered around 1 character or 2 characteres.
            # example aba  -> center is a
            #         abba -> center is bb
            # Try both methods and see which one gives the longer palindome.
        #     v= 1
        #     list = self.expand_around(s, start-v, end +v)
        #
        # while list is not None:
        #     tempStart = list[0]
        #     tempEnd = list[1]
        #     v+=v
        #     list = self.expand_around(s, start - v, end + v)
        #


        # for i in range(1,endpoint):
        #     print(i)
        #     print(start, end)
        #     # print(s)
        #     list = self.expand_around(s, start - i, end + i)
        #     if list is not None and list[0]!= start:
        #         start = list[0]
        #         end = list[1]
        #     else:
        #         break


            '''
            Fill your code here!
            '''
            pass

        return s[start: end + 1]

    def expand_around(self, s, left, right):
        if left != -1 and right < len(s):
            if s[left] == s[right]:
                return [left, right]

        '''
        Fill your code here!
        '''
        pass


if __name__ == "__main__":
    solution = Solution()

    for test_case in test_cases:
        print(solution.longestPalindrome(test_case))
