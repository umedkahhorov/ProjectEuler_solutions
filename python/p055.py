int1 = 349
reverse_number = lambda x: int(str(x)[::-1])
is_palindromic = lambda x: str(x) == str(x)[::-1]
is_palindromic(int1+reverse_number(int1))
# number that never forms a palindromic  - lychrel number - 196 is the smallest candidate
# how many Lychrel numbers are there below ten-thousand? 249
def lychrel(n, i):
    # iterate i times, adding n and its reverse each time
    # if at any point n becomes palindromic, return False immediately - NOT a Lychrel number
    # only returns True if it survives all i iterations without ever hitting a palindrome - IS a Lychrel number
    for _ in range(i):
        n = n + int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True
max_n = 10000
def compute():
    count = 0
    for number in range(max_n):
        if lychrel(number, 50):
            count += 1
    return count
# test with known Lychrel candidates
print(lychrel(196, 50))  # True
print(compute())  # Should print 249
