#This program takes a text file as input whic is downloaded from NCBI blast search. The text file contains the pdb codes
# for all the homologs. This programs automatically downloads all the pdb files of the homologs. It parses the text file and then downloads 
#using the variable url.
from sys import argv 
import urllib,os

#name of the text file which has all the homologs
#The same folder will hold all the pdb files
fileName = '/media/qazi/EAD2-9C2F/LabWork/Documents/HomologsTextFile'
with open(fileName) as textFile:
        lines = textFile.readlines()
        for i, line in enumerate(lines):
                content = line.split()
                #print content
                if content:
                        myWord = content[0]
                        myChain = content[2]
                        print myChain
                        if myWord.startswith('pdb'):
                                checkWord = myWord.split('|')
                                eValue1 = line[-6:]
                                eValue = eValue1.split()
                                eValue = float(eValue[0])
                                #print eValue
                                if eValue < 0.002:
                                        var = checkWord[1]
                                        os.system('wget http://files.rcsb.org/download/%s.pdb'%var)
                                
                        
print 'done!'              
                
                 
                 
                                         
                 
        


 
 
 
 
