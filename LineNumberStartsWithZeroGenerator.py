import hashlib
import time

apt = ''
x = 0
prev = 0

count = 0.0
t = time.time()
tp = time.time()


f = open("LineNumberStartsWithZeroGeneratorLineNumberOutput.txt", "a")
fs = open("LineNumberStartsWithZeroGeneratorHashOutput.txt", "a")
fp = open("PatternOfHashesStartingWithZero.txt", "a")

while (not apt.startswith('0000')):

    apt = hashlib.sha256('A' + str(x)).hexdigest()
    #print(apt)
    if('00' in apt):
        f.write(str(x) + ', ')
        fp.write(str(x - prev) + ', ')
        fs.write(apt + '\n')
        prev = x
        
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
fs.close()
fp.close()

print("Total Hashes/ Nonce number: " + str(x))

