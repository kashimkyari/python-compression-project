#!/usr/bin/env python
import zipfile
import sys
# unzip all files in list from command line
for arg in sys.argv[1:]:
    print("Opening file", arg)
    with open(arg, 'rb') as f:
        print("  Unzipping file", arg)
        z = zipfile.ZipFile(f)
        for name in z.namelist():
            print("    Extracting file", name)
            z.extract(name,"./")