"""
first_string = 'A literal string'
second_string = "A literal string"
print(first_string == second_string)
"""
'''
third_string = 'A single quoted literal string a " double quote'
fourth_string = "A double quoted literal string with a ' single quote"
print(third_string)
print(fourth_string)
'''
'''
fifth_string = 'A single quoted literal string with an \' single quote'
sixth_string = "A double quoted literal string with a \" double quote"
seventh_string = 'A literal string with a \n new line character'
eighth_string = 'A literal string with a \t tab character'

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)
'''
'''
nineth_string = r"A literal string with a \n new line chracter printed raw"
print(nineth_string)
'''
'''
tenth_string = 'A literal string
on more than one line
sometimes known as a verbatim string' #This has 3 quotes removed due to syntax issues

eleventh_string = """Another literal string 
    on more than one line
using double quotes"""

print(tenth_string)
print(eleventh_string)

'''
'''
first = 'Conrad'
second ='Grant'
third ='Bob'

print(first, second)
print(first, second, third)
print(first, second, third, sep='-')
print(first, second, third, sep='-', end='.')
'''
'''
var1 = u'0'
val = var1.isnumeric()
print(val)
'''
'''
message = str.capitalize('first message')
print(message)
message = 'second message'.capitalize()
print(message)
message = 'third message'
print(message.capitalize())
'''
'''
message ='hello world'
print(message.lower())
print(message.upper())

message = message.title()
print(message)
print(message.swapcase())
'''

#message = 'mississippi'
#print(message.count('s')) #I used message instead of location for less confusion

#print(len('how many letters in this string?'))

'''
message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))
'''
'''
message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T'))
'''
'''
message ='     message     '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')
'''
'''
message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)
'''

message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-'))