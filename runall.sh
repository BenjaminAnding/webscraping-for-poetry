mkdir ./authors
rm -r authors/*/combined.txt
rm -r authors/*/label.txt
rm ./labels.txt
python ./anthmagverse.py 
python ./anthmasspoets.py 
python ./elizabethanverse.py 
python ./georgianverse.py 
python ./newpoetry.py 
python ./oxfordengverse.py 
python ./oxfordvictverse.py 
python ./restorationverse.py 
python ./cleanandlabel.py
