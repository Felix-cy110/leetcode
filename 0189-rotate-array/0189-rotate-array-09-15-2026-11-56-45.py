class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        newArray = [0] * n
        for i in range(n):
            newArray[(i+k)%n] = nums[i]
        nums[:] = newArray