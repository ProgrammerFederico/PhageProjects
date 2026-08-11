def multi_phage_analyzer():
    from fasta_analyzer import fasta_analyzer
    from pathlib import Path

    path_name = input("Greetings Researcher! \nPlease enter the folder path where your FASTA files are located: ")
    folder_path = Path(path_name)
    file_paths = []
    information_list = []

    for file in folder_path.iterdir():
        if file.suffix in {".fa", ".fasta"}:
            file_paths.append(file)
            
            information_list.append(fasta_analyzer(file))

    # # of phages analyzed, avg gc content, gc range, avg genome size.
    if len(file_paths) == 0:
        print("Researcher, no FASTA Files have been found. :( ")
        return

    total_phages = len(information_list)

    average_gc = (
        sum(sample['gc_percentage'] for sample in information_list) 
        / total_phages
    )
    average_genome_size = (
        sum(sample['genome_length'] for sample in information_list) 
        / total_phages
    )

    min_gc = min(sample['gc_percentage'] for sample in information_list)
    max_gc = max(sample['gc_percentage'] for sample in information_list)

    analysis = (
        f"------------\n"
        f"Total Phages Analyzed: {total_phages}\n"
        f"Average GC Content: {average_gc * 100:.2f}%\n"
        f"Average Genome Size: {average_genome_size:,.0f} bp\n"
        f"GC Range: {min_gc * 100:.2f}% - {max_gc * 100:.2f}%"
    )

    print(analysis)
    return(analysis)

    
# File Path for Testing C:\MyWork\PhageInformation
multi_phage_analyzer()