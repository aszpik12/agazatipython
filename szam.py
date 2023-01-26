import random

def fel1():
    rand = random.randint(1,50)
    print("I/A")
    print("\tA generált szám: {}".format(rand))
    print("I/B")
    if rand%5==0 and rand%3 == 0:
        print("\tA szám öttel és hárommal is osztható!")
    elif rand%5 == 0:
        print("\tA szám öttel osztható!")
    elif rand%3 == 0:
        print("\tA szám hárommal osztható!")