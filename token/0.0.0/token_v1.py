# author: Jeremy Temple, Eli Manning
import enum


class Tokens(object):
    def __init__(self):
        self._data = []

    def __iter__(self):
        return iter(self._data)

    def append(self, token):
        self._data.append(token)

    @property
    def lookahead(self):
        return self._data[0]

    def consume(self):
        self._data.pop(0)

    def __str__(self):
        w = []
        for i in self._data:
            w.append("Kind: {0}\nValue: {1}\n\n".format(i._kind, i._value))
        return "".join(w)
class tokenenum(enum.Enum):
    BEGIN = enum.auto()
    DO = enum.auto()
    END = enum.auto()
    FALSE = enum.auto()
    HALT = enum.auto()
    IF = enum.auto()
    PRINT = enum.auto()
    PROGRAM = enum.auto()
    THEN = enum.auto()
    TRUE = enum.auto()
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

keywords = {"begin" : tokenenum.BEGIN,
           "do" : tokenenum.DO,
           "end" : tokenenum.END,
           "false" : tokenenum.FALSE,
           "halt" : tokenenum.HALT,
           "if" : tokenenum.IF,
            "print" : tokenenum.PRINT,
            "program" : tokenenum.PROGRAM,
            "then" : tokenenum.THEN,
            "true" : tokenenum.TRUE,
            "var" : tokenenum.VAR,
            "while" : tokenenum.WHILE}
