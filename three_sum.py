class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        posi_int = sorted([n for n in nums if n > 0])
        neg_int = sorted([n for n in nums if n < 0])
        zeros = [n for n in nums if n == 0]
        res = set([])
        if len(zeros) >= 3:
            res.add((0, 0, 0))
        if len(zeros) > 0:
            for i in posi_int:
                if -i in neg_int:
                    temp = (-i, 0, i)
                    res.add(temp)

        for i in range(len(neg_int) - 1):
            for j in range(i + 1, len(neg_int)):
                if -(neg_int[i] + neg_int[j]) in posi_int:
                    temp = (neg_int[i], neg_int[j], -(neg_int[i] + neg_int[j]))
                    res.add(temp)

        for i in range(len(posi_int) - 1):
            for j in range(i + 1, len(posi_int)):
                if -(posi_int[i] + posi_int[j]) in neg_int:
                    temp = (-(posi_int[i] + posi_int[j]),
                            posi_int[i], posi_int[j])
                    res.add(temp)

        return list(res)
