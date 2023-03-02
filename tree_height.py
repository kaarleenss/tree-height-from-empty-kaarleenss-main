# python3

import sys
import threading
import numpy as np


def compute_height(n, parent):

    heights = np.zeros(n, dtype=int)

    for i in range(n):
        if np.where(parent == i)[0].size == 0:
            heights[i] = 1

    for i in range(n - 1, -1, -1):
        max_height = 0
        for child in np.where(parent == i)[0]:
            zari = heights[child]
            max_height = max(max_height, zari)

        heights[i] = max_height + 1

    
    return np.max(heights)



def main():
    # implement input form keyboard and from files
    text = input()
    if text[0] == "I":
        n = int(input())
        element = input()
        parent = element.split(" ")
        parent = np.asarray(parent, dtype=int)
    elif text[0] == "F":
        ievade = input()
        if "a" not in ievade:
            cels = "C:\datuStrukturas\\tree-height-from-empty-kaarleenss-main\\test\\" + ievade
            with open(cels) as file:
                text = file.readlines()
            n = int(text[0].replace('\n', ''))
            parent = text[1].replace('\n','').split(" ")
            parent = np.asarray(parent, dtype=int)
        else:
            print("Neatļauts faila nosaukums")
    print(compute_height(n, parent))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


if __name__ == "__main__":
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
    # print(numpy.array([1,2,3]))
