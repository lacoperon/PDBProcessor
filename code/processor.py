# PYTHON 3
import sys

if len(sys.argv) < 3:
    print("ERROR: No filename(s) specified. Try again, specifying file(s) to parse")
    sys.exit()

nn = sys.argv[1]
pdb_to_parse = sys.argv[2:]

# pdb_to_parse = ["../data/pdb_input" + f for f in pdb_to_parse]

print(pdb_to_parse)


for pdb_filename in pdb_to_parse:
    # Opens file; line buffering keeps it efficient and not slow, for large pdbs
    print("Opening " + pdb_filename)
    filedata = open(pdb_filename, "r", 1)
    path = "../pdb_output/"
    new_file = open(path+pdb_filename[0:len(pdb_filename)-4]+"_"+nn+".pdb" , "w")

    current_atom_number = 1
    current_chain = "CURRENTLY NULL"
    for line in filedata:
        atom_string= line[0:4]
        chain_name = line[72:74]
        is_atom = atom_string == "ATOM"
        if is_atom:
            if chain_name != current_chain:
                new_file.write(chain_name + "\n")
                print("Last number: " + str(current_atom_number))
                current_chain = chain_name
                print("New chain: "   + str(current_chain))
                current_atom_number = 1
            current_atom_number += 1

    # This happens automatically,
    # but it's good practice -- in case I add more stuff
    filedata.close()
    new_file.close()
