class Solution:
    
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        total = 0
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                total += i
                if i != num // i and i != 1:
                    total += num // i
        
        return total - num == num
