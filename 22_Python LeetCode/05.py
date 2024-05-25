class Solution:
    def RomanToInt(self, s):
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        current = 0
        total = 0
        prev = 0

        for i in range(len(s)):
            current = roman_dict[s[i]]

            if current > prev:
                total += current - 2 * prev
            else:
                total += current

            prev = current

        return total
