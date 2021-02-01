
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

