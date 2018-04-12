# author: Jeremy Temple, Eli Manning, Hayden Walters
import enum
import operator


class Tokens(object):
    def __init__(self):
        self._data = []

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def append(self, token):
        self._data.append(token)

    @property
    def lookahead(self):
        return self._data[0]

    def consume(self):
        self._data.pop(0)

    def peek(self):
        return self._data[0]

    def __str__(self):
        w = []
        for i in self._data:
            w.append("Kind: {0}\nValue: {1}\n\n".format(i._kind, i._value))
        return "".join(w)


class tokenenum(enum.Enum):
    # Integer constant
    INT = enum.auto()

    # arithmetic operators
    OPERATOR = enum.auto()

    # Assignment operators
    ASSIGN = enum.auto()

    # Punctuation
    COLON = enum.auto()
    SEMI = enum.auto()
    OPEN = enum.auto()
    CLOSE = enum.auto()
    DOT = enum.auto()
    COMMA = enum.auto()

    # ID (variable/Program Names)
    ID = enum.auto()

    # keywords
    BEGIN = enum.auto()
    DO = enum.auto()
    END = enum.auto()
    HALT = enum.auto()
    IF = enum.auto()
    PRINT = enum.auto()
    PROGRAM = enum.auto()
    THEN = enum.auto()
    BOOL = enum.auto()
    VAR = enum.auto()
    WHILE = enum.auto()



class token(object):
    def __init__(self, kind, value):
        self._kind = kind
        self._value = value

    def __str__(self):
        return "{0} {1}".format(self.kind, self.value)

    @property
    def kind(self):
        return self._kind

    @property
    def value(self):
        return self._value


arithmetic = {"+" : tokenenum.OPERATOR,
              "-" : tokenenum.OPERATOR,
              "*" : tokenenum.OPERATOR,
              "/" : tokenenum.OPERATOR,
              "%" : tokenenum.OPERATOR}

relational = {"=" : tokenenum.OPERATOR,
              "!=" : tokenenum.OPERATOR,
              "<" : tokenenum.OPERATOR,
              "<=" : tokenenum.OPERATOR,
              ">" : tokenenum.OPERATOR,
              ">=" : tokenenum.OPERATOR}

punctuation = {":" : tokenenum.COLON,
               ";" : tokenenum.SEMI,
               "(" : tokenenum.OPEN,
               ")" : tokenenum.CLOSE,
               "." : tokenenum.DOT,
               "," : tokenenum.COMMA}

keywords = {"begin" : tokenenum.BEGIN,
           "do" : tokenenum.DO,
           "end" : tokenenum.END,
           "false" : tokenenum.BOOL,
           "halt" : tokenenum.HALT,
           "if" : tokenenum.IF,
           "print" : tokenenum.PRINT,
           "program" : tokenenum.PROGRAM,
           "then" : tokenenum.THEN,
           "true" : tokenenum.BOOL,
           "var" : tokenenum.VAR,
           "while" : tokenenum.WHILE}

non_enum_math = {"+" : operator.add,
                 "-" : operator.sub,
                 "*" : operator.mul,
                 "/" : operator.floordiv,
                 "%" : operator.mod}
