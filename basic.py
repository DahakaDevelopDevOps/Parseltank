#Types that we are going to have TYPES, defined as constants
#CONSTANTS

from distutils.log import error


DIGITS  = '0123456789'

#Errors

class Error:
    def __init__ (self, error_name, details):
        self.error_name = error_name
        self.details = details
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result
class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illefal Character', details)

#TOKENS
 
TT_INT        = 'TT_INT'
TT_FLOAT      = 'FLOAT'
TT_PLUS       = 'PLUS'  
TT_MINUS      = 'MINUS'
TT_MUL        = 'MUL' 
TT_LBRACKET   = 'LBRACKET'
TT_RBRACKET   = 'RBRACKET'
TT_DIV        = 'DIV'

class Token:
    def __init__(self, type_, value = None): #initialisation method
      self.type = type_
      self.value = value

    def __repr__(self):  #representational method
       if self.value: return f'{self.type}:{self.value}' #if value is given prints a value and a type
       return f'{self.type}'#if value is't given prints a type

#LEXER

class Lexer: #initial method (based)
    def __init__(self, text): #text that will be processing
       self.text  = text 
       self.pos  = -1 #tracking of current position and character
       self.current_char = None
    
    def advance(self): #advance method that drives to the next character in the text 
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None #increasing a position of text until the text will end, than tags it as None

    def make_tokens(self):
        tokens =[]

        while self.current_char != None: #for token that is taged as None
            if self.current_char in '\t': #if meets space
                self.advance() #jump to next charracter
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())#we have to find a way how to define is number integer or not
            elif self.current.char =='+':#if meets plus symbol
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current.char =='-':#if meets minus symbol
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current.char =='/':#if meets divide symbol
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current.char =='*':#if meets mul symbol
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current.char =='(':#if meets mul symbol
                tokens.append(Token(TT_LBRACKET))
                self.advance()
            elif self.current.char ==')':#if meets mul symbol
                tokens.append(Token(TT_RBRACKET))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'")


            return tokens, None    

        def make_number(self):
            num_str = '' #to keep track of number in the string
            dot_count = 0 #dot tracking if number contsins a dot it means that it is as float type

            while self.current_char != None and self.current_char in DIGITS + '.':
                if self.current_char == '.':
                    if dot_count == 1 : break #we can't have two dots in a single number
                    dot_count += 1
                    num_str += '.'
                else: #if it's not a dash 
                    num_str += self.current_char #adding string to current meaning  
                self.advance()
                    
        if self.dot_count == 0:
            return Token(TT_INT, int(self.num_str)) #transforming string into int
        else:
            return Token(TT_FLOAT, float(self.num_str)) #transforming string into float   

#RUN

def run(text): #function which is going to take text and run it 
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    return tokens, error
#have to be upgraded with new steps in the future