import unittest
from tokens import Token, TokenType
from lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_empty(self):
        tokens = list(Lexer("").generate_tokens())
        self.assertEqual(tokens, [])

    def test_empty(self):
        tokens = list(Lexer("  \t\n  \t\t\n\n").generate_tokens())
        self.assertEqual(tokens, [])

    def test_numbers(self):
        tokens = list(Lexer("123 123.456 123. .456 .").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.number_token, 123.000),
            Token(TokenType.number_token, 123.456),
            Token(TokenType.number_token, 123.000),
            Token(TokenType.number_token, 000.456),
            Token(TokenType.number_token, 000.000)
        ])

    def test_operators(self):
        tokens = list(Lexer("+-*/").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.plus_token),
            Token(TokenType.minus_token),
            Token(TokenType.star_token),
            Token(TokenType.slash_token)
        ])

    def test_parentheses(self):
        tokens = list(Lexer("()").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.left_parentheses_token),
            Token(TokenType.right_parentheses_token)
        ])

    def test_all(self):
        tokens = list(Lexer("27 + (43 / 36 - 48) * 51").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.number_token, 27),
            Token(TokenType.plus_token),
            Token(TokenType.left_parentheses_token),
            Token(TokenType.number_token, 43),
            Token(TokenType.slash_token),
            Token(TokenType.number_token, 36),
            Token(TokenType.minus_token),
            Token(TokenType.number_token, 48),
            Token(TokenType.right_parentheses_token),
            Token(TokenType.star_token),
            Token(TokenType.number_token, 51)
        ])