import sys
# This script takes two arguments, IE The filenames of the pdb files compared

pdb_file1 = sys.argv[1]
pdb_file2 = sys.argv[2]


'''
Input: filename for which we're trying to calculate
Output: number of lines in each file
'''
def file_len(file):
    with file as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print("Opening " + pdb_file1)
path = "../data/pdb_output/"
# filedata = open(path + pdb_file1, "r", 1)
pdb1 = open(path + pdb_file1 , "r+")
pdb2 = open(path + pdb_file2 , "r+")

pdb1_lines = pdb1.readlines()
pdb2_lines = pdb2.readlines()

print("The reference file has : " + str(len(pdb1_lines)) + " lines")
print("The produced  file has : " + str(len(pdb2_lines)) + " lines")

for i in range(min(len(pdb1_lines), len(pdb2_lines))):
    if pdb1_lines[i].strip() == pdb2_lines[i].strip():
        pass
    else:
        print("\nLine Number is : " + str(i+1))
        print("1>>" + pdb1_lines[i])
        print("2>>" + pdb2_lines[i])
        exit()
