
import string
from examples.token import Token, TokenEnum, Tokens


def scanner():
    line = input("Please input a string to be tokenized.\n")
    tokens = Tokens()
    failed = False
    skip = 0

    for i in range(len(line)):
        if skip > 0:
            skip -= 1
            continue

        character = line[i]
        token = None

        if character in string.whitespace:
            continue

        if character in ["("]:
            token = Token(TokenEnum.OPEN_PAREN, "(")
        elif character in [")"]:
            token = Token(TokenEnum.CLOSE_PAREN, ")")
        elif character in string.ascii_letters:
            word = [character, ]

            # alpha + (beta + gamma)
            for j in range(1, len(line[i:])):
                lookahead = line[i + j]
                skip += 1

                if lookahead in string.whitespace:
                    continue

                if lookahead not in string.ascii_letters:
                    skip -= 1
                    break

                word.append(lookahead)

            token = Token(TokenEnum.VARIABLE, "".join(word))
        elif character in ["+"]:
            token = Token(TokenEnum.OP, "+")

        if token is not None:
            tokens.append(token)
        else:
            print("Invalid character "
                  "{0} at index {1}".format(repr(character), i))
            failed = True
            break

    if not failed:
        tokens.append(Token(TokenEnum.EOF, "$"))
        return tokens
    else:
        return []
