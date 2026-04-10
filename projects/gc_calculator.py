sequence = input("Enter a DNA sequence: ")
A = sequence.count('A')
T = sequence.count('T')
C = sequence.count('C')
G = sequence.count('G')
sum = (A + T + C + G)
GC_content = f"{((G + C) / sum) * 100:.2f}%"
print(GC_content)