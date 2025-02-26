text = "This is an exmple of a large text file that contains common mispelling errors. The intention is to test the spel checker for various types of misspelt words. Some of the erors are unintentional, while others are placed deliberately. We also want to test sentense structure and grammer mistakes. This text is repeated to create a sufficiently large file."

output = text * 1000

with open("generated_1000.txt", "w") as file:
    file.write(output)
print("Text has been written to generated_10.txt")