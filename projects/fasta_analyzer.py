def fasta_analyzer(folderName, fileName):
    from gc_calculator import gc_calculator
    from nucleotide_counter import nucleotide_counter
    from pathlib import Path

    file_path = Path(f"../{folderName}") / fileName

    with open(file_path, "r") as file:
        text = ""
        for raw_line in file:
            if raw_line.startswith(">"):
                continue
            raw_line = raw_line.replace("\n", "")
            text += raw_line
        
        count = nucleotide_counter(text)
        print(count)

        gc_percent = gc_calculator(count)
        # print(f"GC content: {gc_percent * 100:.2f}%")
        return count, gc_percent
        


