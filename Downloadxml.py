"""This code downloads xml files. It Writes PDB codes into a file 
   and uses the codes in wget"""
from sys import argv 
import urllib,os


path = '/home/qazi/mydata/LabWork/Data/EnolaseSubGroupsNodupRaw/MuconateLactonizingEnzyme'
os.chdir(path)
pdbfiles = os.listdir('.')
filepath = '/media/qazi/EAD2-9C2F/LabWork/Documents/MuconateLactonizingEnzymeNoDuplicatePDBs'


for files in pdbfiles:
    #os.system('wget http://files.rcsb.org/download/%s.xml.gz'%files[:4])
    f = open(filepath,'a')
    f.write(str(files[:5]))
    f.write('\n')
    f.flush()
f.close()
print 'yay'         