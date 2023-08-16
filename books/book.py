filename = 'foobar.txt'
basename, __, ext = filename.rpartition('.')
print (basename,ext,__)

four_lists = [[]] * 4
four_lists[0].append("Ni")
print (four_lists)
four_lists = [[] for __ in range(4)]
four_lists[0].append("Ni")
print(four_lists)

##
import threading
some_lock = threading.Lock()
with some_lock:
     # Make Earth Mark One, run it for 10 million years ...
    print(
        "Look at me: I design coastlines.\n"
        "I got an award for Norway."
        )
    print (type(some_lock))

from contextlib import closing
with closing(open("outfile.txt", "w")) as output:
    output.write("Well, he's...he's, ah...probably pining for the fjords.")

def append_to(element, to=[]):
    to.append(element)
    return to
my_list = append_to(12)
print(my_list)
my_other_list = append_to(42)
print(my_other_list)

def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to
my_list = append_to(12)
print(my_list)
my_other_list = append_to(42)
print(my_other_list)

def create_multipliers():
    return [lambda x : i * x for i in range(5)]
for multiplier in create_multipliers():
    print(multiplier(2), end=" ... ")
    print()
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]
for multiplier in create_multipliers():
    print(multiplier(2), end=" ... ")
    print()

