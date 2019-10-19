# problem link: https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        word_list = reversed(s.split())
        return ' '.join(word_list)
        
