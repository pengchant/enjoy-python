import sys
import time

f = None

try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end = ' ')
        sys.stdout.flush()
        print('-------press ctrl+c now-------')
        time.sleep(2)
except IOError:
    print('could not find file poem.txt')
except KeyboardInterrupt:
    print("! you cancelled the reading from the line.")
finally:
    if f:
        f.close()
    print('cleaning up:closed the file')