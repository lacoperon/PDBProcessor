# PYTHON 3
import sys

if len(sys.argv) < 3:
    print("ERROR: No filename(s) specified. Try again, specifying file(s) to parse")
    sys.exit()

nn = sys.argv[1]
pdb_to_parse = sys.argv[2:]

# pdb_to_parse = ["../data/pdb_input" + f for f in pdb_to_parse]






# function which converts a num to a length 5 atom number
# OR RESIDUE
def atomNumToString(num):
    if 0 <= num and num < 10:
        return "    " + str(num)

    if 10 <= num and num < 100:
        return "   " + str(num)

    if 100 <= num and num < 1000:
        return "  " + str(num)

    if num > 1000 and num < 10000:
        return " " + str(num)

    if num >= 10000 and num < 100000:
        return str(num)

    else:
        return "99999"

# function which converts a num to a length 4 atom number
# OR RESIDUE
def residNumToString(num):
    if 0 <= num and num < 10:
        return "   " + str(num)

    if 10 <= num and num < 100:
        return "  " + str(num)

    if 100 <= num and num < 1000:
        return " " + str(num)

    if num > 1000 and num < 10000:
        return str(num)

    else:
        return "9999"


#TODO: Fix artificial picking of .pdb structures to parse
pdb_to_parse = ["../data/pdb_input/5jup.pdb"]
for pdb_filename in pdb_to_parse:

    structure_inputs = (
        {"chain_name": "A",
         "region_start": 1,
         "region_end" : 31},
        {"chain_name": "A",
         "region_start": 547,
         "region_end" : 600},
        {"chain_name": "A",
         "region_start": 1108,
         "region_end" : 1113},
        {"chain_name": "A",
         "region_start": 1133,
         "region_end" : 1140}
    )

    current_region = 0
    target_chain_name = structure_inputs[current_region]["chain_name"]
    target_range_start = structure_inputs[current_region]["region_start"]
    target_range_end   = structure_inputs[current_region]["region_end"]

    # Opens file; line buffering keeps it efficient and not slow, for large pdbs
    print("Opening " + pdb_filename)
    filedata = open(pdb_filename, "r", 1)
    path = "../pdb_output/"
    new_file = open(pdb_filename[0:len(pdb_filename)-4]+"_"+nn+".pdb" , "w")

    current_region = 0
    atom_num_counter = 1
    current_atom_number = 1
    current_chain = "CURRENTLY NULL"


    for line in filedata:
        atom_string= line[0:4]
        is_atom = atom_string == "ATOM"
        if is_atom:
            chain_name = line[72:74]
            # defines residue/base number
            rb_num = int(line[22:26])
            # string with resid/base type, chain nickname
            type_nick = line[18:22]
            # written atom num
            written_atom_num = int(line[8:12])

            if chain_name != current_chain:
                # print("Last number: " + str(current_atom_number))
                current_chain = chain_name
                # print("New chain: "   + str(current_chain))
                current_atom_number = 1

            if chain_name.strip() is target_chain_name:
                if rb_num >= target_range_start and rb_num <= target_range_end:
                    line = line[0:5] + atomNumToString(atom_num_counter) + line[11:]
                    new_file.write(line)
                    atom_num_counter += 1
                # Edge case to deal with : end of chain is in our subset -- not dealt with yet
                if rb_num == (target_range_end + 1):
                    atom_num = atomNumToString(current_atom_number)
                    ter_line = "TER" + (" " * 2) + atomNumToString(atom_num_counter)
                    ter_line += " " * 7 + last_type_nick + residNumToString(rb_num-1) + "\n"
                    print(written_atom_num)
                    print(ter_line)
                    current_region += 1
                    if current_region < len(structure_inputs):
                        target_chain_name = structure_inputs[current_region]["chain_name"]
                        target_range_start = structure_inputs[current_region]["region_start"]
                        target_range_end   = structure_inputs[current_region]["region_end"]
                    else:
                        target_chain_name = "all_chains_represented"
                        target_range_start = -1
                        target_range_end   = -1

                    new_file.write(ter_line)
                    atom_num_counter += 1



            current_atom_number += 1
            last_type_nick = type_nick


    # This happens automatically,
    # but it's good practice -- in case I add more stuff
    filedata.close()
    new_file.close()
