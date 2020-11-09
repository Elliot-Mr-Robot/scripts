#!/usr/bin/env python

import os


file_path = raw_input('Please enter full path to file: \n')
file_output = raw_input('Please enter file name for output: \n')
file_01 = raw_input('Please enter file 01 name: \n')
file_02 = raw_input('Please enter file 02 name: \n')

os.chdir(file_path)
with open(file_01,'r') as f01:
    list_01 = f01.read().splitlines()

with open(file_02,'r') as f02:
    list_02 = f02.read().splitlines()

'''
    print list_01[0]
    print('============================================================')
    print(list_02)

match_list = [n for n in list_02 if n[:1000] in list_01]
with open(file_output,'w+') as foutput:
    foutput.write('\n'.join(match_list))
'''

missing = [n for n in list_02 if n[:1000] not in list_01]
with open(file_output,'w+') as foutput:
    foutput.write('\n'.join(missing))
