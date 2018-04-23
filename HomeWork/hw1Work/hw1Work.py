#!/usr/bin/env python
import pdb
import string
import operator

class SM:
    def start(self):
        self.state = self.startState
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o
    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]

# Tokenizer class takes in a string, one character at a time
# and returns a list of tokens.  A final space is needed at the end
# of the input string or the final token (stored in self.state) will not
# be returned.

class Tokenizer(SM):
    def __init__(self):
        self.startState = ''

    def getNextValues(self, state, inp):
        if (inp.isalpha() and self.state.isalpha()) or (inp.isdigit() and self.state.isdigit()):
            self.state += inp
            return self.state, self.startState
        elif inp == ' ':
            return self.startState, self.state
        else:
            return inp, self.state


##################################

class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return self.opStr + '(' + \
               str(self.left) + ', ' +\
               str(self.right) + ')'
    __repr__ = __str__

# for all class.eval() methods
# continue to evaluate the left and right sides of the expression
# until a number is returned
class Sum(BinaryOp):
    opStr = 'Sum'

    def eval(self, env):
        return operator.add(self.left.eval(env), self.right.eval(env)) 


class Prod(BinaryOp):
    opStr = 'Prod'

    def eval(self, env):
        return operator.mul(self.left.eval(env), self.right.eval(env))

class Quot(BinaryOp):
    opStr = 'Quot'

    def eval(self, env):
        return operator.div(self.left.eval(env), self.right.eval(env))

class Diff(BinaryOp):
    opStr = 'Diff'

    def eval(self, env):
        return operator.sub(self.left.eval(env), self.right.eval(env))

class Assign(BinaryOp):
    opStr = 'Assign'

    def eval(self, env):
        env[self.left.name] = self.right.eval(env) #left side is always a Variable, right side may be an expression



class Number:
    def __init__(self, val):
        self.value = val
    def __str__(self):
        return 'Num('+str(self.value)+')'
    def eval(self, env):
        return self.value
    __repr__ = __str__

class Variable:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Var('+self.name+')'
    def eval(self, env):
        return env[self.name]
    __repr__ = __str__



# characters that are single-character tokens
seps = ['(', ')', '+', '-', '*', '/', '=']

# Convert strings into a list of tokens (strings)
def tokenize(string):
    newWord = ""  # current word
    prevChar = "" # previous character
    tokens = []   # list of tokens

    for char in string:
        if char in seps:
            if newWord != "":  # if there's a word, add word to tokens first then add char
                tokens.append(newWord)
                newWord = ""
                tokens.append(char)
            else:   # otherwise add char to tokens
                tokens.append(char)
        elif char.isalpha():
            if prevChar.isalpha() or newWord == "": # if char is alphabetical and word is empty or word, add to newWord
                newWord += char
            else:  # if word is 'finished', add to tokens list
                tokens.append(newWord)
                newWord = ""
                newWord += char
        elif char.isdigit():
            if prevChar.isdigit() or newWord == "": # if char is numerical and word is empty or number, add to newWord
                newWord += char
            else:     # if word is 'finished', add to tokens list
                tokens.append(newWord)
                newWord = ""
                newWord += char
        prevChar = char
    
    if newWord != "":    # append any remaining word
        tokens.append(newWord)
    
    return tokens

def tokenize2(inputString):
    tokenizer = Tokenizer()
    tokens = tokenizer.transduce(inputString)
    finalTokens = []
    for item in tokens:
        if item != '':
            finalTokens.append(item)

    return finalTokens

# tests for tokenize2
def testTokenize2():
    print tokenize2('fred ')
    print tokenize2('777 ')
    print tokenize2('777 hi 33 ')
    print tokenize2('**-)( ')
    print tokenize2('(hi*ho) ')
    print tokenize2('fred + george) ')

# token is a string
# returns True if contains only digits
def numberTok(token):
    for char in token:
        if not char in string.digits: return False
    return True

# token is a string
# returns True its first character is a letter
def variableTok(token):
    for char in token:
        if char in string.letters: return True
    return False

