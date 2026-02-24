# Chapter 3
# coding lesson-word count
from sys import argv
# this is how we get command line arguments
print(argv)

if len(argv) < 2:
    print("Please provide a filename.")
else:
    file = open(argv[1])
    print(file)
    lines = file.read()
    print(type(lines))
    lines = lines.split("\n")  # create a new line
    print(lines)  # a list of strings
    word_count = 0
    letter_count = 0

    for line in lines:
        words = line.split(" ")
        word_count += len(words)
        letter_count += len(line)
    line_count = len(lines) - 1
    print(f"The line count is {line_count}")
    print(f"The word count is {word_count}")
    print(f"The letter count is {letter_count}")
