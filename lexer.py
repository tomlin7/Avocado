from tokens import Token, TokenType

whitespace = " \n\t"
digits = "0123456789"


class Lexer:
    def __init__(self, code):
        self.source = code + '\n'
        self.cur_char = None
        self.cur_pos = -1
        self.advance()

    def advance(self, pos=1):
        self.cur_pos += pos
        try:
            self.cur_char = self.source[self.cur_pos]
        except:
            self.cur_char = None

    def peek(self):
        try:
            return self.source[self.cur_pos + 1]
        except:
            return None
    
    # def advance(self):
    #     try:
    #         self.cur_char = next(self.text)
    #     except StopIteration:
    #         self.cur_char = None

    def generate_tokens(self):
        while self.cur_char is not None:
            if self.cur_char in whitespace:
                self.advance()
            elif self.cur_char == "." or self.cur_char.isdigit():
                yield self.generate_number()
            elif self.cur_char == "+":
                self.advance()
                yield Token(TokenType.plus_token)
            elif self.cur_char == "-":
                self.advance()
                yield Token(TokenType.minus_token)
            elif self.cur_char == "%":
                self.advance()
                yield Token(TokenType.percent_token)
            elif self.cur_char == "*":
                if self.peek() == "*":
                    self.advance(2)
                    yield Token(TokenType.star_star_token)
                else:
                    self.advance()
                    yield Token(TokenType.star_token)
            elif self.cur_char == "/":
                if self.peek() == "/":
                    self.advance(2)
                    yield Token(TokenType.slash_slash_token)
                else:
                    self.advance()
                    yield Token(TokenType.slash_token)
            elif self.cur_char == "(":
                self.advance()
                yield Token(TokenType.left_parentheses_token)
            elif self.cur_char == ")":
                self.advance()
                yield Token(TokenType.right_parentheses_token)
            elif self.cur_char == "%":
                self.advance()
                yield Token(TokenType.percent_token)
            else:
                raise Exception(f"Illegal character '{self.cur_char}'")

    def generate_number(self):
        decimal_point_count = 0
        number_str = self.cur_char
        self.advance()

        while self.cur_char is not None and (self.cur_char == "." or self.cur_char.isdigit()):
            if self.cur_char == ".":
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.cur_char
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
