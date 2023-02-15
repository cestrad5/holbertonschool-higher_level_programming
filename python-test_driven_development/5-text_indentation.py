#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after these characters: ., ? and :
Prototype: def text_indentation(text):
There should be no space at the beginning or at the end of each printed line.
"""


def text_indentation(text):
    """
    text must be a string, otherwise raise a TypeError exception.
    """

    is_whitespace = 0

    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip(' ')

    for _letters in text:
        if is_whitespace == 0:
            if _letters == " ":
                pass
            else:
                is_whitespace = 1
        if is_whitespace == 1:
            if _letters == '.' or _letters == '?' or _letters == ':':
                print(_letters)
                print()
                is_whitespace = 0
            else:
                print(_letters, end="")
