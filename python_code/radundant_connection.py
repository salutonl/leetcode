class Solution:
    def findRedundantConnection(self, edges):
        roots = [i for i in range(len(edges) + 1)]
        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
        for x, y in edges:
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return [x, y]
            else:
                roots[root_y] = root_x
