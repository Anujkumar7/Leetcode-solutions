class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x:(x[0] , -x[1]))
        res = []
        #Perform LIS
        for _, h in envelopes:
            index = bisect_left(res, h)
            if index == len(res):
                res.append(h)
            else:
                res[index]= h
        return len(res)
        