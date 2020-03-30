class Solution:
    def calcEquation(self, equations, values, queries):

        def find(x):
            if x != U[x][0]:
                r_x, r_v = find(U[x][0])
                U[x] = (r_x, U[x][1] * r_v)
            return U[x]

        def judge(x, y):
            r_x, v_x = find(x)
            r_y, v_y = find(y)
            if r_x != r_y:
                return -1.0
            else:
                return v_x/v_y

        U= {}
        for (x, y), z in zip(equations, values):
            if x not in U and y not in U:
                U[x] = (y, z)
                U[y] = (y, 1.0)
            elif x not in U:
                U[x] = (y, z)
            elif y not in U:
                U[y] = (x, 1.0/z)
            else:
                r_x, v_x = find(x)
                r_y, v_y = find(y)
                U[r_x] = (r_y, z/v_x*v_y)

        res = [judge(x, y) if x in U and y in U else -1.0 for x, y in queries]

        return res
