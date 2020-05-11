import random

#create random number generator to create 1000 randum numbers
def randNum():
    #initialize array
    numLst = []
    #generate 1000 random numbers
    for randNum in range (1000):
       numLst = random.randint(1,10000)
       return(numLst)


#Create rand number generator to create a single element and store it in the search value
def singleRandNum():
    #initialize search value
    searchVal = []
    #generate random element and store in searchVal
    for singleRandNum in range (1):
        searchVal = random.randint(1,10000)
        print(searchVal)

# binary search function
def binary_search(numLst, length, searchVal):
    start = 0
    end = length - 1
    while start <= end:
        mid = int((start + end)/2)
        if searchVal == numLst[mid]:
            print("\nRandom number $d is present at position %d" %(searchVal, mid))
            return -1
        elif searchVal < numLst[mid]:
            end = mid - 1
        elif searchVal > numLst[mid]:
            start = mid + 1
    print("\nsearchVal not found")
    return -1

singleRandNum()
#randNum()

#myLst = []
#size = 1000
#loop to append 1000 numbers in myLst[]
#for i in range(size):
    #elements = randNum()
    #myLst.append(elements)

#x = singleRandNum()
#binary_search(myLst, size, x)