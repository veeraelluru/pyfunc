import numpy as np
import pandas as pd
import re
import sys
from os.path import basename, splitext
from os.path import isfile, isdir, join
from os import listdir
from os import mkdir
import json

def writeJsonFile(dictList, keyname, outJsonFile):
    intentsDict = {keyname:dictList}
    jsonData = json.dumps(intentsDict, indent=2, sort_keys=True, separators=(',', ':'))
    with open(outJsonFile, "w") as jFile:
        jFile.write(jsonData)

def load_dictionary(infile, split_char=' '):
    phoneDict = dict()
    lines = readFile(infile)
