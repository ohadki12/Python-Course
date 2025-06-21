HANGMAN_ASCII_ART = """Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
"""
MAX_TRIES = 6
SECRET_WORD = ""

#   print(f"{HANGMAN_ASCII_ART}\n{MAX_TRIES}")

stagesLst = ["""    x-------x""", """    x-------x
    |
    |
    |
    |
    |""", """    x-------x
    |       |
    |       0
    |
    |
    |""", """    x-------x
    |       |
    |       0
    |       |
    |
    |""", """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""]


def is_valid_input(word: str, old_letters_guessed: list) -> bool:
    #  making sure function has word_lst attribute

    # checking initial tests
    if len(word) != 1 and not word.isalpha():
        #   print("E3")
        return False
    if len(word) != 1:
        #   print("E1")
        return False
    if not word.isalpha():
        #   print("E2")
        return False

    ch = chr(ord(word) | 0x20)

    # checking if character exists in list
    if ch not in old_letters_guessed:
        return True

    return False


def print_old_letters_guessed(secret_word, old_letters_guessed) -> None:
    print("    ", end="")
    for ch in secret_word:
        if ch in old_letters_guessed:
            print(ch, end="")
        else:
            print("_", end="")
    print("\n")


def print_hangman(num_of_tries):
    #   prints the ascii art of the Hangman for the corresponding tries

    # checking valid input
    if num_of_tries < 1 or num_of_tries > len(stagesLst):
        raise Exception("Error")
    print(stagesLst[num_of_tries - 1])


def create_file() -> None:
    file_path = "words.txt"
    words = [
        "apple", "banana", "computer", "python", "hangman",
        "keyboard", "monitor", "notebook", "elephant", "giraffe",
        "penguin", "island", "volcano", "mountain", "galaxy",
        "puzzle", "mystery", "language", "programming", "challenge",
        "umbrella", "zebra", "dolphin", "rocket", "satellite",
        "adventure", "treasure", "diamond", "forest", "castle"
    ]

    with open(file_path, "w") as file:
        file.write(" ".join(words))


def choose_word(file_path, index) -> tuple[int, str]:
    words_count: int = 30
    words = []

    with open(file_path, "r") as file:
        words = file.read().split(" ")

    return words_count, words[index % words_count]


def check_win(secret_word: str, words: list) -> bool:
    # checking if win

    for ch in secret_word:
        if ch.lower() not in words:
            return False
    return True


def game_loop() -> None:
    print(HANGMAN_ASCII_ART)
    # game loop
    num = int(input("    please choose a number: "))
    num_of_tires: int = 6
    chosen_words = []

    SECRET_WORD = choose_word("words.txt", num)[1]

    while num_of_tires > 0:

        #  print(num_of_tires, "tries left")
        print_hangman(7 - num_of_tires)

        chosen_ch = input("    choose an alphabetic char: ")
        while not is_valid_input(chosen_ch, chosen_words):
            print("    invalid char, please try again")
            chosen_ch = input("    choose an alphabetic char: ")

        chosen_words.append(chr(ord(chosen_ch) | 0x20))

        print_old_letters_guessed(SECRET_WORD, chosen_words)

        if check_win(SECRET_WORD, chosen_words):
            print("   you won!")
            exit(1)

        if chosen_ch not in SECRET_WORD:
            num_of_tires -= 1
    print("    you lost, the word was:", SECRET_WORD)


game_loop()

