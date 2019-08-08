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