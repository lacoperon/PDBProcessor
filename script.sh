# !#/bin/bash
# Base script which runs python scripts therein



# Gets into relative directory where script lives
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
    # pwd
cd ./data/pdb_input

# Checks for pdb_input files,
# then runs our conversion python script on them
# for i in $( ls )
# do
#   echo $i #TODO: Run python script for all of these
# done

cd ../../code/

# Runs pdb processor for neighbourhood "n1_new", for all pdb files in pdb_input folder
/usr/bin/python3 processor.py "n1" ../data/pdb_input/*.pdb

# Can run 'check' script, against hand-picked script
# /usr/bin/python3 checkForInconsistencies.py 5jup_actual_selection.pdb 5jup_n1.pdb
