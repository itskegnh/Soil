class Lexer:
    def __init__(self, code):
        self.tokens = []
    
    def tokenize(self, code):
        for line in code.splitlines():
            print(line)

Lexer(open('Examples/helloworld.soil', 'r').read()).tokenize()