# question 4.1.2
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    for word in sentence.split(" "):
        yield words[word]


print(" ".join(list(translate("el gato esta en la casa"))))


# question 4.1.3
def first_prime_over(n):
    while True:
        if is_prime(n):
            yield n
        n += 1


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


gen = first_prime_over(1000000)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())


# question 4.2.2
def parse_ranges(ranges_string: str):
    lst_ranges = ranges_string.split(",")
    for cur_range in lst_ranges:
        low, high = cur_range.split("-")
        for i in range(int(low), int(high) + 1):
            yield i


print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))


# question 4.3.4
def get_fibo():
    first, second = 0, 1
    while True:
        yield first

        # calc next sequence
        temp = first
        first = second
        second += temp

fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))


# question 4.4
def gen_secs():
    return (i for i in range(0, 60))


def gen_minutes():
    return (i for i in range(0, 60))


def gen_hours():
    return (i for i in range(0, 24))


def get_time():
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                yield "%02d:%02d:%02d" % (h, m, s)


def gen_years(start=2025):
    while True:
        yield start
        start += 1


def gen_months():
    return (i for i in range(1, 13))


def gen_days(month, leap_year=True):
    days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if month == 2 and leap_year:
        return (i for i in range(days_in_months[month - 1] + 1))
    return (i for i in range(days_in_months[month - 1]))


def gen_date():
    for y in gen_years():
        for m in gen_months():
            for d in gen_days(m):
                time_gen = get_time()
                for time in time_gen:
                    yield "%02d/%02d/%02d" % (d, m, y) + " " + time

try:
    date_gen = gen_date()
    for i in range(1, 10):
        for k in range(100000):
            next(date_gen)
        print(next(date_gen))

except StopIteration:
    print("Done")