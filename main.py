from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

print("Welcome to Avocado-0.0.1-beta"
      "\n-----------------------------\n")
while True:
    try:
        text = input("🥑 ")

        lexer = Lexer(text)
        tokens = lexer.generate_tokens()

        parser = Parser(tokens)
        tree = parser.parse()

        if not tree:
            continue

        interpreter = Interpreter()
        value = interpreter.visit(tree)

        print(tree)
        print(value)
    except Exception as e:
        print(e)
