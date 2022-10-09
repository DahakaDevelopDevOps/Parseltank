#Tokens, used for adding description for base types

#Types that we are going to have TYPES, defined as constants

TT_INT        = 'TT_INT'
TT_FLOAT      = 'FLOAT'
TT_PLUS       = 'PLUS'  
TT_MINUS      = 'MINUS'
TT_MUL        = 'MUL' 
TT_LBRACKET   = 'LBRACKET'
TT_RBRACKET   = 'RBRACKET'   

class Token:
    def __init__(self, type_, value): #initialisation method
      self.type = type_
      self.value = value

    def __repr__(self):  #representational method
       if self.value: return f'{self.type}:{self.value}' #if value is given prints a value and a type
       return f'{self.type}'#if value is't given prints a type

