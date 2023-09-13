import random

SHUFFLE_DRUMS = False
SHUFFLE_CABLES = False
SELECTED_DRUMS = (2, 1, 0)
SELECTED_REFLECTOR = 0

LETTERS = (
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
    "X",
    "Y", "Z")
DRUM_ASSIGNMENT = ({"A": "E",
                    "B": "K",
                    "C": "M",
                    "D": "F",
                    "E": "L",
                    "F": "G",
                    "G": "D",
                    "H": "Q",
                    "I": "V",
                    "J": "Z",
                    "K": "N",
                    "L": "T",
                    "M": "O",
                    "N": "W",
                    "O": "Y",
                    "P": "H",
                    "Q": "X",
                    "R": "U",
                    "S": "S",
                    "T": "P",
                    "U": "A",
                    "V": "I",
                    "W": "B",
                    "X": "R",
                    "Y": "C",
                    "Z": "J"},
                   {"A": "A",
                    "B": "J",
                    "C": "D",
                    "D": "K",
                    "E": "S",
                    "F": "I",
                    "G": "R",
                    "H": "U",
                    "I": "X",
                    "J": "B",
                    "K": "L",
                    "L": "H",
                    "M": "W",
                    "N": "T",
                    "O": "M",
                    "P": "C",
                    "Q": "Q",
                    "R": "G",
                    "S": "Z",
                    "T": "N",
                    "U": "P",
                    "V": "Y",
                    "W": "F",
                    "X": "V",
                    "Y": "O",
                    "Z": "E"},
                   {"A": "B",
                    "B": "D",
                    "C": "F",
                    "D": "H",
                    "E": "J",
                    "F": "L",
                    "G": "C",
                    "H": "P",
                    "I": "R",
                    "J": "T",
                    "K": "X",
                    "L": "V",
                    "M": "Z",
                    "N": "N",
                    "O": "Y",
                    "P": "E",
                    "Q": "I",
                    "R": "W",
                    "S": "G",
                    "T": "A",
                    "U": "K",
                    "V": "M",
                    "W": "U",
                    "X": "S",
                    "Y": "Q",
                    "Z": "O"},
                   {"A": "E",
                    "B": "S",
                    "C": "O",
                    "D": "V",
                    "E": "P",
                    "F": "Z",
                    "G": "J",
                    "H": "A",
                    "I": "Y",
                    "J": "Q",
                    "K": "U",
                    "L": "I",
                    "M": "R",
                    "N": "H",
                    "O": "X",
                    "P": "L",
                    "Q": "N",
                    "R": "F",
                    "S": "T",
                    "T": "G",
                    "U": "K",
                    "V": "D",
                    "W": "C",
                    "X": "M",
                    "Y": "W",
                    "Z": "B"},
                   {"A": "V",
                    "B": "Z",
                    "C": "B",
                    "D": "R",
                    "E": "G",
                    "F": "I",
                    "G": "T",
                    "H": "Y",
                    "I": "U",
                    "J": "P",
                    "K": "S",
                    "L": "D",
                    "M": "N",
                    "N": "H",
                    "O": "L",
                    "P": "X",
                    "Q": "A",
                    "R": "W",
                    "S": "M",
                    "T": "J",
                    "U": "Q",
                    "V": "O",
                    "W": "F",
                    "X": "E",
                    "Y": "C",
                    "Z": "K"})
REFLECTOR_ASSIGNMENT = ({"A": "E",
                         "B": "J",
                         "C": "M",
                         "D": "Z",
                         "E": "A",
                         "F": "L",
                         "G": "Y",
                         "H": "X",
                         "I": "V",
                         "J": "B",
                         "K": "W",
                         "L": "F",
                         "M": "C",
                         "N": "R",
                         "O": "Q",
                         "P": "U",
                         "Q": "O",
                         "R": "N",
                         "S": "T",
                         "T": "S",
                         "U": "P",
                         "V": "I",
                         "W": "K",
                         "X": "H",
                         "Y": "G",
                         "Z": "D"},
                        {"A": "Y",
                         "B": "R",
                         "C": "U",
                         "D": "H",
                         "E": "Q",
                         "F": "S",
                         "G": "L",
                         "H": "D",
                         "I": "P",
                         "J": "X",
                         "K": "N",
                         "L": "G",
                         "M": "O",
                         "N": "K",
                         "O": "M",
                         "P": "I",
                         "Q": "E",
                         "R": "B",
                         "S": "F",
                         "T": "Z",
                         "U": "C",
                         "V": "W",
                         "W": "V",
                         "X": "J",
                         "Y": "A",
                         "Z": "T"},
                        {"A": "F",
                         "B": "V",
                         "C": "P",
                         "D": "J",
                         "E": "I",
                         "F": "A",
                         "G": "O",
                         "H": "Y",
                         "I": "E",
                         "J": "D",
                         "K": "R",
                         "L": "Z",
                         "M": "X",
                         "N": "W",
                         "O": "G",
                         "P": "C",
                         "Q": "T",
                         "R": "K",
                         "S": "U",
                         "T": "Q",
                         "U": "S",
                         "V": "B",
                         "W": "N",
                         "X": "M",
                         "Y": "H",
                         "Z": "L"})

