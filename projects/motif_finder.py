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
    found_flag = False

    if haystack in text:
        for i in range((len(haystack) - len(needle) + 1)):
            if haystack[i:i + len(needle)] == needle:
                found_flag = True

        if found_flag:
            print("MOTIF Identified.")
        else:
            print("No MOTIF Identified. :(")
            
    else:
        print("No sequence found within DNA.")
    
        

motif_finder()