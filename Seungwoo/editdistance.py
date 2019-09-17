class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l = word1
        r = word2 
        
        dists = []
    
        for i in range(len(l)+1):
            dists.append([])
            for j in range(len(r)+1):
                dists[-1].append(0)

        for i in range(len(l)+1):
            dists[i][0] = i 
        for j in range(len(r)+1):
            dists[0][j] = j 

        for i in range(1, len(l)+1):
            for j in range(1, len(r)+1):
                if l[i-1] == r[j-1]:
                    dists[i][j] = min(\
                        dists[i-1][j] + 1, 
                        dists[i][j-1] + 1, 
                        dists[i-1][j-1])
                else:
                    dists[i][j] = min(\
                        dists[i-1][j] + 1, 
                        dists[i][j-1] + 1, 
                        dists[i-1][j-1] + 1,)
        return dists[-1][-1]