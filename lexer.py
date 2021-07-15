from tokens import Token, TokenType

whitespace = " \n\t"
digits = "0123456789"


class Lexer:
    def __init__(self, text):
        self.current_char = None
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in whitespace:
                self.advance()
            elif self.current_char == "." or self.current_char in digits:
                yield self.generate_number()
            elif self.current_char == "+":
                self.advance()
                yield Token(TokenType.plus_token)
            elif self.current_char == "-":
                self.advance()
                yield Token(TokenType.minus_token)
            elif self.current_char == "*":
                self.advance()
                yield Token(TokenType.star_token)
            elif self.current_char == "/":
                self.advance()
                yield Token(TokenType.slash_token)
            elif self.current_char == "(":
                self.advance()
                yield Token(TokenType.left_parentheses_token)
            elif self.current_char == ")":
                self.advance()
                yield Token(TokenType.right_parentheses_token)
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char == "." or self.current_char in digits):
            if self.current_char == ".":
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith("."):
            number_str = '0' + number_str
        if number_str.endswith("."):
            number_str += '0'

        return Token(TokenType.number_token, float(number_str))


# 1 + 2 * 3
#
#    +
#   / \
#  a   *
#     / \
#    b   c

# (1 + 2) * 3
#
#      *
#     / \
#    +   c
#   / \
#  a   b
