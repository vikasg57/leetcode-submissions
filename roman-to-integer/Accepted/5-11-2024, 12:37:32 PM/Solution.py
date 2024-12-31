// https://leetcode.com/problems/roman-to-integer

class Solution(object):
    def romanToInt(self, s):

        s_l_roman_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        roman_int = 0
        prev = s[0]

        for i, r in enumerate(s):
            if i > 0:
                if r in ("V", "X") and prev == "I":
                    roman_int -= s_l_roman_dict.get(prev)
                    if r == "V":
                        roman_int += 4
                    else:
                        roman_int += 9
                elif r in ("L", "C") and prev == "X":
                    roman_int -= s_l_roman_dict.get(prev)
                    if r == "L":
                        roman_int += 40
                    else:
                        roman_int += 90
                elif r in ("D", "M") and prev == "C":
                    roman_int -= s_l_roman_dict.get(prev)
                    if r == "D":
                        roman_int += 400
                    else:
                        roman_int += 900
                else:
                    roman_int += s_l_roman_dict.get(r)
            else:
                roman_int += s_l_roman_dict.get(r)
            prev = r
        return roman_int