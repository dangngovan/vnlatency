#!/usr/bin/python
import os

f1 = open('ipdatatest','r')
list_f1 = []
for line in f1:
    list_f1.append(line.strip())

with open('ipdatafinal') as oldfile, open('data3', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in list_f1):
            newfile.write(line)