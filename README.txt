# filematching
Match files to multiple templates

for example you have:

my_stupid_file_00001.txt
my_stupid_file_00002.txt
my_stupid_file_00003.txt
my_stupid_file_00004.txt

give it template:
my_stupid_file_&.txt

and search templates:
&_extrastupid.dat, otherfile_&_test.blah

looks for:
00001_extrastupid.dat
otherfile_0001_test.blah
00002_extrastupid.dat
otherfile_0002_test.blah

and etc...

reports back which files are missing the partner files.  
