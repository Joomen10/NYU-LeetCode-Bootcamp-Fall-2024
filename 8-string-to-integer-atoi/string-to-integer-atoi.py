class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()  
        if len(str) == 0:
            return 0
        
        sign = 1 
        value = 0
        pos = 0
        
        if str[pos] == "+" or str[pos] == "-":
            sign = 1 if str[pos] == "+" else -1
            pos += 1
        
        
        while pos < len(str) and str[pos].isdigit():
            value = value * 10 + int(str[pos])
            pos += 1
        
        value = sign * value

        value = max(-(2 ** 31), min(value, 2 ** 31 - 1))
        
        return value
