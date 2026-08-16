

class Solution:
    def majorityElement(self, nums):
        count = Counter(nums)
        n = len(nums)

        return [x for x in count if count[x] > n // 3]