# tokens is a list of tokens
# returns a syntax tree:  an instance of {\tt Number}, {\tt Variable},
# or one of the subclasses of {\tt BinaryOp} 
def parse(tokens):
    def parseExp(index):
        # if a token represents a number, make it into a Number instance and return that paried with index+1
        if numberTok(tokens[index]):
            num = Number(float(tokens[index]))
            return (num, index+1)
        # if a token is a variable name, make it a variable instance and return that with index+1
        elif variableTok(tokens[index]):
            var = Variable(str(tokens[index]))
            return (var, index+1)
        else:
            (leftTree, nextIndex1) = parseExp(index+1)
            op = tokens[nextIndex1]
            (rightTree, nextIndex2) = parseExp(nextIndex1+1)
            if op == "+":
                return Sum(leftTree, rightTree), nextIndex2 + 1
            elif op == "-":
                return Diff(leftTree, rightTree), nextIndex2 + 1
            elif op == "*":
                return Prod(leftTree, rightTree), nextIndex2 + 1
            elif op == "/":
                return Quot(leftTree, rightTree), nextIndex2 + 1
            elif op == "=":
                return Assign(leftTree, rightTree), nextIndex2 + 1

    (parsedExp, nextIndex) = parseExp(0)
    return parsedExp

# thing is any Python entity
# returns True if it is a number
def isNum(thing):
    return type(thing) == int or type(thing) == float

# Run calculator interactively
def calc():
    env = {}
    while True:
        e = raw_input('%')            # prints %, returns user input
        print '%', # your expression here
        print '   env =', env

# exprs is a list of strings
# runs calculator on those strings, in sequence, using the same environment
def calcTest(exprs):
    env = {}
    for e in exprs:
        print '%', e                    # e is the experession 
        print parse(tokenize(e)).eval(env) # tokenize then parse the expression, then evaluate the result
        print '   env =', env

# Simple tokenizer tests
'''Answers are:
['fred']
['777']
['777', 'hi', '33']
['*', '*', '-', ')', '(']
['(', 'hi', '*', 'ho', ')']
['(', 'fred', '+', 'george', ')']
['(', 'hi', '*', 'ho', ')']
['(', 'fred', '+', 'george', ')']
'''
def testTokenize():
    print tokenize('fred ')
    print tokenize('777 ')
    print tokenize('777 hi 33 ')
    print tokenize('**-)(')
    print tokenize('( hi * ho )')
    print tokenize('(fred + george)')
    print tokenize('(hi*ho)')
    print tokenize('( fred+george )')

# Simple parsing tests from the handout
'''Answers are:
Var(a)
Num(888.0)
Sum(Var(fred), Var(george))
Quot(Prod(Var(a), Var(b)), Diff(Var(cee), Var(doh)))
Quot(Prod(Var(a), Var(b)), Diff(Var(cee), Var(doh)))
Assign(Var(a), Prod(Num(3.0), Num(5.0)))
'''
def testParse():
    print parse(['a'])
    print parse(['888'])
    print parse(['(', 'fred', '+', 'george', ')'])
    print parse(['(', '(', 'a', '*', 'b', ')', '/', '(', 'cee', '-', 'doh', ')' ,')'])
    print parse(tokenize('((a * b) / (cee - doh))'))
    print parse(tokenize('(a = (3 * 5))'))

####################################################################
# Test cases for EAGER evaluator
####################################################################

def testEval():
    env = {}
    Assign(Variable('a'), Number(5.0)).eval(env)
    print Variable('a').eval(env)
    env['b'] = 2.0
    print Variable('b').eval(env)
    env['c'] = 4.0
    print Variable('c').eval(env)
    print Sum(Variable('a'), Variable('b')).eval(env)
    print Sum(Diff(Variable('a'), Variable('c')), Variable('b')).eval(env)
    Assign(Variable('a'), Sum(Variable('a'), Variable('b'))).eval(env)
    print Variable('a').eval(env)
    print env

# Basic calculator test cases (see handout)
testExprs = ['(2 + 5)',
             '(z = 6)',
             'z',
             '(w = (z + 1))',
             'w'
             ]
#calcTest(testExprs)

####################################################################
# Test cases for LAZY evaluator
####################################################################

# Simple lazy eval test cases from handout
'''Answers are:
Sum(Var(b), Var(c))
Sum(2.0, Var(c))
6.0
'''
def testLazyEval():
    env = {}
    Assign(Variable('a'), Sum(Variable('b'), Variable('c'))).eval(env)
    print Variable('a').eval(env)
    env['b'] = Number(2.0)
    print Variable('a').eval(env)
    env['c'] = Number(4.0)
    print Variable('a').eval(env)

# Lazy partial eval test cases (see handout)
lazyTestExprs = ['(a = (b + c))',
                  '(b = ((d * e) / 2))',
                  'a',
                  '(d = 6)',
                  '(e = 5)',
                  'a',
                  '(c = 9)',
                  'a',
                  '(d = 2)',
                  'a']
# calcTest(lazyTestExprs)

## More test cases (see handout)
partialTestExprs = ['(z = (y + w))',
                    'z',
                    '(y = 2)',
                    'z',
                    '(w = 4)',
                    'z',
                    '(w = 100)',
                    'z']

# calcTest(partialTestExprs)
