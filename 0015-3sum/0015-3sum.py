class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ret = []
        for i in range(n):
            if nums[i] > 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                        continue
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return ret