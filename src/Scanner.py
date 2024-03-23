from Token import Token
from TokenType import TokenType
from typing import List


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

    def scan_token(self):
        c: str = self.advance()
        while c != TokenType.EOF:
            if c == "(":
                self.add_token(TokenType.LEFT_PAREN)
