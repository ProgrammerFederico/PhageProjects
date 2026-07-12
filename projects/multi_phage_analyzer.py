def multi_phage_analyzer():
    from fasta_analyzer import fasta_analyzer
    from pathlib import Path

    path_name = input("Greetings Researcher! \nPlease enter the folder path where your FASTA files are located: ")
    folder_path = Path(path_name)
    text_list = []

    for file in folder_path.iterdir():
        for file_name in path_name:
            if file_name.endswith(".fa") or file_name.endswith(".fasta"):
                text_list.append("file_name")
                continue

    if file_name.count == 0:
        print("Researcher, no FASTA Files have been found. :( ")
    print(file_name)
    # print(fasta_analyzer("/PhageProjects/data", "fastaOne.fa"))

multi_phage_analyzer()