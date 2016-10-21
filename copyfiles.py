"""This program is used to copy the files using 2 diffrent different methods"""
import os
import numpy as np
from shutil import copyfile

class copy:
    def init(self,filename):
        filename = None
    def copyIntersection(self,path1,path2):
        #This function does the intersection of files in two folders and copies the intersection in 		      another folder
        path1 = 'SourceFolder1'
        path2='SourceFolder2'
        t=[]
        os.chdir(path1)
        pdbfiles = os.listdir('.')
        pdbfiles2 =os.listdir(path2)
        for f in pdbfiles:
            t.append(f)
        for i in t:
            for g in pdbfiles2:
                if i.lower()==g.lower():
                    src ='SourceFolder1'+i
                    dst='DestinationFolder'+i
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
           
            
            
        
