
# Basic Translator
"""
Simple Translator vowels to g character
vowels -> g
------------
dog -> dgg
cat -> cgt
"""

# Solution 1: using in_buit functions

def translate(phrase):

    for letter in phrase:
        if letter.lower() in "aeiou":          # important feature
            if letter.isupper():
                phrase = phrase.replace(letter, "G")
            else:
                phrase = phrase.replace(letter, "g")
        else:
            phrase = phrase.replace(letter, letter)
    return phrase

print(translate("hi THERE are you ok"))

# Solution 2:

def translate2(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":          # important feature
            """
            we can also say: if letter.lower() in "aeiou":
            """
            if letter.isupper():
                 translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate2(input("Enter a phrase: ")))