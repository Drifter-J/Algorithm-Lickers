# problem link: https://leetcode.com/problems/remove-invalid-parentheses

import itertools

pas = ['(', ')']

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = set()
        remove_list = []
        basic = self.parsing_parentheses(s)
        result.add(basic)
        pa_list = []
        
        for i, ch in enumerate(s):
            if ch in pas:
                pa_list.append(i)
        
        diff = len(s) - len(basic)        
        remove_list = itertools.combinations(pa_list, diff)
                
        for r_list in remove_list:
            tmp_l = list(s)
            for i in reversed(r_list):
                tmp_l.pop(i)
            if self.parsing_parentheses(tmp_l, True):
                tmp_s = ''.join(tmp_l)
                result.add(tmp_s)
        
        return list(result)
        
        
        
    def parsing_parentheses(self, s, check_valid=False):
        stack = list()
        result = list()
        removed = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append([ch, i - removed])
                result.append(ch)
            elif ch == ')':
                if len(stack) > 0 and stack[-1][0] == '(':
                    stack.pop()
                    result.append(ch)
                else:
                    if check_valid:
                        return False
                    else:
                        removed += 1
                
            else:
                result.append(ch)
        
        for remain in stack[::-1]:
            if remain[0] == '(':
                if check_valid:
                    return False
                else:
                    result.pop(remain[1])
            
        if check_valid:
            return True
        else:
            return ''.join(result)
