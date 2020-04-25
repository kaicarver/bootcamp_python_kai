#!/usr/bin/env python


class Book:
    """A simple example class"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"Book {self.name}"
        """Your code goes here"""
        return txt
