import math

class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n+1)]
        result = []

        k -= 1
        while n > 0:
            n -= 1
            index = k // math.factorial(n)
            k %= math.factorial(n)
            result.append(numbers.pop(index))

        return ''.join(result)