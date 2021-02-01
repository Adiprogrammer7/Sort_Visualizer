import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sorting_algorithms import BubbleSort
import sys
import random

# when this file is itself is ran, not by importing.
if __name__ == '__main__':
	li = []
	step_cnt = 0 
	try:
		N = int(input("Enter no. of elements to be sorted: "))
		choice = int(input("Choice(1:select randomly, 2:input manually): "))
		if choice == 1:
			li = random.sample(range(0, 2*N), N) #selects N random nums from range(0, 2N)
		elif choice == 2:
			for i in range(N):
				num = input("Enter {}th element: ".format(i+1))
				li.append(int(num))
		else:
			sys.exit("Invalid input!")

		algo_dict = {1:'Bubble Sort', 2:'Merge Sort'}
		algo = int(input('Sorting Algorithm{}: '.format(algo_dict)))
		if algo == 1:
			generator_func = BubbleSort(li)
		else:
			sys.exit("Invalid input!")

	except Exception as e:
		raise e

	# plot configurations
	fig, ax = plt.subplots(num= 'Sorting Algorithm Visualizer')
	ax.set_title(algo_dict[algo])
	plt.xlabel('Elements being sorted')
	bar_rec = ax.bar(range(len(li)), li, tick_label=li)  #container for bar diagram.
	# by using plt.gcf().transFigure, (0,0) is the bottom left and (1,1) is the top right of the figure
	plt.text(0.015, 0.94, 'input:{}'.format(str(li)), fontsize=10, transform=plt.gcf().transFigure) #to show input data
	step_text = plt.text(0.015, 0.90, "", fontsize=10, transform=plt.gcf().transFigure) #to show no. steps

	def update_fig(li):
		global step_cnt
		for rect, val in zip(bar_rec, li):
			rect.set_height(val)
			ax.set_xticklabels(li) #also changing xticks labels to match with changing bars.
		# to update step count
		step_cnt += 1
		step_text.set_text('No. of steps: {}'.format(step_cnt))

	# at each 'frames' it calls 'func' function, which then modifies the plot based on 'li' at that time.
	anim = animation.FuncAnimation(fig, func=update_fig, frames=generator_func, interval=200, repeat=False)
	plt.show()

	# In abstract, above animation stuff kinda working like this.
	# for i in QuickSort(li):
	# 	for rect, j in zip(bar_rec, li):
	# 		rect.set_height(j)
	# 		ax.set_xticklabels(li)
	# 		fig.canvas.draw()
	# 		plt.pause(0.0001)		
	# plt.show()