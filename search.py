import numpy as np


def sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not stop and not found:
        if a_list[pos] == item:
            found = True
        else:
            # if a_list[pos] > item:
            #     stop = True
            pos += 1
    print(pos)
    return found

def binary_search(a_list, item):
    length = len(a_list)
    assert length > 0
    if a_list[length//2] == item:
        return length//2
    if a_list[length//2] < item:
        return length//2  +  1 + binary_search(a_list[length//2 + 1:],item)
    else:
        return binary_search(a_list[0:length//2],item)

def main():
    print(sequential_search([15, 18, 2, 18, 0, 8, 13, 19, 14],14))
    print(binary_search([0, 2, 4, 6, 7, 8, 10], 8))
if __name__ == '__main__':
    main()
