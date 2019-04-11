import numpy as np
from cle import EEN
import random
import gym
from gym import spaces
from gym.utils import seeding


"""The action is to increment or decrement the value"""
class MultiAgent():
	def __init__(self):
		print("entered init ")
		self.ni=EEN.ni
		self.no=EEN.no
		self.arr=EEN.arr
		self.state=EEN.state
		self.params=EEN.params
		self.lss=EEN.lss
		self.lso=EEN.lso
		self.outp=EEN.outp
		self.reseop = EEN.reseop 
		self.resein = EEN.resein

		self.val =abs(outp[r][0]-(self.params[0]/self.params[1])) #Should be done dynamically instead of static, needs to be improved
		lows=[]
		highs=[]
		for i in range(EEN.ni):
			lows = self.arr[i][0]
			highs = self.arr[i][1]
		losw = np.asarray(lows, dtype = np.float32, order = None)
		hihgs = np.asarray(highs, dtype = np.float32, order = None)
		self.observation_space = spaces.Box(low=losw, high=hihgs, dtype = np.float32)
		print(self.observation_space)
		self.action_space = spaces.Discrete(2) 

	def do_action(self,action):
		for i in range(len(self.params)):
			self.params[i] = self.params[i]+action[i]

	def step(self,action):
		flag=1
		assert self.action_space.contains(action),"%r (%s) invalid:" % (action, type(action))	
		for i in range(len(self.params)):
			if self.params[i][0]>=(self.params[i]+action[i]) or (self.params[i]+action[i])>=self.params[i][1]:
				print("Any of the value getting put of the range ")
				flag=0
				break
		if flag ==1:
			do_action(action)
		elif flag==0:
			print("cant perform action this time ")

		self.state = (self.params[0]/self.params[1])
		ouput = abs(outp[0][0]-self.state) #here in outp[r][0] should be there...do necessary changes, needs to be improved

		if ouput<self.val:
			reward = reward+1
		elif ouput>self.val:
			reward = reward-1
		else:
			reward+0.5
		
		
return np.array(self.state), reward, done, {}

	def reset(self):
		self.state = self.reseop
		self.params = self.resein
		print("states params ", self.state, self.params)
		

	def init_inop():
		EEN.initi_states()
		self.state=EEN.state
		self.params=EEN.params
	lows = []
	highs = []
m1 = MultiAgent()
m1.reset()
