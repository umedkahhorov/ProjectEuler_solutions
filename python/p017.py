import time
"""
one, two, three, four, five, then there are 3+3+5+4+4=19 letters
If all the numbers from 1 to 1000 (one thousand) inclusive were written 
out in words, how many letters would be used? 
342 (three hundred and forty-two) contains letters 23
21124
"""
def int_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 1000:
        return "onethousand"
    elif 1 <= n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 20 <= n < 100:
        return tens[n // 10] + ones[n % 10]
    elif 100 <= n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + "hundred"
        else:
            return ones[n // 100] + "hundredand" + int_to_words(n % 100)

def count_letters(n):
    word_list = int_to_words(n)
    return len(word_list)

def count():
    ans = sum(count_letters(i) for i in range(1, 1001))
    return ans

########

def compute():
    ans = sum(len(to_english(i)) for i in range(1,1001))
    return str(ans)

def to_english(n):
    if 0 <= n < 20:
        return ONES[n]
    elif 20 <= n < 100:
        return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return ONES[n//100] + "hundred" +(("and" + to_english(n%100)) if (n%100!=0) else "")
    elif 1000<= n < 1000000:
        return to_english(n//1000) + "thousand" + (to_english(n%1000) if (n%1000!=0) else "") 
    else:
        raise ValueError()
ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
if __name__ == "__main__":
    print(count())
    print (compute())






    