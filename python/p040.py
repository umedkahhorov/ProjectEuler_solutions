# Champernowne constant C10 = 0.1234567891011121314151617181920... concatenating  by positive integers
# f dn represents the n-th digit of the fractional part d1xd10xd100xd1000xd10000xd100000xd1000000xd10000000...
# Find the value of the following expression using python
# f1 x f10 x f100 x f1000 x f10000 x f100000 x f1000000

def champernownes_constant(n):
    series = "0." + "".join(str(i) for i in range(1, n))
    product = 1
    indexes = [1, 10, 100, 1000, 10000, 100000, 1000000]
    for digit in indexes:
        product *=int(series[digit+1])
    product0 = 1
    for i in range(7):
        product0 *= int(series[10**i+1])
    print(product0)
    print(product)
    return None

if __name__ == "__main__":
    champernownes_constant(1000000)
# Output: 210
    