def fasta_analyzer(file_path):
    from gc_calculator import gc_calculator
    from nucleotide_counter import nucleotide_counter

    with open(file_path, "r") as file:
        text = ""
        for raw_line in file:
            if raw_line.startswith(">"):
                continue
            raw_line = raw_line.replace("\n", "")
            text += raw_line

        phage_information = {
            "file_name": file_path.name,
        }

        count = nucleotide_counter(text)

        gc_percent = gc_calculator(count)

        phage_information["nucleotide_count"] = count
        phage_information["gc_percentage"] = gc_percent
        phage_information["genome_length"] = len(text)
        # print(f"GC content: {gc_percent * 100:.2f}%")
        return phage_information
        