DRUMS = []
REFLECTOR = REFLECTOR_ASSIGNMENT[SELECTED_REFLECTOR].copy()
CABLES = {}


def drum_logic(input, direction):
    output = ""
    cache = ""

    if direction == "forward":
        for index, drum in enumerate(reversed(DRUMS)):
            if index == 0:
                cache = drum[input]
            else:
                cache = drum[cache]
        output = cache
    elif direction == "backward":
        for index, drum in enumerate(DRUMS):
            if index == 0:
                cache = list(drum.keys())[list(drum.values()).index(input)]
            else:
                cache = list(drum.keys())[list(drum.values()).index(cache)]
        output = cache
    return output


def reflector_logic(input):
    output = ""
    cache = REFLECTOR[input]
    output = cache
    return output


def cable_logic(input, direction):
    output = ""
    if direction == "forward":
        output = CABLES[input]
    elif direction == "backward":
        output = list(CABLES.keys())[list(CABLES.values()).index(input)]
    return output


def rotate_drums(count):
    for i in range(count):
        values = list(DRUMS[2].values())
        values = values[1:] + values[:1]
        for index, key in enumerate(DRUMS[2].keys()):
            DRUMS[2][key] = values[index]

        if list(DRUMS[2].values())[0] == list(DRUM_ASSIGNMENT[SELECTED_DRUMS[2]].values())[0]:
            values = list(DRUMS[1].values())
            values = values[1:] + values[:1]
            for index, key in enumerate(DRUMS[1].keys()):
                DRUMS[1][key] = values[index]

            if list(DRUMS[1].values())[0] == list(DRUM_ASSIGNMENT[SELECTED_DRUMS[1]].values())[0]:
                values = list(DRUMS[0].values())
                values = values[1:] + values[:1]
                for index, key in enumerate(DRUMS[0].keys()):
                    DRUMS[0][key] = values[index]


def prepare():
    for i in range(len(SELECTED_DRUMS)):
        DRUMS.append(DRUM_ASSIGNMENT[SELECTED_DRUMS[i]].copy())
    if SHUFFLE_DRUMS:
        for i in range(len(SELECTED_DRUMS)):
            rotate_drums(random.randint(0, 17567))

    REFLECTOR = REFLECTOR_ASSIGNMENT[SELECTED_REFLECTOR].copy()

    for i in range(len(LETTERS)):
        CABLES[LETTERS[i]] = LETTERS[i]
    if SHUFFLE_CABLES:
        used_letters = []
        for _ in CABLES.keys():
            random_letter_1 = LETTERS[random.randint(0, 25)]
            random_letter_2 = LETTERS[random.randint(0, 25)]
            while random_letter_1 - 1 in used_letters and random_letter_2 in used_letters:
                random_letter_1 = LETTERS[random.randint(0, 25)]
                random_letter_2 = LETTERS[random.randint(0, 25)]
            CABLES[random_letter_1] = random_letter_2
            CABLES[random_letter_2] = random_letter_1
            used_letters.append(random_letter_1)
            used_letters.append(random_letter_2)

    print("Drums:", DRUMS)
    print("Reflector:", REFLECTOR)
    print("Cables", CABLES)
    print()


def encrypt(string):
    output = ""
    for char in string:
        if char.upper() not in LETTERS:
            output += char
        else:
            output += cable_logic(
                drum_logic(reflector_logic(drum_logic(cable_logic(char.upper(), "forward"), "forward")), "backward"),
                "backward")
            rotate_drums(1)
    return output


if __name__ == "__main__":
    prepare()
    while True:
        print("Encrypted String: " + encrypt(input("String: ")))
        print()
