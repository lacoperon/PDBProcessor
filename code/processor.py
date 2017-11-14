# PYTHON 3
import sys
import csv

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

    if num >= 1000 and num < 10000:
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

    if num >= 1000 and num < 10000:
        return str(num)

    else:
        return "9999"


#TODO: Fix artificial picking of .pdb structures to parse
pdb_filenames = ["5jup.pdb"]
# pdb_to_parse = ["../data/pdb_input/5jup.pdb"]

with open('../config/n1.csv', mode='r') as infile:
    reader = csv.reader(infile)
    isHeader = True

    structure_inputs = []

    for row in reader:
        if isHeader:
            isHeader = False
        else:
            current_dict = {}
            current_dict["chain_name"] = row[0]
            current_dict["region_start"] = int(row[1])
            current_dict["region_end"] = int(row[2])
            structure_inputs.append(current_dict)

    print(structure_inputs)



for pdb_filename in pdb_filenames:
    pdb_no_ext = pdb_filename
    pdb_filename = "../data/pdb_input/" + pdb_filename

    current_region = 0
    target_chain_name = structure_inputs[current_region]["chain_name"]
    target_range_start = structure_inputs[current_region]["region_start"]
    target_range_end   = structure_inputs[current_region]["region_end"]

    # Opens file; line buffering keeps it efficient and not slow, for large pdbs
    print("Opening " + pdb_filename)
    filedata = open(pdb_filename, "r", 1)
    path = "../data/pdb_output/"
    new_file = open(path + pdb_no_ext[:len(pdb_no_ext)-4] +"_"+ nn + ".pdb" , "w")

    current_region = 0
    atom_num_counter = 1
    current_atom_number = 1
    current_chain = "CURRENTLY NULL"

    for i in structure_inputs:
        print(i["chain_name"] + "from " + str(i["region_start"]) +" to "+ str(i["region_end"]))


    for line in filedata:
        atom_string= line[0:4]
        is_atom = atom_string == "ATOM"
        if is_atom:
            chain_name = line[72:74]
            # print(chain_name)
            # defines residue/base number
            rb_num = int(line[22:26])
            # string with resid/base type, chain nickname
            type_nick = line[17:22]
            # written atom num
            written_atom_num = int(line[8:12])

            if chain_name.strip() != current_chain.strip:
                # print("Last number: " + str(current_atom_number))
                current_chain = chain_name.strip()
                # print(current_chain)
                # print("New chain: "   + str(current_chain))
                # current_atom_number = 1

            if chain_name.strip() == target_chain_name.strip():
                # print("TRUE" + chain_name)
                if rb_num >= target_range_start and rb_num <= target_range_end:
                    line = line[0:6] + atomNumToString(atom_num_counter) + line[11:]
                    new_file.write(line)
                    atom_num_counter += 1
                # Edge case to deal with : end of chain is in our subset -- not dealt with yet
                if rb_num == (target_range_end + 1):
                    atom_num = atomNumToString(current_atom_number)
                    ter_line = "TER" + (" " * 3) + atomNumToString(atom_num_counter)
                    ter_line += " " * 6 + last_type_nick + residNumToString(last_rbnum) + "\n"
                    # print(written_atom_num)
                    # print(ter_line)
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
            last_rbnum = rb_num


        is_ter = line[0:3] == "TER"
        if is_ter:
            print(line)
            if chain_name.strip() == target_chain_name.strip():
                # Edge case to deal with : end of chain is in our subset -- not dealt with yet
                if rb_num == target_range_end :
                    atom_num = atomNumToString(current_atom_number)
                    ter_line = "TER" + (" " * 2) + atomNumToString(atom_num_counter)
                    ter_line += " " * 7 + last_type_nick + residNumToString(rb_num-1) + "\n"
                    # print(written_atom_num)
                    # print(ter_line)
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
