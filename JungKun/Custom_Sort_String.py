class Solution:
    def customSortString(self, S: str, T: str) -> str:
        l =[]
        for i in S:
            l.append(i*T.count(i))
        for i in T:
            if i not in S:
                l.append(i)
        return ''.join(l)
