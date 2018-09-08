'''
Elliot Williams
September 8th, 2018
`check_residue_order.py`
'''

import re

def get_residue_order(filename):
    f = open(filename)

    curr_resid = None
    residues = []
    for line in f:
        resid = line[22:28].strip()
        resname = line[17:21].strip()

        if resid != curr_resid and resid != "":
            residues.append("{}|{}".format(resname,resid))
            curr_resid = resid

    return residues

def compare_residue_order(residues1, residues2):

    if len(residues1) != len(residues2):
        rl1 = len(residues1)
        rl2 = len(residues2)
        raise Exception("Not same # of residues; {} vs {}".format(rl1, rl2))

    for i in range(len(residues1)):
        res1 = residues1[i]
        res2 = residues2[i]
        if res1 != res2:
            res1_strip = re.sub("(?<=[UATGC])5", "", res1)
            res2_strip = re.sub("(?<=[UATGC])5", "", res2)

            his_res1 = re.sub("D", "S", res1)
            his_res2 = re.sub("D", "S", res1)

            if res1_strip != res2_strip and his_res1 != his_res2:
                raise Exception("{} in file1 is not {} in file2".format(res1, res2))

    print("PDB files are equivalent in residue order")

if __name__ == "__main__":
    import sys

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    resids1 = get_residue_order(filename1)
    resids2 = get_residue_order(filename2)

    compare_residue_order(resids1, resids2)
