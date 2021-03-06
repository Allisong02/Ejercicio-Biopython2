from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq 
import os

# Archivo de la carpeta en escritorio, se debe de cambiar a la dirección del nuevo archivo .gbk o .fasta a leer
filename =  "/mnt/c/Users/world/OneDrive/Escritorio/Allison/Ejercicio-Biopython/data/m_cold.fasta" 

def summarize_contents(filename):
	lista = []
	lista = os.path.split(filename)
	cadena = " "
	cadena = ("\nfile: "+ lista[1] + "\npath: " + lista[0])
	File_Extension = []
	File_Extension = os.path.splitext(filename)
	if(File_Extension[1]==".gbk"):
		type_file="genbank"
	else:
		type_file="fasta"
		pass
	records = list(SeqIO.parse(filename, type_file))
	cadena += ("\nnum_records: " + str(len(records)))
	cadena += ("\nrecord(s): ")
	for seq_record in SeqIO.parse(filename, type_file):
		cadena += ("\n- id: " + str(seq_record.id))
		cadena += ("\nname: " + seq_record.name)
		cadena += ("\ndescription: " + str(seq_record.description))
	return cadena
if __name__=="__main__":
	resultado = summarize_contents(filename)
	print(resultado)

#Comienzo de la función concatenate_and_get_reverse_complement
seq1 = Seq("GTCAGCATA")
seq2 = Seq("GACTCATCA") 
def concatenate_and_get_reverse_complement(seq1, seq2):
    seqcon = seq1 + seq2 
    seqrevcom = seqcon.reverse_complement() 
    return seqrevcom
    print (seqrevcom)
concatenate_and_get_reverse_complement(seq1, seq2)

#Comienzo de la función print_protein_and_stop_codon_using_standard_table 
cadenaDNA = "CTGGTGGGTAAACATATCTGAG"
def print_protein_and_stop_codon_using_standard_table(cadenaDNA): 
    seqDNA = Seq(cadenaDNA)
    diccionario = {}
    mRNA = seqDNA.transcribe()
    diccionario ['mRNA'] = mRNA 
    for i in range(len(seqDNA)):
        if((seqDNA[i*3:i*3+3] == 'ATG') or (seqDNA[i*3:i*3+3] == 'TTG') or (seqDNA[i*3:i*3+3] == 'CTG')):
            proteins = seqDNA[i*3:].translate(to_stop = True)
            diccionario['Proteins'] = proteins

            for j in range(len(seqDNA)): 
                if((seqDNA[j*3:j*3+3] == 'TAG') or (seqDNA[j*3:j*3+3] == 'TAA') or (seqDNA[j*3:j*3+3] == 'TGA')):
                    diccionario['Stop codon'] = seqDNA[j*3:j*3+3]
                    break
        
        if(i+1 == len(seqDNA)): 
            break 
    return diccionario 
resultado = print_protein_and_stop_codon_using_standard_table(cadenaDNA)
print(resultado)

#Comienzo de la función print_protein_and_stop_codon_using_mitochondrial_yeast_table 
cadenaDNA = "ATGCGCGAGAGCGATAGCTAG"
def print_protein_and_stop_codon_using_mitochondrial_yeast_table(cadenaDNA): 
    seqDNA = Seq(cadenaDNA)
    diccionario = {}
    mRNA = seqDNA.transcribe()
    diccionario ['mRNA'] = mRNA 
    for i in range(len(seqDNA)):
        if((seqDNA[i*3:i*3+3] == 'ATG') or (seqDNA[i*3:i*3+3] == 'GTG') or (seqDNA[i*3:i*3+3] == 'ATA')):
            proteins = seqDNA[i*3:].translate(table = 3, to_stop = True)
            diccionario['Proteins'] = proteins

            for j in range(len(seqDNA)): 
                if((seqDNA[j*3:j*3+3] == 'TAG') or (seqDNA[j*3:j*3+3] == 'TAA')):
                    diccionario['Stop codon'] = seqDNA[j*3:j*3+3]
                    break
        
        if(i+1 == len(seqDNA)): 
            break 
    return diccionario 
resultado = print_protein_and_stop_codon_using_mitochondrial_yeast_table(cadenaDNA)
print(resultado)

#Comienzo de la función extract_sequences para Gen Bank y Fasta.  
filename = "/mnt/c/Users/world/OneDrive/Escritorio/Allison/Ejercicio-Biopython/data/sequences.fasta"
salida = "genbank"
tipo_de_molecula = "protein"
def extract_sequences(filename,salida):
    files = 0
    if(salida == "genbank"): 
        SeqIO.convert(filename, "fasta", "sequences.gbk", "genbank", tipo_de_molecula)
        records = list(SeqIO.parse("sequences.gbk","genbank"))
        for i, record in enumerate(records): 
            archivo = open(f"sequence{i}.gbk", "w")
            archivo.write(record.format("genbank"))
            archivo.close()
            files = files+1 
    else:
        records = list(SeqIO.parse(filename,"fasta"))
        files = 0
        for i, record in enumerate(records): 
            archivo = open(f"sequence{i}.fasta", "w")
            archivo.write(record.format("fasta"))
            archivo.close()
            files = files+1 
    return(files) 
extract_sequences(filename,salida)
#Comienzo de la función extract_sequences_revcomp.
filename = "/mnt/c/Users/world/OneDrive/Escritorio/Allison/Ejercicio-Biopython/data/sequences.fasta"
def extract_sequences_revcomp(filename): 
    records = list(SeqIO.parse(filename, "fasta"))
    s = open(f"sequence_revcomp.fasta","w")
    for i, record in enumerate(records): 
        s.write(f'>{record.id}\n')
        s.write(f'{record.seq.reverse_complement()}\n')
    s.close()
    num_records = len(records)
    return (num_records)
extract_sequences_revcomp(filename)
