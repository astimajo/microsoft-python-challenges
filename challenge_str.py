first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.replace('  FIRST challenge         ', '       FIRST challenge')
first_value = first_value.title()


# Second challenge
second_value = second_value.replace('-', " ")
second_value = second_value.lstrip()
second_value = second_value.title()

# Third challenge
third_value = third_value.replace('tH IR D-C HALLE NGE', 'third challenge')
third_value = third_value.title()
third_value = third_value.rjust(30)

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
message = f'''        {fourth_value}
        {fifth_value}
        {sixth_value}
                '''
print(message)

message = '-Angelo          -'

print(f'{message:^30}')