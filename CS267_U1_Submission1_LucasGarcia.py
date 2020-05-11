import timeit


def bubble_sort():
	length = len(sampleArray)
	for i in range(length):
		for j in range(length - i -1):
			if sampleArray[j] > sampleArray[j + 1]:
				sampleArray[j], sampleArray[j+1] = sampleArray[j+1], sampleArray[j]

def selection_sort(sampleArray2):
	for i in range(len(sampleArray2)):
		low_val = i
		for j in range(i + 1, len(sampleArray2)):
			if sampleArray2[j] < sampleArray2[low_val]:
				low_val = j
		sampleArray2[i], sampleArray2[low_val] = sampleArray2[low_val], sampleArray2[i]
		
#create sample list
sampleArray = [100, 45, 33, 55, 356, 11, 1000, 999, 987]
sampleArray2 = [100, 45, 33, 55, 356, 11, 1000, 999, 987]
selection_sort(sampleArray2)
print(sampleArray2)
bubble_sort()
for k in range(len(sampleArray)):
	print(sampleArray[k])
	
# compute bubble sort execution time
def bubble_time():
	BUBBLE_CODE = 'from __main__ import bubble_sort'
	times = timeit.timeit(setup = BUBBLE_CODE, number = 1)
	print('Bubble sort execution time: {}'.format(times))
	
#compute selection sort execution time
def selection_time():
	SELECTION_CODE = 'from __main__ import selection_sort'
	times2 = timeit.timeit(setup = SELECTION_CODE, number = 1)
	print('Selection sort execution time: {}'.format(times2))
	


def compare_times():
	BUBBLE_TIME = 'from __main__ import bubble_time'
	SELCTION_TIME = 'from __main__ import selection_time'
	if BUBBLE_TIME < SELCTION_TIME:
		print('Bubble sort is faster')
	else:
		print('Selection sort is faster')

if __name__ =='__main__':
	bubble_time()
	selection_time()
	compare_times()