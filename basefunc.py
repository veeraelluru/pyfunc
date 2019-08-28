import numpy as np
import pandas as pd
import re
import sys
from os.path import basename, splitext
from os.path import isfile, isdir, join
from os import listdir
from os import mkdir

def writeJsonFile(dictList, keyname, outJsonFile):
    intentsDict = {keyname:dictList}
    jsonData = json.dumps(intentsDict, indent=2, sort_keys=True, separators=(',', ':'))
    with open(outJsonFile, "w") as jFile:
        jFile.write(jsonData)