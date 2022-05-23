#!/usr/bin/python3
def text_indentation(text):
    """adds two integers or floats, casting floats into integers"""

    if type(text) != str:
        raise TypeError("text must be a string")

    new_string = text[:]
    char_replace = {'.':'.\n\n',
                    '?':'?\n\n',
                    ':':':\n\n',
                    ' \n':'\n',
                    '\n ':'\n'}
    
    for key, value in char_replace.items():
        new_string = new_string.replace(key, value)

    print(new_string, end="")
