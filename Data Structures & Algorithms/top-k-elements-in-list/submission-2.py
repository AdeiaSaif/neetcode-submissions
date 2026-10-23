class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = Counter(nums)
        print(topk.most_common(k))
        return [item[0] for item in topk.most_common(k)]