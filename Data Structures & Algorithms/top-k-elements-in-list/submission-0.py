class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countN = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            countN[i] = 1 + countN.get(i, 0)

        for n, c in countN.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
