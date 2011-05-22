'''
Created on May 21, 2011

@author: Ethan
'''

import sys


def getLikeness(firstEng, secondEng):
    assert len(firstEng) == len(secondEng), "needs same length"
    
    #print firstEng, secondEng
    
    appearedYet = [False for _ in xrange(0,len(firstEng))]
    
    score = 0
    for drinka, drinkb,curPoints in zip(firstEng,secondEng,xrange(len(firstEng),0,-1)):  
        if drinka == drinkb:
            #print "first at ", curPoints
            score +=  curPoints ** 2
                        
        elif (appearedYet[drinka] == False):
            #print "second at ", curPoints
            appearedYet[drinkb] = True
            score += curPoints
            
        #print curPoints
            
    return score    
        
    

if __name__ == '__main__':

    #print "hello world"
    #print sys.argv
    f = open (sys.argv[1],'r')
    theStr = f.readlines()
    
    
    
    firstLine = theStr[0].split()
    numOfEng = int(firstLine[0])
    numOfDrinks = int(firstLine[1])
    
    posInFile = 1 +  int(numOfDrinks)  
    
    engList = [[0 for i in xrange(0,numOfDrinks)] for i in xrange(0,numOfEng)]
    
    for i in xrange(0,numOfEng):
        lineStr = map(int,theStr[i + posInFile].split()[1].split(',')) #gets a string, splits it to get rid of start, splits again to get numbers seperate, and then uses map and int
        engList[i] = lineStr
    
    #print engList
    
    #print engList
    
    
    goodEng = engList[:len(engList)/2]
    badEng = engList[len(engList)/2:]
    #print goodEng, badEng
    
    
    results  = [0 for _ in xrange(0,len(goodEng))]
    used  = [False for _ in xrange(0,len(badEng))]
    
    for i in xrange (0,len(goodEng)):
        theMax = getLikeness(goodEng[i],badEng[0])
        theMaxOne = 0
        
        for b in xrange (1,len(badEng)):
        
            if (not used[b]) and getLikeness(goodEng[i],badEng[b]) >= theMax:
                theMax = getLikeness(goodEng[i],badEng[b])
                theMaxOne = b
                
        used[theMaxOne] = True
        results[i] = theMaxOne + len(goodEng)
    
    #print results
                
    for i,num in zip(results,xrange(0,len(results))):
        print num, i
        
    print   0xFACEB00C >> 2
    
    #print getLikeness(engList[0],engList[3])
    
    
    
    
    
    