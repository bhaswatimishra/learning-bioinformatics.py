rna_seq="AUGCCCAUGGGGAUG"
def find_startcodon(rna_seq) :
    count= []
    for i in range(0,len(rna_seq)-2):
        codon=rna_seq[i:i+3]
        if codon == "AUG" :
            count.append(i+1)
    total = len(count)
    print(f"Total start codon is {total}")
    print(f"positions are {count}")
find_startcodon(rna_seq)
def find_stopcodon(rna_seq) :
    count=[]
    for i in range(0,len(rna_seq)-2) :
        codon = rna_seq[i:i+3]
        if (codon == "UAA") or (codon== "UGA") or (codon == "UAG") :
            count.append(i+1)
    if len(count) == 0 :
        print(f"No stop codon")
    else :
        print(f"total stop codon is {len(count)}")
        print(f"stop codon positions are {count}")
find_stopcodon(rna_seq)
        
        
