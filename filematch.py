#!/usr/bin/env python

# match files, make sure each has its corresponding partner files
# writes a list of offending files

import glob
import sys

files = glob.glob(raw_input("file search string: "))
for i in files:
    print i

print "file template is: invariant part of file name, & for the file number IE: file_01_stuff.txt == file_&_stuff.txt"
filetemplate = raw_input("file template: ").split('&')
print "match templates, with & for the numbers, enter multiple separarted by commas "
matchtemplates = raw_input("templates to match: ").strip()
matchtemplates = matchtemplates.split(',')

missingfiles = {}

allfiles = glob.glob("*")
files.sort()
for i in files:
    number1 = i.replace(filetemplate[0],'')
    number = number1.replace(filetemplate[1],'')
    for j in matchtemplates:
        halves = j.split('&')
        if "{0}{1}{2}".format(halves[0],number,halves[1]) not in allfiles:
            if i not in missingfiles.keys():
                missingfiles[i] = ["{0}{1}{2}".format(halves[0],number,halves[1])]
            else:
                missingfiles[i].append("{0}{1}{2}".format(halves[0],number,halves[1]))

output = open("offending_files.txt","w")
for i in missingfiles:
    print i, missingfiles[i]
    output.write("{0}\n".format(i))
print len(missingfiles)," mismatched files"
