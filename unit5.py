import functools

import winsound
import itertools

# question 5.1.2
freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }


def get_notes():
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    for tup in notes.split("-"):
        yield tup.split(",")


# playing little jonathan
for note, time in get_notes():
    winsound.Beep(freqs[note], int(time))


# question 5.2.2
try:
    numbers = iter(range(1, 101))
    for i in numbers:
        next(numbers)
        next(numbers)
        print(i)
except StopIteration:
    print("Done")


# question 5.3
class MusicNotes(object):
    def __init__(self):
        self._notes = {
            "La" : [55, 110, 220, 440, 880],
            "Si" : [61.74, 123.48, 246.96, 493.92, 987.84],
            "Do" : [65.41, 130.82, 261.64, 523.28, 1046.56],
            "Re" : [73.42, 146.84, 293.68, 587.36, 1174.72],
            "Mi" : [82.41, 164.82, 329.64, 659.28, 1318.56],
            "Fa" : [87.31, 174.62, 349.24, 698.48, 1396.96],
            "Sol" : [98, 196, 392, 784, 1568]

        }
        self._cnote = "La"
        self._coctiveindex = 0
    def __iter__(self):
        return self

    def __next__(self):
        note_freq = self._notes[self._cnote][self._coctiveindex]

        notes_Lst = list(self._notes.keys())
        next_note = ""
        if notes_Lst.index(self._cnote) != len(notes_Lst) - 1:
            next_note = notes_Lst[notes_Lst.index(self._cnote) + 1]
        else:
            if self._coctiveindex == len(self._notes["La"]) -1:
                raise StopIteration
            next_note = notes_Lst[0]
            self._coctiveindex += 1

        self._cnote = next_note
        return note_freq


for note in MusicNotes():
    print(note)


# question 5.4
class IDIterator(object):
    def __init__(self, id):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        self._id += 1
        while not self.check_id_valid(self._id):
            if self._id == 999999999:
                raise StopIteration
            self._id += 1
        return self._id

    def get_gen(self):
        self._id += 1
        while True:
            if self.check_id_valid(self._id):
                yield self._id
            self._id += 1
    @staticmethod
    def check_id_valid(id_number):
        # stage 1
        id_lst = list(map(int, str(id_number)))
        # print(id_lst)
        # stage 2
        for i, digit in enumerate(id_lst):
            id_lst[i] = id_lst[i] * ((i % 2 != 0) + 1)
        # print(id_lst)
        # stage 3
        for i, val in enumerate(id_lst):
            if val > 9:
                id_lst[i] = functools.reduce(lambda a, b: a + b, map(int, str(val)))
        # print(id_lst)
        return sum(id_lst) % 10 == 0

#print(IDIterator.check_id_valid(287654321))
try:
    start_id = int(input("Enter ID: "))
    kind = input("Generator or Iterator? (gen/it)? ")
    if kind == "it":
        id_iter = IDIterator(start_id)
        for i in range(10):
            print(f"\n{next(id_iter)}")
    else:
        id_gen = IDIterator(start_id).get_gen()
        for i in range(10):
            print(f"\n{next(id_gen)}")
except ValueError:
    exit(0)