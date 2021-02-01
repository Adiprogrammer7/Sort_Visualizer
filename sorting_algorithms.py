
def swap(li, i, j):
	li[i], li[j] = li[j], li[i]

def BubbleSort(li):
	swapped = False #flag in case if list is already sorted.
	for i in range(len(li) - 1):
		for j in range(len(li) - 1 - i):
			if li[j] > li[j + 1]:
				swap(li, j, j+1)
				swapped = True
				yield li #so that any update in data can be visualized at each iteration.
		if not swapped:  #when list is already sorted.
			break

def MergeSort(li, low, high):
	if high <= low:
		return
	mid = (low+high)//2
	yield from MergeSort(li, low, mid)
	yield from MergeSort(li, mid+1, high)
	yield from merge(li, low, mid, high)
	yield li

def merge(li, low, mid, high):
	merged_li = []
	left_start = low
	right_start = mid+1
	# going through two chunks of data and merging on sort.
	while left_start <= mid and right_start <= high:
		if li[left_start] < li[right_start]:
			merged_li.append(li[left_start])
			left_start += 1
		else:
			merged_li.append(li[right_start])			
			right_start += 1
	# for remaining elements from left chunk
	while left_start <= mid:
		merged_li.append(li[left_start])
		left_start += 1
	# for remaining elements from right chunk
	while right_start <= high:
		merged_li.append(li[right_start])
		right_start += 1
	for i, j in enumerate(merged_li):
		li[low + i] = j
		yield li
