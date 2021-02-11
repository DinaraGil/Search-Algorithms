from random import sample


def bin_search(number, lst):
    mid = len(lst) // 2
    low = 0
    high = len(lst) - 1

    while lst[mid] != number and low <= high:
        if number > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return "No such value"
    else:
        return "Index = " + str(mid)


if __name__ == "__main__":
    lst = sorted(sample(range(-1000, 1000), 1000))

    number = int(input())

    print(bin_search(number, lst))