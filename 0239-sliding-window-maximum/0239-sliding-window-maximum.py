class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        n = len(nums)
        p = deque()
        for i, num in enumerate(nums):
            while p and nums[p[-1]] <= num:
                p.pop()
            p.append(i)

            if p[0] <= i - k:
                p.popleft()
            if i >= k - 1:
                ret.append(nums[p[0]])

        return ret 