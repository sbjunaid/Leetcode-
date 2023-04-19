#Max Value of Equation


class Solution:
    def findMaxValueOfEquation(self, A, k):
        q = []
        res = -float('inf')
        for x, y in A:
            while q and q[0][1] < x - k:
                heapq.heappop(q)
            if q: res = max(res, -q[0][0] + y + x)
            heapq.heappush(q, (x - y, x))
        return res