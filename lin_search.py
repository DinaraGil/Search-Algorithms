from random import sample


def lin_search(number, lst):
    index = -1
    for i in range(len(lst)):
        if number == lst[i]:
            index = i

    if index >= 0:
        return 'Index = ' + str(index)
    else:
        return 'No such value'


if __name__ == "__main__":
    lst = sample(range(-1000, 1000), 1000)

    number = int(input())

    print(lin_search(number, lst))