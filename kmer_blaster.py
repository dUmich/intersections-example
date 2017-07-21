import Bio
import argparse
from Bio.Blast import NCBIWWW
from Bio.Blast.Applications import NcbiblastnCommandline

# sysargv 1 is kmer length, sysargv 2 is file name, sysargv 3 is database name
parser = argparse.ArgumentParser(description='''

This script takes a file of k-mers and blasts them against a single nucleotide database returning
position ID's for each k-mer.
By Daniel Harris 5-23-2015

 ''')

parser.add_argument('-db', help='blast database')
parser.add_argument('-q', help = 'sorted k-mers/p-values')
parser.add_argument('-o', help='output')
parser.add_argument('-p', help='percent identity')
args=parser.parse_args()

DB=args.db
Q=args.q
OUT=args.o
P=args.p

blast_tsv = NcbiblastnCommandline(query=Q, db=DB, perc_identity=P, outfmt=6, out=(OUT))
print(blast_tsv)
stdout, stderr = blast_tsv()

