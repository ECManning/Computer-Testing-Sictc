from token_v2 import tokenenum, arithmetic, relational
tokens = None
token = None

def set_globals(t):
    global tokens
    global token
    tokens = t
    token = t.peek()



def header():
    return match(tokenenum.PROGRAM) and match(tokenenum.COLON) and match(tokenenum.ID) and match(tokenenum.SEMI) and declarations()


def declarations():
    return match(tokenenum.VAR) and match(tokenenum.COLON) and id_list() and match(tokenenum.SEMI)


def id_list():
    return match(tokenenum.ID) and id_list2()


def id_list2():
    global token
    if token._kind is tokenenum.COMMA:
        match(tokenenum.COMMA)
        return id_list()
    else:
        return True


def body():
    return match(tokenenum.BEGIN) and match(tokenenum.COLON) and statement_list() and match(tokenenum.HALT) and match(tokenenum.DOT)



def statement_list():
    global token
    if statement():
        return statement_list()
    else:
        return True



def statement():
    global token
    if token._kind is tokenenum.ID:
        return match(tokenenum.ID) and match(tokenenum.ASSIGN) and expression() and match(tokenenum.SEMI)
    elif token._kind is tokenenum.PRINT:
        return match(tokenenum.PRINT) and match(tokenenum.COLON) and match(tokenenum.ID) and match(tokenenum.SEMI)
    elif token._kind is tokenenum.IF:
        return match(tokenenum.IF) and match(tokenenum.COLON) and expression() and match(tokenenum.COMMA) and match(tokenenum.THEN) and match(tokenenum.COLON) and statement_list() and match(tokenenum.END) and match(tokenenum.DOT)
    elif token._kind is tokenenum.WHILE:
        return match(tokenenum.WHILE) and match(tokenenum.COLON) and expression() and match(tokenenum.COMMA) and match(tokenenum.DO) and match(tokenenum.COLON) and statement_list() and match(tokenenum.END) and match(tokenenum.DOT)
    else:
        return False



def expression():
    global token
    if token._kind is tokenenum.ID:
        return match(tokenenum.ID)
    elif token._kind is tokenenum.INT:
        return match(tokenenum.INT)
    elif token._kind is tokenenum.BOOL:
        return match(tokenenum.BOOL)
    elif token._kind is tokenenum.OPEN:
        return match(tokenenum.OPEN) and expression() and match(tokenenum.OPERATOR) and expression() and match(tokenenum.CLOSE)
    else:
        print("Error: expected expression before {0}".format(token._kind))
        return False
def match(expected):
    global tokens
    global token
    if token._kind is expected:
        tokens.consume()
        if len(tokens) != 0:
            token = tokens.peek()
        return True
    else:
        print('Error expected "{0}" got "{1}"'.format(expected, token._kind))
        print(tokens)
        return False

def start():
    return header() and body()
