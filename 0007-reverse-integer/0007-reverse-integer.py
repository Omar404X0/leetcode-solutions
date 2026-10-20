class Solution:
    def reverse(self, x: int) -> int:
        number = str(x)
        result = ''
        postive = True
        if number[0] == '-':
            number = number[1:]
            postive = False
        i = len(number) - 1
        while i >= 0:
            result += number[i]
            i -= 1

        if postive:
            final = int(result)
        else:
            final = int(result) * -1

        if final > 2147483647 or final < -2147483648:
            return 0
        return final