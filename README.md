# PDB Processor

## Motivation

This is a Bash/Python script to parse PDB structural
files into given subsets of the PDB file, based on the 'neighbourhood' csv
file it is given as input.

Our motivation here is to pre-process some of our ribosome structures in
a standardized way, to ensure our structures have the same number of atoms,
and to confirm that all of our structures are comparable.

**Note:** The current version of this script doesn't know what to do with
`CONECT` lines; this should be fairly easy to implement later using a dictionary
between input atom numbers and output atom numbers, but wasn't necessary at the time,
so is unimplemented.

## How to setup to convert the files?

### Protein Input files

Put all PDB_formatted files to be converted into `/data/PDB_input/`. The script
`code/processor.py` will automatically be run for each PDB file in this folder,
and will output a file appended with the neighbourhood name at the end within
`data/PDB_output`.

### Configuration File

This neighbourhood csv file should be saved in `config/[NEIGHBOURHOOD_NAME].csv`.

An example csv is shown in `config/n1.csv`. Note the three columns,
`chain name`, `region_start`, and `region_end`.

### Where does the output go?

The output of the script goes to `/data/output/`, and the name of the
outputted file will correspond to the original PDB name, with the name of the
'neighbourhood' of pruning applied to the end.

IE `5jup_n1.PDB` or `5jup_neighbourhood2.PDB`, or whatever is the desired extension.

## How do I run the script?

Firstly, run `chmod +x script.sh` to make script.sh executable.
Then, run `./script.sh` to execute the script.

## Error Checking

I also wrote a script, `code/checkForInconsistencies.py`, which compares two
PDB files (IE one picked by hand, and one parsed by `code/processor.py`), and
prints out when and where errors are found. You can use this to check that the
script runs as expected.

## Any more questions?

Ask me (Elliot)
