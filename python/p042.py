# coded triangle numbers - riangular Number Sequence: 1, 3, 6, 10, 15, 21, 28, 36, 45, ... It is simply the number of dots in each triangular pattern:
#  * ooo
#n ** oo
#  *** o
#  n+1
# xn = n(n+1)/2 -> x5 = 5(5+1)/2 = 15
# ans 162
import math
alphabet_position = lambda letter: ord(letter.upper()) - ord('A')+1

def read_words(filename):
    """
    Read a file and return a list of words read from it.
    The file is expected to be a plain text file with words separated by commas
    and optionally surrounded by double quotes.
    """
    words = []
    with open(filename,"r") as f:
        for line in f:
            words.extend(word.strip('"') for word in line.strip().split(',')) 
    return words

def find_n(xn):
     # compute discriminant
     discriminant = 1 + 8 * xn
     if discriminant<0:
         return None # no real sol
     # solve for n
     n = (-1+math.sqrt(discriminant)) / 2
     # return int if n is a whole number
     return int(n) if n.is_integer() else None

def find_n2(xn):
    n = int((math.sqrt(8*xn+1)-1)/2)
    #  Apply one iteration of Newton's method for refinement
    #n = n - (n**2 + n - 2*xn) / (2*n + 1)
    #return int(n) if n.is_interger() else round(n,6)

    if (n * (n+1)) // 2 == xn:
        return n
    else:
        return None
    
def compute():
    filename = "0042_words.txt"
    words = read_words(filename)
    result = 0
    for word in words:
        n = 0
        for letter in word:
            position = alphabet_position(letter)
            n +=position
        if find_n(n):
            result +=1
    return result








if __name__ == "__main__":
    #print(alphabet_position('S'))
    filename = "0042_words.txt"
    #words = read_words(filename)
    #print(find_n(55))
    #print(find_n2(55))
    print(compute())

    print(len([num for num in [sum([ord(letter) - 64 for letter in list(word)]) for word in open(filename, 'r').readline().replace('\"', '').split(',')] if num in [0.5 * n * (n + 1) for n in range(500)]]))
