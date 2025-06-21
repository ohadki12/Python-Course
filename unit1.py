import functools


# question 1.1.2
def double_letter(my_str):
    return "".join(list(map(lambda c: c * 2, my_str)))


print(double_letter("hello world"))


# question 1.1.3
def four_dividers(num: int) -> list:
    return list(filter(lambda x: x % 4 == 0, range(1, num)))


print(four_dividers(9))


# question 1.1.4
def sum_of_digits(num: int) -> int:
    return functools.reduce(lambda a, b: a + b, get_digits(num))


def get_digits(num: int) -> list:
    if num == 0: return []
    return [num % 10] + get_digits(num // 10)


print(sum_of_digits(1234))


# question 1.3.1
def intersection(list_1, list_2):
    return list(set([list_1[i] for i in range(0, len(list_1)) if list_1[i] in list_2]))


print(intersection([1, 2, 3, 4], [8, 3, 9]))
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))


# question 1.3.2
def is_prime(number):
    return number > 1 and all([number % i != 0 for i in range(2,int(number * 0.5))])


print(is_prime(42))
print(is_prime(43))


# question 1.3.3
def is_funny(string: str):
    return all([(ch == 'h' or ch == 'a') for ch in string])


print(is_funny("hahahahahaha"))
print(is_funny("hahahahgahaha"))


# question 1.3.4
def solve_password(string: str):
    return "".join(map(lambda ch: chr(ord(ch) + 2), string))


print(solve_password("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))


# question 1.5
def tr1_5():
    names = []
    with open("names.txt", "r") as file:
        names = file.read().split("\n")
        # 1 -> longest name
        print(sorted(names, key=lambda x:len(x), reverse=True)[0])

        # 2 -> total length of names
        print(functools.reduce(lambda a, b: a + b, [len(name) for name in names]))

        # 3 -> all shortest names
        shrt = functools.reduce(lambda a, b: min(a, b), [len(name) for name in names])
        print(list(filter(lambda name: len(name) == shrt, names)))

        # 4 -> write names length
    with open("name_length.txt", "w") as file2:
        file2.write("\n".join([str(len(name)) for name in names]))

        



tr1_5()