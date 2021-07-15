import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *


class TestParser(unittest.TestCase):
    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.number_token, 51.2)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(51.2))

    def test_individual_operations(self):
        tokens = [
            Token(TokenType.number_token, 27),
            Token(TokenType.minus_token),
            Token(TokenType.number_token, 14)
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(27), NumberNode(14)))

        tokens = [
            Token(TokenType.number_token, 27),
            Token(TokenType.plus_token),
            Token(TokenType.number_token, 14)
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(27), NumberNode(14)))

        tokens = [
            Token(TokenType.number_token, 27),
            Token(TokenType.star_token),
            Token(TokenType.number_token, 14)
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(27), NumberNode(14)))

        tokens = [
            Token(TokenType.number_token, 27),
            Token(TokenType.slash_token),
            Token(TokenType.number_token, 14)
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(27), NumberNode(14)))

    def test_full_expressionZ(self):
        tokens = [
            # 27 + (43 / 36 - 48) * 51
            Token(TokenType.number_token, 27),
            Token(TokenType.plus_token),
            Token(TokenType.left_parentheses_token),
            Token(TokenType.number_token, 48),
            Token(TokenType.minus_token),
            Token(TokenType.number_token, 43),
            Token(TokenType.slash_token),
            Token(TokenType.number_token, 36),
            Token(TokenType.right_parentheses_token),
            Token(TokenType.star_token),
            Token(TokenType.number_token, 51)
        ]

        node = Parser(tokens).parse()

        # 27 + ((48 - 43 / 36) * 51)
        #
        #      +
        #    /  \
        #  27    *
        #      /  \
        #    51    -
        #        /  \
        #      48    /
        #          /  \
        #         43  36

        self.assertEqual(node, AddNode(
                NumberNode(27),
                MultiplyNode(
                    SubtractNode(
                        NumberNode(48),
                        DivideNode(
                            NumberNode(43),
                            NumberNode(36)
                        )
                    ),
                    NumberNode(51)
                )
            )
        )