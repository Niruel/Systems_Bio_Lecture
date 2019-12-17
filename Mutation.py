import string
import random
def mutateString(DNA):
    a = chr(random.randint(0,127))
    print(a)
    newString= DNA
    y = random.randint(0,len(newString))
    print(y)
    s = random.randint(1,100)
    print(s)
    for _ in range(100):
        if s==1:
            SnewString= " ".join((newString[:y],a,newString[y+1:]))
            print(SnewString)
            break
    
    return DNA    
mutateString("Michel")

