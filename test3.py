'''Get 2 user inputs: 1-number, 2-letter -> print number amount of letters in one line: e.g. user inputs are 3 and 'a', output should be 'aaa' '''

import sys
arg = sys.argv
a = int(input('Enter number: '))
b = input('Enter letter: ')
print(a*b)
