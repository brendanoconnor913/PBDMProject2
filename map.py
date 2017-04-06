#!/usr/bin/python

import sys, ast

# Function to strip all non alphabetical characters
def cleanWord(word):
    return word.lower().strip("1234567890-=+_)(*&^%$#@!`~.,<>/?'\"\\[]{};: |")

for line in sys.stdin:
    # skip if line empty
    if line == "":
        continue

    try:
        # Get the text of the tweet
        newline = ast.literal_eval(line)["text"]
        newline = newline.strip()
        words = newline.split()

        # Get all of the words w/ no symbols and output them with a count of 1
        for word in words:
            cword = cleanWord(word)
            if cword != "":
                print '%s\t%s' % (cword, 1)
    except:
        continue
