import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums_3 = sorted(nums1 + nums2)

        # Odd
        if len(nums_3) % 2 != 0:
            mid_number = nums_3[math.ceil(len(nums_3) / 2) - 1]
            return float(mid_number)

        # Even
        if len(nums_3) % 2 == 0:
            first_mid_number = nums_3[math.ceil(len(nums_3) / 2) - 1]
            sec_mid_number = nums_3[math.ceil(len(nums_3) / 2)]
            mid = (first_mid_number + sec_mid_number) / 2
            return mid