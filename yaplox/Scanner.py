from Token import Token
from TokenType import TokenType
from typing import List
import Lox
import Keywords


class Scanner:
    def __init__(self, source: str) -> None:
        self.tokens: List[Token] = []
        self.source: str = source
        self.start: int = 0
        self.current: int = 0
        self.line: int = 1

    def scan_tokens(self) -> List[Token]:
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def advance(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def add_token(self, token_type: TokenType, literal=None) -> None:
        text = self.source[self.start : self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def match(self, expected: str) -> bool:
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self) -> str:
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def string(self) -> None:
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        if self.is_at_end():
            #! The tmp is really needed?
            tmp = Lox.Lox()
            tmp.error(self.line, "Unterminated string.")
            return

        self.advance()

        value = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenType.STRING, value)

    def is_digit(self, c: str) -> bool:
        return c >= "0" and c <= "9"

    def peek_next(self) -> str:
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def number(self) -> None:
        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == "." and self.is_digit(self.peek_next()):
            self.advance()

            while self.is_digit(self.peek()):
                self.advance()

        self.add_token(TokenType.NUMBER, float(self.source[self.start : self.current]))

    def is_aplha_numeric(self, c: str) -> bool:
        return self.is_alpha(c) or self.is_digit(c)

    def identifier(self) -> None:
        while self.is_aplha_numeric(self.peek()):
            self.advance()

        text: str = self.source[self.start : self.current]
        token_type: TokenType = Keywords.keywords.get(text, TokenType.IDENTIFIER)

        if token_type is None:
            token_type = TokenType.IDENTIFIER

        self.add_token(TokenType.IDENTIFIER)

    def is_alpha(self, c: str) -> bool:
        return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or c == "_"

    def scan_token(self):
        c: str = self.advance()
        while c != TokenType.EOF:
            if c == "(":
                self.add_token(TokenType.LEFT_PAREN)
            elif c == "(":
                self.add_token(TokenType.LEFT_PAREN)
            elif c == ")":
                self.add_token(TokenType.RIGHT_PAREN)
            elif c == "{":
                self.add_token(TokenType.LEFT_BRACE)
            elif c == "}":
                self.add_token(TokenType.RIGHT_BRACE)
            elif c == ",":
                self.add_token(TokenType.COMMA)
            elif c == ".":
                self.add_token(TokenType.DOT)
            elif c == "-":
                self.add_token(TokenType.MINUS)
            elif c == "+":
                self.add_token(TokenType.PLUS)
            elif c == ";":
                self.add_token(TokenType.SEMICOLON)
            elif c == "*":
                self.add_token(TokenType.STAR)
            elif c == "!":
                self.add_token(
                    TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG
                )
            elif c == "=":
                self.add_token(
                    TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL
                )
            elif c == "<":
                self.add_token(
                    TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS
                )
            elif c == ">":
                self.add_token(
                    TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER
                )
            elif c == "/":
                if self.match("/"):
                    while self.peek() != "\n" and not self.is_at_end():
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            elif c in [" ", "\r", "\t"]:
                pass
            elif c == "\n":
                self.line += 1
            elif c == '"':
                self.string()
            elif self.is_digit(c):
                self.number()
            elif self.is_alpha(c):
                self.identifier()
            else:
                #! The tmp is really needed?
                tmp = Lox.Lox()
                tmp.error(self.line, "Unexpected character.")
            break
