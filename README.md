# intersections-example
Example folder for intersections (https://github.com/PlasmaPower/intersections)

This is an example of one way to use intersections, finding the location of an unlabeled gene. We are searching the known colistin 
resistance gene MgrB against a colistin resistant genome to see where it resides.

## Commands run:

### gff file produced using (with appropriate modules or programs installed)

```
prokka-1.12/bin/prokka -kingdom Bacteria -rfam -outdir ./path/to/prokkadatabase/R_113 -force -prefix R_113 R_113.fasta
```
https://github.com/tseemann/prokka

### bla file produced using (with appropriate modules or programs installed)

1. Create blast database
```
makeblastdb -in R_113.fasta -dbtype nucl -parse_seqids -out ./blast_databases/R_113/R_113
```
http://nebc.nox.ac.uk/bioinformatics/docs/makeblastdb.html

2. Blast sequence -MgrB gene- using kmer_blaster (included in example folder)

```
/anaconda2/bin/python kmer_blaster.py -db ./R_113/R_113 -q ./MrgB.gene -o ./bla_gff/R_113.bla -p 100
```
http://biopython.org/DIST/docs/api/Bio.Blast.Applications.NcbiblastnCommandline-class.html

### Intersections output created using

```
cd ~/intersections-example
/path/to/intersections/intersections -s ./bla_gff/ > intersections_output.tsv
```
