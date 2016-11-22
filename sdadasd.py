#!/usr/bin/python
file = open('ipdatafinal','r')
file2 = open('ipdatatest','w')
for i in file:
    print >> file2,i.split("|")[3].strip()