
sample={}
sequence=[]
header= None
with open ("sample.faasta", "r") as f :
    for line in f :
      if line.startswith(">") :
        if header is not None :
            sample[header] = "".join(sequence)
        header = line[1:].strip()
        sequence = []
      else :
        sequence.append(line.strip())
    if header is not None :
        sample[header] = "".join(sequence)
def transcription(sample) :
    sample_transcription= {}
    for key in sample :
        transcription=[]
        for letter in sample[key] :
            if letter == "T" :
                transcription.append("U")
            else :
                transcription.append(letter)
        sample_transcription[key] = "".join(transcription)
    for key in sample_transcription :
        print(f"{key} : {sample_transcription[key]}")
transcription(sample)
def translation(sample) :
    sample_transcription= {}
    for key in sample :
        transcription=[]
        for letter in sample[key] :
            if letter == "T" :
                transcription.append("U")
            else :
                transcription.append(letter)
        sample_transcription[key] = "".join(transcription)
    codon_table = {
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
    protein = {}
    for key in sample_transcription :
        protein_seq =[]
        for i in range (0,len(sample_transcription[key]),3):
            codon = sample_transcription[key][i:i+3]
            if len(codon) != 3 :
                break
            elif codon_table[codon]== "Stop" :
                break
            else :
                protein_seq.append(codon_table[codon])

        protein[key] = "".join(protein_seq)
    for key in protein :
        print(f"{key} : {protein[key]}")
translation(sample)