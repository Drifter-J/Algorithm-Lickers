# https://leetcode.com/submissions/detail/272507879/
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
