import sys
# This script takes two arguments, IE The filenames of the pdb files compared

pdb_file1 = sys.argv[1]
pdb_file2 = sys.argv[2]

print("\n>>>>>Checking for PDB Inconsistencies Script Running")

path = "../data/pdb_output/"

print("Opening " + pdb_file1)
pdb1 = open(path + pdb_file1 , "r+")
print("Opening " + pdb_file2)
pdb2 = open(path + pdb_file2 , "r+")

pdb1_lines = pdb1.readlines()
pdb2_lines = pdb2.readlines()

print("The reference file (1) has : " + str(len(pdb1_lines)) + " lines")
print("The produced  file (2) has : " + str(len(pdb2_lines)) + " lines")



num_different = 0
for i in range(min(len(pdb1_lines), len(pdb2_lines))):
    if pdb1_lines[i].strip() == pdb2_lines[i].strip():
        pass
    else:
        if pdb1_lines[i].split()[0] == "CONECT":
            print(">>Error on CONECT @ line " + str(i+1))
        else:
            print(">>>> Error " + str(num_different+1))
            print("Line Number is : " + str(i+1))
            print("1>>" + pdb1_lines[i].strip())
            print("2>>" + pdb2_lines[i].strip() + "\n")
            num_different += 1
            if num_different is 10:
                exit()
