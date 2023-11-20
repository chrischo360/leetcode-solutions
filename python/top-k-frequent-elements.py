# time: O(n log n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count using Counter then find the k most frequent elements
        counter = Counter(nums)
        arr = []

        for num in counter:
            arr.append((counter[num], num))
        
        arr = sorted(arr)
        res = []

        for i in range(k):
            res.append(arr.pop()[1])

        return res
