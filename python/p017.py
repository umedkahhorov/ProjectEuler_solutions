import time
"""
one, two, three, four, five, then there are 3+3+5+4+4=19 letters
If all the numbers from 1 to 1000 (one thousand) inclusive were written 
out in words, how many letters would be used? 

"""

def int_to_words(n):
    def convert_digit(digit):
        ones = ["","one","two","three","four","five","six","seven","eight","nine"]
        tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
        teens = ["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"] 
        if digit==0:
            return ""
        elif digit<10:
            return ones[digit]
        elif digit<20:
            return teens[digit-10]
        else:
            tens_digit = digit//10
            ones_digit = digit%10
            return tens[tens_digit]+" "+ones[ones_digit]
    if n==0:
        return "zero"
    elif n<0:
        return "negative" + int_to_words(-n)
    else:
        parts = []
        if n>=1000000:
            parts.append(int_to_words(n//1000000)+" million")
            n%=1000000
        if n>=1000:
            parts.append(int_to_words(n//1000)+" thousand")
            n%=1000
        if n>=100:
            parts.append(int_to_words(n//100)+" hundred")
            n%=100
        if n>0:
            parts.append(convert_digit(n))
        return " ".join(parts)
    
if __name__ == "__main__":
    print (int_to_words(190))

    