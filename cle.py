import random
import numpy as np
import gym
from gym import spaces
from gym.utils import seeding

class EEN():
	ni=no=0
	arr={}
	state={}
	params={}
	lss=[]
	lso=[]
	outp={}
	reseop = [] 
	resein = []	

	def enter_inputs(self):
		self.ni=(int(input("Enter the number of inputs ")))
		self.no= (int(input("Enter the number of outputs ")))

	def enter_ranges(self):
		for i in range(self.ni):
			lst=[]
			pp = input("Enter the parameter name: ")
			self.lss.append(pp)
			p1 = float(input("Enter the lower range: "))		
			p2 = float(input("Enter the upper range: "))
			lst.append(p1)
			lst.append(p2)
			print(lst)
			self.arr[pp]=lst
		print("Output ")
		for i in range(self.no):
			lst1=[]
			op = input("Enter the output name ")
			self.lso.append(op)
			opval = float(input("Enter the value: "))
			p1 = float(input("Enter the lower range: "))		
			p2 = float(input("Enter the upper range: "))
			lst1.append(opval)
			lst1.append(p1)
			lst1.append(p2)
			print(lst1)
			self.outp[op]=lst1
		print("All the inputs with ranges are ",self.arr)
		print("All the initial states are ",self.state)
		print("pp lss ", self.lss, "lso ", self.lso)
		print("outp ", self.outp)


	def initi_states(self):
		print(len(self.lso))
		for i in range(len(self.lso)):
			self.state[self.lso[i]]=random.uniform(self.outp[self.lso[i]][0],self.outp[self.lso[i]][1])
			self.reseop.append(self.state[self.lso[i]])
		for i in range(len(self.lss)):
			self.params[self.lss[i]]=random.uniform(self.arr[self.lss[i]][0],self.arr[self.lss[i]][1])
			self.resein.append(self.params[self.lss[i]])
		print("The initialized states are ", self.state)
		print("The initialized paramss are ", self.params)

	"""csv_file = "arr_list.csv"
	try:
    		with open(csv_file, 'w') as csvfile:
        	writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        	writer.writeheader()
        	for data in dict_data:
            		writer.writerow(data)
	except IOError:
    		print("I/O error") """

e1 = EEN()
p = e1.enter_inputs()
e1.enter_ranges()
e1.initi_states()
