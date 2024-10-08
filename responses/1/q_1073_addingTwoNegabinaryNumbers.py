from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += arr1[i]
                i -= 1
            if j >= 0:
                carry += arr2[j]
                j -= 1
            result.append(carry & 1)
            carry = -(carry >> 1)

        # Remove leading zeros in the result
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return result[::-1]