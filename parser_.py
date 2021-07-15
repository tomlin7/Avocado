from tokens import TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.current_token = None
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):
        raise Exception("Invalid Syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token is None:
            return

        result = self.expr()

        if self.current_token is not None:
            self.raise_error()

        return result

    def expr(self):
        result = self.term()

        while self.current_token is not None and self.current_token.type in (TokenType.plus_token, TokenType.minus_token):
            if self.current_token.type == TokenType.plus_token:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.minus_token:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.current_token is not None and self.current_token.type in (TokenType.star_token, TokenType.slash_token):
            if self.current_token.type == TokenType.star_token:
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif self.current_token.type == TokenType.slash_token:
                self.advance()
                result = DivideNode(result, self.factor())

        return result

    def factor(self):
        token = self.current_token

        if token.type == TokenType.left_parentheses_token:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.right_parentheses_token:
                self.raise_error()

            self.advance()
            return result

        elif token.type == TokenType.number_token:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.plus_token:
            self.advance()
            return PlusNode(self.factor())
        elif token.type == TokenType.minus_token:
            self.advance()
            return MinusNode(self.factor())

        self.raise_error()
