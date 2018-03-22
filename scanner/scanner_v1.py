import string
from token_v1 import token
offset = 0
fstrim = None


def next():
    global fstrim
    global offset
    while True:
        fstrim.seek(offset)
        character = fstrim.read
        offset += 1
        if character not in string.whitespace:
            break
        offset -= 1
        return character


def scan():
    global fstrim
    global offset
    while True:
        fstrim.seek(offset)
        character = fstrim.read(1)
        offset += 1
        if character not in string.whitespace or character in "":
            break

    return character


def scanner(filename):
    global fstrim
    global offset
    with open(filename) as fstrim:
        while True:
            character = scan()
            if not character:
                break
            # comment
            if character in "#":
                character = scan()
                if character in "#" or character in "":
                    break
            # word
            elif character in string.ascii_letters:
                word = ""
                while True:
                    word += character
                    character = scan()
                    if character not in string.ascii_letters or character in "":
                        offset -= 1
                        break
                print(word)




scanner("thing.sictc")
