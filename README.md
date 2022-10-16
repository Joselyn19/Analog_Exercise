# Python Line Count Exercise

This Python program takes a directory as a required argument and a filename extension as optional argument that defaults to “.txt”. The program locates all files with the given extension in the given directory and all its subdirectories to produce a list of all matching files with the numbers of lines within the file. The program also output the total number of lines and the average number of lines per file. 

Example
```
./file1.txt		10
./file2.txt		25
./d1/d1fa.txt	5
./d1/d1fb.txt	37
===============
Number of files found: 	4
Total number of lines:  77
Average lines per file:	19.25
```

## File/Directory
Here is the main files and directory in this program.
```
analyse_file.py:            Module to analyse file
analyse_file_unit_tests.py: Unit test for analyse_file.py
line_count_script.py:       Script to count lines in files with module analyse_file
test_directory:             Directory for unittest
```

## How to Use
Clone the repository and run
```
python3 line_count_script.py --directory [required]_your_directory_ --extension _your_extension_
```
example 
```
python3 line_count_script.py --directory ./test_directory --extension .md
=================================
Number of files found: 3
Total number of lines: 3
Average lines per file: 12.33
```

## Unit Tests

Test Cases
1. Invalid directory
2. No target extension in directory
3. No other directory in the current directory
4. Has directories in the current directory
5. Has directories in the current directory, extension .md
6. Has directories in the current directory, extension .py

**Run Test Case**
```
python3 ./analyse_file_unit_tests.py
```
**sample output**
```
...No such directory!
...
----------------------------------------------------------------------
Ran 6 tests in 0.008s

OK
```

## Pylint
**Run pylint**
```
pylint --rcfile=pylint.conf line_count_script.py
pylint --rcfile=pylint.conf analyse_file.py
pylint --rcfile=pylint.conf line_count_script.py
```
All pylint pass