import time
f = open('testlist.csv','w')
for x in range(100):
    f.write(str(time.clock()))
    f.write("\n")
