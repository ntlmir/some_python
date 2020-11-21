class Solution:

    roman = {'I' : 1, 
             'V' : 5, 
             'X' : 10, 
             'L' : 50, 
             'C' : 100, 
             'D' : 500, 
             'M' : 1000}

    def romanToInt(self, s: str):

        if self.checkRomanRules(s) == True:
            number = 0
            i = 0
            while i < len(s):
                if i != len(s) - 1:
                    if self.roman[s[i+1]] <= self.roman[s[i]]:
                        number += self.roman[s[i]]
                        i += 1
                    else:
                        number += self.roman[s[i+1]] - self.roman[s[i]]
                        if self.roman[s[i+1]] - self.roman[s[i]] < 10 and i != len(s)-2:
                            print("Wrong sequence of chars.")
                            return False
                        i += 2
                else:
                    number += self.roman[s[i]]
                    i += 1
            return number

    def checkRomanRules(self, s: str):

        if 1 <= len(s) <= 15:

            for char in s:
                if char not in self.roman:
                        print("Wrong char in number.")
                        return False

            i = 0
            rep = 1
            while i < len(s):
                if i != len(s)-1 and s[i] == s[i+1]:
                    rep += 1
                    if (rep == 2 or rep == 3) and i+2 < len(s) and self.roman[s[i+2]] > self.roman[s[i]]:
                        print("Wrong sequence of chars.")
                        return False
                    if rep > 3:
                        print("Char can't repeat 4 times in a row.")
                        return False
                else:
                    rep = 1

                if i != len(s)-1 and self.roman[s[i]] < self.roman[s[i+1]]:
                    if ((s[i] != 'I' and s[i] != 'X' and s[i] != 'C') or
                        s[i] == 'I' and (s[i+1] != 'V' and s[i+1] != 'X') or
                        s[i] == 'X' and (s[i+1] != 'L' and s[i+1] != 'C') or
                        s[i] == 'C' and (s[i+1] != 'D' and s[i+1] != 'M')):
                        print("Wrong sequence of chars.")
                        return False
                i += 1

            if s.count('V') > 1 or s.count('L') > 1 or s.count('D') > 1:
                print("Chars V, L, D can't repeat.")
                return False
        else:
            print("Wrong number's lenght. Should be from 1 to 15.")
            return False

        return True
