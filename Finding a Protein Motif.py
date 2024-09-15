#Given: At most 15 UniProt Protein Database access IDs.
#Return: For each protein possessing the N-glycosylation motif, 
#output its given access ID followed by a list of locations in the protein string where the motif can be found.

################################################################################################
#Load txt.file containing protein IDs from Uniprot
with open("D:/BO/DA-08/.ipynb_checkpoints/Rosalind_practice/rosalind_mprt.txt", "r") as file:
    ids = [i.strip() for i in file.readlines()]

#Access sequence through IDs
base_url = "http://www.uniprot.org/uniprot/"
id_dict = {}
import requests
def getsequences(ids):
    for id in ids:
        id_run = id[0:6] #Some given IDs include IDs and the protein name
        seq_url = f"{base_url}{id_run}.fasta"
        response = requests.get(seq_url)

        if response.status_code == 200:
            for i in range(0, len(response.text)):
                if response.text[i] == "\n":
                    sequence = response.text[i+1:]
                    break
            sequence = "".join(sequence.split("\n"))
            id_dict[id] = sequence
        else:
            print(f"Error: {id}")
    return id_dict
getsequences(ids)

#Access sequence to find whether motif is found
def findmotif(id_dict):
    for id, seq in id_dict.items():
        indices = []
        for i in range(len(seq) - 3):
            if (seq[i] == "N" and
                seq[i+1] != "P" and
                (seq[i+2] == "S" or seq[i+2] == "T") and
                seq[i+3] != "P"):
                indices.append(i + 1)  # +1 for 1-based indexing
        indices_seq = " ".join(str(index) for index in indices)
        print(id)
        if indices:
            print(indices_seq)           
findmotif(id_dict)

