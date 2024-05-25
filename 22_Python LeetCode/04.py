"""Stringg to integer(atoi) Leetcode 08"""
class solution:
    def MYAtoi(self , str):
        str = str.strip()#to remove whitespace

        if not str:
            return 0
        negative = False
        out = 0

        if str[0] == "-":
            negative = True
        elif str[0] == "+":
            negative = False
        elif not str[0].isnumeric:
            return 0
        else:
            out = ord(str[0] - ord["0"]) #ord will give ASCII VALUE

        for i in range(1 , len(str)):
            if str[i].isnumeric():
                out = out*10 + (ord(str[i] - ord["0"]))
                if not negative and out >= 2147483637:
                    return 2147483637
                if negative and out >= 2147483637:
                    return -2147483637
            else:
                break
        if not negative:
            return out
        else:
            return -out
