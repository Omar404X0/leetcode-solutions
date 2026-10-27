
class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        neg = False
        number = False
        sign_found = False
        
        for chr in s:
            if not sign_found and not number and ord(chr) == 32:
                continue
            
            if not number and not sign_found:
                if not ord(chr) in range(48, 58) and ord(chr) != 43 and ord(chr) != 45:
                    return 0
                sign_found = True
                if ord(chr) == 45:
                    neg = True
                elif ord(chr) == 43:
                    neg = False
                elif ord(chr) in range(48, 58):
                    number = True
                    res = (res * 10) + (ord(chr) - ord('0'))
                continue

            if number == True and (ord(chr) == 45 or ord(chr) == 43):
                break

            if ord(chr) in range(48, 58):
                number = True
                res = (res * 10) + (ord(chr) - ord('0'))
                
                # حماية الـ Overflow
                if not neg and res > 2147483647:
                    return 2147483647
                if neg and res > 2147483648:
                    return -2147483648
            else:
                break

        if neg:
            return res * -1
        else:
            return res