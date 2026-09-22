from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qs(arr, l, r):
            if l >= r:
                return
            n = len(arr)
            pivot = nums[random.randint(l, r)]
            i,j = l, r
            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            qs(arr, i, r)
            qs(arr, l, j)
        qs(nums, 0, len(nums) - 1)
        return nums