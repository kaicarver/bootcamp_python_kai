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
    count = 0
    for c in text:
        count = count + 1
    print("NYI", count, text)

if __name__ == "__main__":
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else "Hello, there!"
    text_analyzer(text)
