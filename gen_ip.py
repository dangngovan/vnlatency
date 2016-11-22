#43.239.148
for j in range(255,256):
    for i in range(0,255):
        f = open('ipdata', 'a')
        print >> f, '222.%s.%s.0/24:VNPT VDC'%(j,i)
        f.close()