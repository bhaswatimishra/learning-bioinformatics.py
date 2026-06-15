sample= {}
sequence=[]
header = None
with open ("sample.faasta") as f :
   for line in f :
       if line.startswith(">") :
           if header is not None :
               sample[header]["sequence"]= "".join(sequence)
           header = line[1:].strip()
           sample[header]={}
           sequence =[]
       else :
           sequence.append(line.strip())
   if header is not None :
      sample[header]["sequence"]= "".join(sequence)
def length(sample) :
    for header in sample :
        length = len(sample[header]["sequence"])
        sample[header]["length"] = length
length(sample)
def GC_content(sample) :
    for header in sample :
        g_count = sample[header]["sequence"].count("G")
        c_count = sample[header]["sequence"].count("C")
        gc_perc= ((g_count+c_count)/(sample[header]["length"]))*100
        sample[header]["GC_content"] = gc_perc
GC_content(sample)
def reverse_complement (sample) :
    complement={ "A" : "T",
                "G" : "C",
                "C" : "G",
                "T" :"A"}
    for header in sample :
        sequence=[]
        for letter in sample[header]["sequence"] :
            sequence.append(complement[letter])
        sample[header]["reverse_complement"] = "".join(sequence)
reverse_complement(sample)
def rna(sample) :
    for header in sample :
        rna_seq= sample[header]["sequence"].replace("T","U")
        sample[header]["RNA"] = "".join(rna_seq)
rna(sample)
def translation(sample) :
    codon_table ={
            'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'Stop', 'UAG':'Stop',
    'UGC':'C', 'UGU':'C', 'UGA':'Stop', 'UGG':'W',
        }
    for header in sample :
        protein_morethanone=[]
        for i in range (0,len(sample[header]["RNA"])-2) :
            codon_initiator = sample[header]["RNA"][i:i+3]
            if codon_initiator == "AUG" :
                protein_seq = []
                for j in range (i,len(sample[header]["RNA"]),3) :
                    codon = sample[header]["RNA"][j:j+3]
                    if codon in codon_table :
                        if codon_table[codon] == "Stop" :
                           break
                        elif len(codon)!= 3 :
                           break
                        else :
                          protein_seq.append(codon_table[codon]) 
                protein_morethanone.append("".join(protein_seq))
        sample[header]["protein"] = protein_morethanone
translation(sample)
for header in sample :
        print(f"{header}")
        print(f"sequence : 5'-{sample[header]["sequence"]}-3'")
        print(f"length : {sample[header]["length"]}")
        print(f"GC_Content : {sample[header]["GC_content"]}")
        print(f"reverse complement : 5'-{sample[header]["reverse_complement"][::-1]}-3'")
        print(f"RNA : 5'-{sample[header]["RNA"]}-3'")
        print(f"protein : {sample[header]["protein"]}")
