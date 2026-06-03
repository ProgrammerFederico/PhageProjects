with open("fastaOne.fa", "r") as file:
    text = ""
    for incorrectCharacters in textString:
        incorrectCharacters = incorrectCharacters.replace("\n", "")
        incorrectCharacters = incorrectCharacters.replace(">", "")
        text = incorrectCharacters