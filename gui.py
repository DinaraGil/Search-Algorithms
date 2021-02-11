from tkinter import *
from random import sample
from lin_search import lin_search
from bin_search import bin_search
import time

lst = sorted(sample(range(-100000, 100000), 100000))

root = Tk()

Label(text="Number:").grid(row=0, column=0, sticky=W, pady=10, padx=10)
n_entry = Entry()

n_entry.grid(row=0, column=1, columnspan=3, sticky=W + E, padx=10)

Label(text="Result:").grid(row=1, column=0, sticky=W, pady=10, padx=10)
r_entry = Entry()

r_entry.grid(row=1, column=1, columnspan=3, sticky=W + E, padx=10)


def lin_time(number):
    start_time = time.clock()
    result = lin_search(number, lst)
    return time.clock() - start_time


def bin_time(number):
    start_time = time.clock()
    result = bin_search(number, lst)
    return time.clock() - start_time


def search():
    try:
        number = int(n_entry.get())

        result = bin_search(number, lst)

        r_entry.delete(0, END)
        r_entry.insert(0, result)

        t1_entry.delete(0, END)
        t1_entry.insert(0, lin_time(number))

        t2_entry.delete(0, END)
        t2_entry.insert(0, bin_time(number))
    except ValueError:
        return


but = Button(text="Find", command=search)

but.grid(row=0, column=4, pady=10, padx=10)

Label(text="Linear Search").grid(row=2, column=1, sticky=W, padx=10, pady=10)

Label(text="Binary Search").grid(row=2, column=3, sticky=E, padx=10, pady=10)

Label(text="Time:").grid(row=3, column=0, sticky=W, pady=10, padx=10)
t1_entry = Entry()

t1_entry.grid(row=3, column=1, sticky=W + E, padx=10)

Label(text="Time:").grid(row=3, column=3, sticky=W, pady=10, padx=10)
t2_entry = Entry()

t2_entry.grid(row=3, column=3, sticky=W + E, padx=10)


root.mainloop()
