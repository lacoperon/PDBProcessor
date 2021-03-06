# PYTHON 3
import sys
import csv

if len(sys.argv) < 3:
    print("ERROR: No filename(s) specified. Try again, specifying file(s) to parse")
    sys.exit()

nn = sys.argv[1]
pdb_to_parse = sys.argv[2:]
pdb_list = []
for filename in pdb_to_parse:
    path = filename.split("/")
    pdb_list.append(path[len(path)-1])

print(pdb_list)


# function which converts a num to a length 5 atom number
# OR RESIDUE
def atomNumToString(num):

    if 0 <= num and num < 100000:
        return "{:5d}".format(num)
    else:
        return "99999"

# function which converts a num to a length 4 atom number
# OR RESIDUE
def residNumToString(num):

    if 0 <= num and num < 10000:
        return "{:4d}".format(num)

    else:
        return "9999"


pdb_filenames = pdb_list

print(">>>>>PDB Parser Script Running")
neighbourhood_file = "../config/" + nn +".csv"
print("Using neighbourhood: " + nn)

with open(neighbourhood_file, mode='r') as infile:
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



for pdb_filename in pdb_filenames:
    pdb_no_ext = pdb_filename
    pdb_w_ext = "../data/pdb_input/" + pdb_filename

    current_region = 0
    target_chain_name = structure_inputs[current_region]["chain_name"]
    target_range_start = structure_inputs[current_region]["region_start"]
    target_range_end   = structure_inputs[current_region]["region_end"]

    # Opens file; line buffering keeps it efficient and not slow, for large pdbs
    print("Opening " + pdb_no_ext)
    filedata = open(pdb_w_ext, "r", 1).readlines()
    path = "../data/pdb_output/"
    new_file = open(path + pdb_no_ext[:len(pdb_no_ext)-4] +"_"+ nn + ".pdb" , "w")

    atom_num_counter = 1
    current_atom_number = 1
    current_chain = "CURRENTLY NULL"

    for i in structure_inputs:
        print(">>>Currently parsing chain " + i["chain_name"].ljust(3) + " from " + str(i["region_start"]).ljust(5) +" to "+ str(i["region_end"]).ljust(5))


    while target_chain_name != "all_chains_represented":
        for line in filedata:
            atom_string= line[0:6]
            is_atom = atom_string.strip() == "ATOM" or atom_string.strip() == "HETATM"
            if is_atom:
                chain_name = line[72:74]

                # defines residue/base number
                rb_num = int(line[22:26])
                # string with resid/base type, chain nickname
                type_nick = line[17:22]
                # written atom num
                written_atom_num = int(line[8:12])

                if chain_name.strip() != current_chain.strip:
                    current_chain = chain_name.strip()

                if chain_name.strip() == target_chain_name.strip():
                    if rb_num >= target_range_start and rb_num <= target_range_end:
                        line = line[0:6] + atomNumToString(atom_num_counter) + line[11:]
                        new_file.write(line)
                        atom_num_counter += 1

                    if rb_num == (target_range_end + 1):
                        atom_num = atomNumToString(current_atom_number)
                        ter_line = "TER" + str(atom_num_counter).rjust(8)
                        ter_line += " " * 6 + last_type_nick + residNumToString(last_rbnum) + "\n"
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

            if line[0:3] == "TER":
                if chain_name.strip() == target_chain_name.strip():
                    if rb_num == target_range_end :
                        atom_num = atomNumToString(current_atom_number)
                        ter_line = "TER" + str(atom_num_counter).rjust(8)
                        ter_line += " " * 6 + last_type_nick + residNumToString(last_rbnum) + "\n"
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

    new_file.close()

# Opens file, and removes the last line (IE the last TER, which is unnecessary)
path = "../data/pdb_output/"
new_file = open(path + pdb_no_ext[:len(pdb_no_ext)-4] +"_"+ nn + ".pdb")
lines = new_file.readlines()
w = open(path + pdb_no_ext[:len(pdb_no_ext)-4] +"_"+ nn + ".pdb",'w')
w.writelines(item for item in lines[:-1])

# Writes 'END' at the end of file (canonical PDB end line)
w.write("END")
w.close()
