class Solution:
    def trap(self, height: list[int]) -> int:
        lmax, rmax = 0, 0
        l, r = 0, len(height) - 1
        ret = 0
        while l <= r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if lmax < rmax:
                ret += lmax - height[l]
                l += 1
            else:
                ret += rmax - height[r]
                r -= 1
        return ret