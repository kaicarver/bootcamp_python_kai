#!/usr/bin/env python


def text_analyzer(text='', *args):
    """
    Count the number of characters in a text:
    total, uppercase, lowercase, punctuation, and spaces.

    Args:
        text: the text to be analyzed.
    Returns:
        Nothing. Prints info to stdout.
    Raises:
        Nothing.
"""
    if len(args) > 0:
        print('ERROR')
        return
    (count, upcase, locase, punc, spac) = (0, 0, 0, 0, 0)
    if len(text) == 0:
        text = input("What is the text to analyse?\n>> ")
    for c in text:
        count += 1
        if c.isupper():
            upcase += 1
        elif c.islower():
            locase += 1
        elif c.isspace():
            spac += 1
        elif not c.isdigit():
            punc += 1
    print("""The text contains {} characters:
- {} upper letters
- {} lower letters
- {} punctuation marks
- {} spaces""".format(count, upcase, locase, punc, spac))


if __name__ == "__main__":
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else "Hello, there!"
    print(text + ':')
    text_analyzer(text)
    print('no args:')
    text_analyzer()
    print('too many args:')
    text_analyzer(text, 'bla')
