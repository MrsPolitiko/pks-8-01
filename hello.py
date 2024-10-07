import sys

def get_vowels(String):
    return [each for each in String if each in "aeiou"]

def capitalize(String):
    return String.title()

sys.stdout.write(capitalize("hello world\n"))

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)
