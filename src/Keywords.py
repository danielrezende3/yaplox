from typing import Dict
import TokenType

keywords: Dict[str, TokenType.TokenType] = {
    "and": TokenType.TokenType.AND,
    "class": TokenType.TokenType.CLASS,
    "else": TokenType.TokenType.ELSE,
    "false": TokenType.TokenType.FALSE,
    "for": TokenType.TokenType.FOR,
    "fun": TokenType.TokenType.FUN,
    "if": TokenType.TokenType.IF,
    "nil": TokenType.TokenType.NIL,
    "or": TokenType.TokenType.OR,
    "print": TokenType.TokenType.PRINT,
    "return": TokenType.TokenType.RETURN,
    "super": TokenType.TokenType.SUPER,
    "this": TokenType.TokenType.THIS,
    "true": TokenType.TokenType.TRUE,
    "var": TokenType.TokenType.VAR,
    "while": TokenType.TokenType.WHILE,
}
