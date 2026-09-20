from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qs(arr, l, r):
            if l >= r:
                return
            pivot = arr[random.randint(l, r)]
            i, j = l, r
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            qs(arr, l, j)
            qs(arr, i, r)
        qs(nums, 0, len(nums)-1)
        return nums
