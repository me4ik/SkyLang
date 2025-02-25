from ply import lex
from tokens import tokens, keywords


class SkyLexer:
    def __init__(self):
        self.lexer = lex.lex(module=self)

    # Токены:

    def t_NUMBER(t):
        r'\d+'  # регулярное выражение для чисел
        t.value = int(t.value)  # преобразуем строку в число
        return t

    def t_STRING(self, t):
        r'[^"]*'
        t.value = t.value[1:-1]
        return t

    def t_GREQ(self, t):
        r'>='
        t.type = 'GREQ'
        return t

    def t_LSEQ(self, t):
        r'<='
        t.type = 'LSEQ'
        return t

    def t_EQEQ(self, t):
        r'=='
        t.type = 'EQEQ'
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = keywords.get(t.value, 'ID')
        return t

    def t_error(self, t):
        print(f"Неизвестный символ '{t.value[0]}' на позиции {t.lexpos}")
        t.lexer.skip(1)

    def tokenize(self, text):
        self.lexer.input(text)
        return list(self.lexer)

