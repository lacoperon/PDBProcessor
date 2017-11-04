# PYTHON 3
import sys

if len(sys.argv) < 2:
    print("ERROR: No filename(s) specified. Try again, specifying file(s) to parse")
    sys.exit()

pdb_to_parse = sys.argv[1:]

# pdb_to_parse = ["../data/pdb_input" + f for f in pdb_to_parse]

print(pdb_to_parse)


for pdb_filename in pdb_to_parse:
    # Opens file; line buffering keeps it efficient and not slow, for large pdbs
    print("Opening " + pdb_filename)
    filedata = open(pdb_filename, "r", 1)

    for line in filedata:
        print(line)
