from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    number_token = 0
    
    plus_token = 1
    minus_token = 2
    star_token = 3
    slash_token = 4
    
    percent_token = 5
    
    star_star_token = 6
    slash_slash_token = 7
    left_parentheses_token = 8
    right_parentheses_token = 9


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
