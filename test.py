string = "hello"
def compete(competeDNA):
    fitness = 0 
    the = [ord(c) for c in competeDNA]
    DNA = [ord(j) for j in string]
    that = len(DNA)
    #print(DNA)
    #print(the)
    #print(that)

    for i in DNA:
        #print(i)    
        for k in the:
        #print(k)
            fitness = abs(i-k)
            print(fitness)
       
    return fitness

compete("Thisiswee")