import itertools
import time
import os

user_input = input("Enter the 9 letters here: ")
user_input = str.lower(user_input)
text = open("ukenglish.txt", 'r').readlines()
in_list = list(user_input)
text_set = set(text)
f = open('outWords.txt', 'w')

def one():
    for i in range(0, 8):
        in2 = user_input[i] + '\n'
        if in2 in text_set:
            f.write("1  " + in2)

def two():
    list2 = list(itertools.permutations(in_list, 2))
    for i2 in list2:
        in2 = ''.join(i2)
        in2 += "\n"
        if in2 in text_set:
            f.write("2  " + in2)

def three():
    list2 = list(itertools.permutations(in_list, 3))
    for i2 in list2:
        in2 = ''.join(i2)
        in2 += "\n"
        if in2 in text_set:
            f.write("3  " + in2)

def four():
    list2 = list(itertools.permutations(in_list, 4))
    for i2 in list2:
        in2 = ''.join(i2)
        in2 += "\n"
        if in2 in text_set:
            f.write("4  " + in2)

def five():
    list2 = list(itertools.permutations(in_list, 5))
    for i2 in list2:
        in2 = ''.join(i2)
        in2 += "\n"
        if in2 in text_set:
            f.write("5  " + in2)

def six():
    list2 = list(itertools.permutations(in_list, 6))
    for i2 in list2:
        in2 = ''.join(i2)
        in2 += "\n"
        if in2 in text_set:
            f.write("6  " + in2)

def seven():
    list2 = list(itertools.permutations(in_list, 7))
    for i2 in list2:
        in2 = ''.join(i2)
        in2 += "\n"
        if in2 in text_set:
            f.write("7  " + in2)

def eight():
    list2 = list(itertools.permutations(in_list, 8))
    for i2 in list2:
        in2 = ''.join(i2)
        in2 += "\n"
        if in2 in text_set:
            f.write("8  " + in2)

def nine():
    list2 = list(itertools.permutations(in_list, 9))
    for i2 in list2:
        in2 = ''.join(i2)
        in2 += "\n"
        if in2 in text_set:
            f.write("9  " + in2)
    time.sleep(2)
    f.close()
    outfile_cleanup()

def outfile_cleanup():
    # Get the highest word and print it out
    outputs = open('outWords.txt', 'r').readlines()
    output_list = list(outputs)
    print(output_list[len(output_list) - 1])

    # Make the output file unique
    output_set = set(outputs)
    f = open('outWords.txt', 'w')
    
    # Sort the output file
    final_list = list()
    for i in range(1, 10):
        for value in output_set:
            if int(value[0]) == i:
                f.write(value)


def parent():
    wpid1 = os.fork()
    if wpid1 == 0:
        one()
    else:
        wpid2 = os.fork()
        if wpid2 == 0:
            two()
        else:
            wpid3 = os.fork()
            if wpid3 == 0:
                three()
            else:
                wpid4 = os.fork()
                if wpid4 == 0:
                    four()
                else:
                    wpid5 = os.fork()
                    if wpid5 == 0:
                        five()
                    else:
                        wpid6 = os.fork()
                        if wpid6 == 0:
                            six()
                        else:
                            wpid7 = os.fork()
                            if wpid7 == 0:
                                seven()
                            else:
                                wpid8 = os.fork()
                                if wpid8 == 0:
                                    eight()
                                else:
                                    nine()

parent()