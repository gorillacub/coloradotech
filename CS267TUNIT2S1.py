import random

#create random number generator
def randNum():
    #initialize array
    numLst = []
    #generate 1000 random numbers
    for randNum in range (1000):
       numLst = random.randint(1,10000)
       return(numLst)
       
# create partition/pivot to divide and conquer
def partition(numLst,low,high):
    i = (low -1)
    pivot = numLst[high]
    for j in range(low, high):
        if numLst[j] <= pivot:
            i +=1
            numLst[i], numLst[j] = numLst[j], numLst[i]
    numLst[i+1], numLst[high] = numLst[high], numLst[i+1]
    return(i+1)

# quicksort function to sort list
def quickSort(numLst, low, high):
    if low < high:
        z = partition(numLst, low, high)
        quickSort(numLst, low, z-1)
        quickSort(numLst, z+1, high)
        
        
myLst = []
size = 1000
#loop to append 1000 numbers in myLst[]
for i in range(size):
    elements = randNum()
    myLst.append(elements)


low = 0
high = len(myLst) - 1
quickSort(myLst, low, high)
print(myLst)
