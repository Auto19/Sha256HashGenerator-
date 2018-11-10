import hashlib
import time

apt = ''
x = 0

count = 0.0
t = time.time()
tp = time.time()


f = open("HashesOutput.txt", "a")

totalhashes = 0
while (not apt.startswith('0000')):

    apt = hashlib.sha256('A' + str(x)).hexdigest()
    #print(apt)
    f.write(apt + '\n')
    
    if(tp-t >= 5.0):
        print(str(count/5) + " H/s")
        t = tp
        count = 0
    else:
        count = count + 1
        tp = time.time()
        #print(tp-t)
    x = x + 1


f.close()

print("Total Hashes: " + str(x))

