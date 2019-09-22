# https://leetcode.com/submissions/detail/263144222/

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = [0]*len(T)
        stack=[]
        for i in range(len(T)-1):
            stack.append(i)
            while stack and T[stack[-1]]<T[i+1]:
                output[stack[-1]] = (i+1)-stack[-1]
                stack.pop()               
        return output

