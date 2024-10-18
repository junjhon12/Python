class Token:
    """A class to represent a token."""
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

class Lexer:
    """A lexer to tokenize the input string."""
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalid character")

    def advance(self):
        """Advance the 'pos' pointer and set the current character."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """Skip whitespace characters."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a multidigit integer from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token('INTEGER', int(result))

    def get_next_token(self):
        """Lexical analyzer (also known as a lexer or scanner)."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return self.integer()
            if self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')
            if self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')
            if self.current_char == '*':
                self.advance()
                return Token('MUL', '*')
            if self.current_char == '/':
                self.advance()
                return Token('DIV', '/')
            if self.current_char == '(':
                self.advance()
                return Token('LPAREN', '(')
            if self.current_char == ')':
                self.advance()
                return Token('RPAREN', ')')
            self.error()
        return Token('EOF', None)

class Parser:
    """A parser to parse the tokens and build an expression tree."""
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        """Consume the current token if it matches the expected type."""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """Parse a factor: INTEGER | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type == 'INTEGER':
            self.eat('INTEGER')
            return token.value
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            result = self.expr()
            self.eat('RPAREN')
            return result

    def term(self):
        """Parse a term: factor ((MUL | DIV) factor)*"""
        result = self.factor()
        while self.current_token.type in ('MUL', 'DIV'):
            token = self.current_token
            if token.type == 'MUL':
                self.eat('MUL')
                result *= self.factor()
            elif token.type == 'DIV':
                self.eat('DIV')
                result /= self.factor()
        return result

    def expr(self):
        """Parse an expression: term ((PLUS | MINUS) term)*"""
        result = self.term()
        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
                result += self.term()
            elif token.type == 'MINUS':
                self.eat('MINUS')
                result -= self.term()
        return result

class Interpreter:
    """An interpreter that uses the lexer and parser to evaluate expressions."""
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.parser = Parser(self.lexer)

    def interpret(self):
        return self.parser.expr()

    def evaluate_postfix(self, expression):
        """Evaluate a postfix expression."""
        stack = []
        tokens = expression.split()
        
        for token in tokens:
            if token.isdigit():  # Check if the token is an operand
                stack.append(int(token))
            else:  # The token is an operator
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(left / right)
                else:
                    raise Exception(f"Unknown operator: {token}")
        
        return stack[0] if stack else None

# Example usage:
if __name__ == "__main__":
    while True:
        try:
            mode = input("Enter mode (infix/postfix or 'exit' to quit): ").lower()
            if mode == 'exit':
                break
            text = input("Enter an expression: ")
            
            interpreter = Interpreter(text)
            if mode == 'infix':
                result = interpreter.interpret()
                print("Result:", result)
            elif mode == 'postfix':
                result = interpreter.evaluate_postfix(text)
                print("Result:", result)
            else:
                print("Invalid mode. Use 'infix' or 'postfix'.")
        except Exception as e:
            print("Error:", e)
