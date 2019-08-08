import numpy as np
import pandas as pd
import re
import sys
from os.path import basename, splitext
from os.path import isfile, isdir, join
from os import listdir
from os import mkdir

def load_dictionary(infile, split_char=' '):
    phoneDict = dict()
    lines = readFile(infile)
    
    for line in lines:
        words = re.split(split_char, line)
        key = words[0]
        del words[0]        
        phoneDict[key] = ' '.join(words)
    
    return phoneDict

def readFile(file):    
    if(isfile(file)):
        f = open(file)
        lines = [line.rstrip() for line in f]
        return lines
    else:
        print ("File: " + file +" does not exists")
        sys.exit(1);    

def getFileNames(dirname, ext):
    filenames = [f for f in listdir(dirname) if re.search(ext, f) and isfile(join(dirname, f))]
    return filenames        

def getFullFileNames(dirname, ext):
    filenames = getFileNames(dirname, ext)
    full_filenames = [join(dirname, f) for f in filenames]
    return full_filenames    

def readFile(file):    
    if(isfile(file)):
        f = open(file)
        lines = [line.rstrip() for line in f]
        return lines
    else:
        print ("File: " + file +" does not exists")
        sys.exit(1);    