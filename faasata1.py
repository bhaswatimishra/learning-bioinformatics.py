with open ( "sample.faasta", "w") as f :
    f.write(">Human\nATCG\nATCG\n>Mouse\nGGGG\nTTTT\n>Dog\nAAAA\nCCCC")
sample={}
sequences=[]
header = None
with open("sample.faasta","r") as f :
    for line in f :
        if line.startswith(">") :
            if header is not None :
                sample[header]= "".join(sequences)
            header= line[1:].strip()
            sequences=[]
        else :
            sequences.append(line.strip())
if header is not None :
    sample[header] = "".join(sequences)
def GC_content(sample) :
  GC_file={}
  for key in sample :
    amount_G = sample[key].count("G")
    amount_C = sample[key].count("C")
    total=len(sample[key])
    GC_content= ((amount_G+amount_C)/total)*100
    GC_file[key]= GC_content
  for key in sample :
    print(f"{key} : {GC_file[key]}") 
GC_content(sample)
def reverse(sample) :
    reverse={}
    complement = { "A" : "T",
                "G" : "C",
                "C" : "G",
                "T" :"A"}
    for key in sample :
        reverse_seq=[]
        for letter in sample[key] :
            reverse_seq.append(complement[letter])
        rev = "".join(reverse_seq)
        reverse[key] = rev
        print(f"{key}\n")
        print(f"original sequence : 5'-{sample[key]}-3'")
        print(f"reversed sequence : 5'-{reverse[key][::-1]}-3'")
reverse(sample)