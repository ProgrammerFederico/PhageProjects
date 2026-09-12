def motif_finder():
    file_path = input("Greetings Researcher! \nPlease enter the file path where your .FASTA / .fa file is located: ")
    
    with open(file_path, "r") as file:
        text = ""
        for raw_line in file:
            if raw_line.startswith(">"):
                continue
            raw_line = raw_line.replace("\n", "")
            text += raw_line

    haystack = input("Greetings Researcher, please enter the sequence of DNA you would like analyzed: ")
    needle = input("Please enter the MOTIF: ")

    if haystack in text:
        if needle in haystack:
            print("MOTIF identified.")
        else:
            print('No MOTIF identified. :(')
    else:
        print("No sequence found within DNA.")
    
        

motif_finder()