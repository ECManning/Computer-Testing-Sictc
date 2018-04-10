# author: Jeremy Temple, Eli Manning
import string
from token_v1 import token, Tokens, tokenenum, keywords
offset = 0
fstrim = None
tokens = Tokens()

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
    global tokens
    with open(filename) as fstrim:
        while True:
            character = scan()
            if not character:
                break
            # comment
            if character in "#":
                while True:
                    character = scan()
                    if character in "#" or character in "":
                        break
            # id or keyword
            elif character in string.ascii_letters:
                word = []
                while True:
                    word.append(character)
                    character = scan()
                    if character not in string.ascii_letters or character in "":
                        offset -= 1
                        break
                joined_word = "".join(word).lower()
                if joined_word in keywords:
                    tokens.append(token(keywords[joined_word], joined_word))
                else:
                    tokens.append(token("id", "".join(word)))
            # Integer constant
            elif character in string.digits:
                num = ""
                while True:
                    num += character
                    character = scan()
                    if character not in "1234567890":
                        offset -= 1
                        break
                tokens.append(token("integer", int(num)))
            # assignment or punctuation
            elif character in ":":
                # assignment
                if scan() in "=":
                    tokens.append(token("assignment", ":="))
                # punctuation
                else:
                    offset -= 1
                    tokens.append(token("punctuation", ":"))
            # punctuation
            elif character in ";().,":
                tokens.append(token("punctuation", character))

            # relational
            elif character in "<>":
                if scan() in "=":
                    tokens.append(token("relational", "{0}=".format(character)))
                else:
                    tokens.append(token("relational", character))
            elif character in "!":
                if scan() in "=":
                    tokens.append(token("relational", "!="))
                else:
                    print('Error: expected "=" at character {0}'.format(offset))
                    exit()
            elif character in "=":
                tokens.append(token("relational", character))

            # arithmetic
            elif character in "+-*/%":
                tokens.append(token("arithmetic", character))
    return tokens
