class Solution:
    def numSimilarGroups(self, A):
        roots = [i for i in range(len(A))]
        L = len(A[0])

        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                difference = 0
                for l in range(L):
                    if A[i][l] != A[j][l]:
                        difference += 1
                if difference <= 2:
                    r_i = find(i)
                    r_j = find(j)
                    roots[r_j] = r_i

        for i in range(len(A)):
            find(i)
        return len(set(roots))

test = Solution()
res = test.numSimilarGroups(["ajdidocuyh","djdyaohuic","ddjyhuicoa","djdhaoyuic","ddjoiuycha","ddhoiuycja","ajdydocuih","ddjiouycha","ajdydohuic","ddjyouicha"])
print(res)
