"""This program was written for my thesis in the field of bioinformatics"""
import os
import numpy as np
from shutil import copyfile
import csv
import ast

class copy:
    def init(self,filename):
        filename = None
    def copyIntersection(self,path1,path2,srcPath,dstPath):
        #this program does the intersection of files in two folders and copies the intersection in another folder
        t=[]
        os.chdir(path1)
        pdbfiles = os.listdir('.')
        pdbfiles2 =os.listdir(path2)
        for f in pdbfiles:
            t.append(f)
        for i in t:
            for g in pdbfiles2:
                if i.lower()==g.lower():
                    src =srcPath+i
                    dst=dtsPath+i
                    copyfile(src, dst)
                    
    def copyfilesUsingtxt(self,inpath,src,dest):
        """This function reads a txt file and copies the files named in the text file from source folder
        to destination folder"""
        f = open(inpath, mode='r')
        codes = f.read()
        cod= codes.splitlines()
        pdb = os.listdir(src)
        codes = [c.lower() for c in cod]
        pdbfiles = [d[:5].lower() for d in pdb]
        for p in pdbfiles:
            if p in codes:
                s = src+p+'.pdb'
                d = dest+p+'.pdb'
                copyfile(s,d)
                print p
           
            
    def copyfilenamesInText(self, inputPath,outPath):
        mystructs = os.listdir(inputPath)
        f= open(outPath, mode='a')
        for structs in mystructs:
            f.write(structs[:-4])
            f.write('\n')

        
    def ReadTxtCopyIntoSubFamilyFolders(self,txtPath,subfolderPath,csvPath):
        f = open(txtPath, 'r')
        pdbList = f.read()
        with open(csvPath,'rb') as csvfile:
            reader = csv.reader(csvfile,delimiter ='\t')
            for line in reader:
                pdbids = line[28]
                #pdbids = eval(line[28])
                print pdbids
                
    def DivideIntoSubFamilies(self,SFDLInPath,SFLDoutPath,outputPath,csvInput):
        """This Function is used to divided the protein structure families into subfamilies using a csv file
        which have the information about the subfamilies the PDB's belong to""""
        filelist_ext = os.listdir(SFDLInPath)
        filelist = [x[:-4] for x in filelist_ext]
        f = open(SFLDoutPath, mode = 'a')
        for s in filelist:
            f.write(s)
            f.write('\n')
        #f.close()
        with open(csvInput) as csvfile:
            reader = csv.reader(csvfile,delimiter = '\t')
            for row in reader:
                foldername  = row[6]
                pdbs = row[28].split()
                for p in pdbs:
                    if p in filelist:
                        source = SFDLInPath+p+'.pdb'
                        dst = outputPath+foldername+'/'+p+'.pdb'
                        print dst
                        copyfile(source,dst)        


class folders:
    def makefolders(self,path):
        os.makedirs(path)
        
    def listFilesInFolder(self,folderPath):
        fileList = os.listdir(folderPath)
        return fileList
