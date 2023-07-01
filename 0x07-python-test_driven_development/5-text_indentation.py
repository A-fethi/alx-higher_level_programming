#!/usr/bin/python3
"""Module of "5-test_indentation"."""


def text_indentation(text):
    """
    splits a text into lines along "?", ":", "." followed by 2 new lines.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    index = 0
    for i in text:
        if i in ".?:":
            if text[index + 1] == " ":
                text = text[:index + 1] + text[index + 2:]
        else:
            index += 1
    index = 0
    for i in text:
        if i in ".?:":
            text = text[:index + 1] + '\n\n' + text[index + 1:]
            index += 3
        else:
            index += 1
    print(text, end="")
