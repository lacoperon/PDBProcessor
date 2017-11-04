# PDB Processor

## Motivation

This is (or is to be) a Bash/Python script to parse PDB structural
files into given subsets of the PDB file (IE only residues 1-495).

Our motivation here is to pre-process some of our ribosome structures in
a standardized way, to ensure our structures have the same number of atoms,
and to confirm that all of our structures are comparable.

## How to setup to convert the files?

### Protein Input files

Put all pdb_formatted files to be converted into `/data/pdb_input/`.

TODO: Add converter, using PyMol, which converts `.cif` files from `/data/cif_input`,
into `.pdb` files, which can then be processed automatically in the same way.

### Configuration File
TODO: Add config file format .csv, and explanation, here

### Where does the output go?

The output of the script *will* go to `/data/output/`, and the name of the
outputted file will correspond to the original pdb name, with the name of the
'neighbourhood' of pruning applied to the end.

IE `5jup_n1.pdb` or `5jup_neighbourhood2.pdb`, or whatever is the desired extension.

## How do I run the script?

Firstly, run `chmod +x script.sh` to make script.sh executable.
Then, run `./script.sh` to execute the script.
