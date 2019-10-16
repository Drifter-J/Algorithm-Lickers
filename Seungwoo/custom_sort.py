class Solution:
    def index_lst(lst, x):
        if x in lst:
            return lst.index(x)
        else:
            return -1
    def customSortString(self, S: str, T: str) -> str:
        
        return ''.join(sorted(T, key = lambda x:Solution.index_lst(S, x)))