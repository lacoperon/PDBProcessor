# !#/bin/bash
# Base script which runs python scripts therein



# Gets into relative directory where script lives
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
    pwd
cd ./data/pdb_input

# Checks for pdb_input files,
# then runs our conversion python script on them
for i in $( ls )
do
  echo $i #TODO: Run python script for all of these
done

cd ../../code/

/usr/bin/python3 processor.py "n1" ../data/pdb_input/*.pdb
