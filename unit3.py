# question 3.2.5
import string


def read_file(file_name):
    print("__CONTENT_START__")
    file = None

    try:
        file = open(file_name, "r")
        print(file.read())

    except FileNotFoundError:
        print("__NO_SUCH_FILE__")

    finally:
        if file is not None:
            file.close()
        print("__CONTENT_END__")


read_file("notarealfile.txt")


# question 3.3.2
class UnderAgeError(Exception):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f"Error, name: '{self._name}' is under age"

    def get_arg(self):
        return self._name


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAgeError(name)
    except UnderAgeError as e:
        print("under age")
    else:
        print("You should send an invite to " + name)


send_invitation("Ohad", 17)


# question 3.4
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, name, index):
        self._arg = name, index

    def __str__(self):
        return f"username: '{self._arg}' contains illegal character '{self._arg[0][self._arg[1]]}' at index: {self._arg[1]}"

    def get_arg(self):
        return self._arg


class UsernameTooShort(Exception):
    def __init__(self, name):
        self._arg = name

    def __str__(self):
        return f"username: '{self._arg}' is too short"

    def get_arg(self):
        return self._arg


class UsernameTooLong(Exception):
    def __init__(self, name):
        self._arg = name

    def __str__(self):
        return f"username: '{self._arg}' is too long"

    def get_arg(self):
        return self._arg


class PasswordMissingCharacter(Exception):
    def __init__(self, pas, lst):
        self._arg = (pas, lst)

    def __str__(self):
        return f"password: '{self._arg[0]}' missing: (" + ", ".join(self._arg[1]) + ")"

    def get_arg(self):
        return self._arg


class PasswordTooShort(Exception):
    def __init__(self, name):
        self._arg = name

    def __str__(self):
        return f"password: '{self._arg}' is too short"

    def get_arg(self):
        return self._arg


class PasswordTooLong(Exception):
    def __init__(self, name):
        self._arg = name

    def __str__(self):
        return f"password: '{self._arg}' is too long"

    def get_arg(self):
        return self._arg


def check_input(username: str, password: str):
    try:
        # checking valid username
        lst = list(map(lambda c: str.isalpha(c) or str.isnumeric(c) or c in string.punctuation, username))
        if not all(lst):
            failing_index = next((i for i, c in enumerate(lst) if c == False), None)
            raise UsernameContainsIllegalCharacter(username, failing_index)

        if len(username) < 3:
            raise UsernameTooShort(username)

        if len(username) > 16:
            raise UsernameTooLong(username)

        # checking valid password

        lst_checkers = [
        (str.islower, "lowercase"),
        (str.isupper, "uppercase"),
        (str.isalpha, "alphabetic"),
        (str.isdigit, "numeric"),
        (lambda c: c in string.punctuation, "punctuation")]

        missing = set(name for _, name in lst_checkers)

        for ch in password:
            for func, name in lst_checkers:
                if func(ch):
                    missing.discard(name)

        # check if the updated set isn't empty
        if missing.__len__() != 0:
            raise PasswordMissingCharacter(password, list(missing))

        if len(password) < 8:
            raise PasswordTooShort(password)
    except Exception as e:
        print(e.__str__())


check_input("A_1", "abcdefghijklmnop")
check_input("A_1", "ABCDEFGHIJLKMNOP")
check_input("A_1", "ABCDEFGhijklmnop")
check_input("A_1", "4BCD3F6h1jk1mn0p")