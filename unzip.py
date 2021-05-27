#!/usr/bin/env python

#import and start timer
import time
import zipfile
import sys

dirExtract = input('Enter the destination folder: ')
startTime = time.time()

# unzip all files in list from command line
for arg in sys.argv[1:]:
    print("Opening file", arg)
    with open(arg, 'rb') as f:
        print("  Unzipping file", arg)
        z = zipfile.ZipFile(f)
        for name in z.namelist():
            print("    Extracting file ", name + " to " + dirExtract)
            z.extract(name,dirExtract )
        
#print exection time 
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))