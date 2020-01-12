import random
import collections as cntr

with open('ais_text.txt', 'r') as openReadFile:
    data = openReadFile.read()
    counter = cntr.Counter(data)
    selection = random.choice(list(counter.items()))
    for i in selection:
        print(i)
        # print(selection)
    #dataLen = len(data)


# with open('myNewtes.txt', 'w') as openWriteFile:
   # openWriteFile.write("text")
