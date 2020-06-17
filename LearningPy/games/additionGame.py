import random
import os

from pip._vendor.distlib.compat import raw_input

randomlist = []
again = 'y'
while again == 'y':
    os.system('clear')
    correct = 0
    wrong = 0
    print("PLAY !!")
    print("")
    for i in range(0, 10):
        a = random.randint(0, 5)
        b = random.randint(0, 5)
        okInput = True
        while okInput:
            try:
                c = input(str(a) + " + " + str(b) + " = ")
                okInput = False
            except:
                print("ERROR !..Please enter valid answer")

        ans = a + b
        if ans == int(c):
            print("OK, CORRECT !!")
            correct = correct + 1
        else:
            print("WRONG!!")
            wrong = wrong + 1

    print("")
    print("SAANVI, YOU ANSWERED !!")
    print("CORRECT -> " + str(correct))
    print("WRONG -> " + str(wrong))
    print("=============")
    print("SCORE : " + str(correct-wrong))
    print("=============")

    redo_input = True

    while redo_input:

        r = raw_input("WANT TO PLAY AGAIN ?? [y/n] : ")

        if r == 'n' or r == 'N':
            again = 'n'
            redo_input = False
            os.system('clear')
            print("----------- BYE BYE !! -----------")
        elif r == 'y' or r == 'Y':
            again = 'y'
            redo_input = False
        else:
            print("!! << Please enter y/n to proceed >> !!")
