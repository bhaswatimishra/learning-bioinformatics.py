sequence = "ATCGAATTCGGATCCAAAGAATTCTTTGGATCC"
def restriction_sites(sequence) :
    restriction = {}
    key = None
    restriction_sites = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT"
    }
    for key in restriction_sites :
        key_positions =[]
        for i in range (0,len(sequence)-5) :
           site = sequence[i:i+6]
           if site == restriction_sites[key] :
               key_positions.append(i+1)
        restriction[key] = {}
        restriction[key]["positions"] = key_positions
        restriction[key]["count"] = len(restriction[key]["positions"])
    for key  in restriction :
        print(f"{key}")
        print(f"positions : {restriction[key]["positions"]}")
        print(f"count : {restriction[key]["count"]}")
restriction_sites(sequence)
