class Solution:
    def findCircleNum(self, M):
        roots = [i for i in range(len(M))]
        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    r_i = find(i)
                    r_j = find(j)
                    roots[r_j] = r_i
        for i in range(len(roots)):
            find(i)
        return len(set(roots))