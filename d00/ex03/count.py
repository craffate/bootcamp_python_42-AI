import sys
import re


def text_analyzer(text=None):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
    if text is None:
        text = input("What is the text to analyse?\n")

    punc = re.findall(r"[!\"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", text)
    lower = re.findall(r"[a-z]", text)
    upper = re.findall(r"[A-Z]", text)
    spaces = re.findall(r"[ ]", text)
    print("The text contains", len(text), "characters:")
    print("-", len(upper), "upper letters")
    print("-", len(lower), "lower letters")
    print("-", len(punc), "punctuations characters")
    print("-", len(spaces), "spaces")

print(text_analyzer.__doc__)
