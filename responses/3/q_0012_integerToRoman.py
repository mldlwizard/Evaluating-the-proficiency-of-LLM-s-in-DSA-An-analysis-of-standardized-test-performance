class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        
        roman_numeral = ''
        
        for value, numeral in mapping.items():
            while num >= value:
                roman_numeral += numeral
                num -= value
        
        return roman_numeral