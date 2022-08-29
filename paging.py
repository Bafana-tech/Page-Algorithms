### Paging Algorithms
### Name: Bafana Mhlahlo
### Student No: MHLBAF004



import random
import array
import sys
try:
   import queue
except ImportError:
   import Queue as queue

import subprocess


''' Here with fifo we replace pages using first come first serve method, removing the first one to come in'''

def FIFO(size, page):
    
    faultCount = 0
    frameElements = []
    frameLength = len(frameElements)
   
    # My memory is a queue
    memoryMain = queue.Queue(maxsize=size)

    for i in range(len(page)):
        
        #check if the size frameLength has elements that are less than frame size
            
            if size > len(frameElements):
                if page[i] not in frameElements:

                    faultCount = faultCount + 1

                    frameElements.append(page[i])
                        
                        
                    memoryMain.put(page[i])
                    
            # You have a full frame elements now you need to delete
            else:
                # check if the value of page you are about to append is not in memory already
                if page[i] not in frameElements:
                    
                    firtpos = memoryMain.queue[0]
                    memoryMain.get()
                    
                    try:

                        frameElements.remove(firtpos)

                    except:
                        print("Removing error....")
                    
                    frameElements.append(page[i])

                    memoryMain.put(page[i])
                    faultCount = faultCount + 1
    
    return faultCount

''' Replacing the pages using least recently used method
    Meaning you replacement the element that is least used in memory
'''
def LRU(size, page):

    mainMemory = [] * size
    n = 0
    faultCount = 0
    
    # Looping through all the pages
    for p in range(len(page)):

        # Page is not found in n counter is 0
        if mainMemory.count(page[p]) == 0:
            if size > n:
                n = n + 1

                mainMemory.append(page[p])
                faultCount +=1
               
            # main memory is full then you pop the first one to come in main memory
            elif size == n:
                
                mainMemory.pop(0)
                mainMemory.append(page[p])
                faultCount +=1

        # Page is found in n counter is >= 1. 
        else:
            mainMemory.remove(page[p])
            mainMemory.append(page[p])
            
    return faultCount
                
def OPT( size,page):
    ''' Here we do page replacement using the nearest future value that won't be used'''
    mainMemory = [] 
    faultCount = 0
    indexes = [None] * size

    # Loop through each page to insert the pages to memory
    for i in range(len(page)):
        element = page[i]

        #Check if the element is in main memory
        if element not in mainMemory:

            #Check if the we have empty slots in memory
            if len(mainMemory) < size:
                mainMemory.append(element)
                faultCount += 1
                
            # If we have full memory then we do replacement
            else:                

                # Loop through your current main memory values
                for k in range(len(mainMemory)):
                    
                    # Value will not be used again then just replace it
                    if mainMemory[k] not in page[i+1:]:
                        
                        mainMemory[k] = page[i]
                        faultCount +=1
                        break                 

                    # Value will be used again then you need to get the index of all the values 
                    # that will be used again. Save these indexws in an array
                    else:
                        indexes[k] = page[i+1:].index(mainMemory[k])
                # Look for maximum index in the array then replace the memory value with page 
                else:
                    indexReplace = indexes.index(max(indexes))
                    mainMemory[indexReplace] = page[i]  
                    faultCount += 1

    
    return faultCount


def main():
    size = int(sys.argv[1])
    stringArr = ' '.join(str(random.randint(0,9)) for i in range(size))
    
    page = stringArr.split(' ')
    pages = [int(i) for i in page]
    
    
    frameSize = int(input("Enter frame size: "))
    print("Sequence generated", pages)


    print("Page fault for Fifo", FIFO(frameSize, pages))
    
    print("Page fault for LRU", LRU(frameSize, pages))

    print("Page fault for OPT", OPT(frameSize, pages))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of pages]")

    else:

        main()
