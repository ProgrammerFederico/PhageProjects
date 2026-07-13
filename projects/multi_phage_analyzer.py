def multi_phage_analyzer():
    from fasta_analyzer import fasta_analyzer
    from pathlib import Path

    path_name = input("Greetings Researcher! \nPlease enter the folder path where your FASTA files are located: ")
    folder_path = Path(path_name)
    file_paths = []

    for file in folder_path.iterdir():
        if file.suffix in {".fa", ".fasta"}:
            file_paths.append(file)
            continue

    if len(file_paths) == 0:
        print("Researcher, no FASTA Files have been found. :( ")
    print(file_paths)

    
    # print(fasta_analyzer("/PhageProjects/data", "fastaOne.fa"))

multi_phage_analyzer()