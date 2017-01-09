import random
import math
from random import randint, sample
from itertools import chain, combinations
import time
class SSP():
    def __init__(self, S=[], t=0):
        self.S = S
        self.t = t
        self.n = len(S)
    #
        self.decision = False
        self.total    = 0
        self.selected = []
    def __repr__(self):
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    def random_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = randint(0,n*max_n_bit_number)
        self.n = len( self.S )
    def random_yes_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = sum( sample(self.S, randint(0,n)) )
        self.n = len( self.S )
    def grasp(self, max_repetition=100):
        best_candidate = 0
        for i in range (0, max_repetition):
            greedy_candidate = self.ConstructGreedyRandomizedSolution()
            grasp_candidate = self.LocalSearch(greedy_candidate)
            if math.fabs(self.t - grasp_candidate) <= math.fabs(self.t - greedy_candidate): 
                best_candidate = grasp_candidate
            print "greedy", greedy_candidate
            print "grasp", grasp_candidate
            print "best", best_candidate
            if best_candidate == self.t:
                return best_candidate
        return best_candidate
    def ConstructGreedyRandomizedSolution(self):
        total=0
        self.selected =[0 for i in range(self.n)]
        nums = [x for x in range(self.n)]
        random.shuffle(nums)
        for i in nums:
            if (self.S[i]<=self.t-total):
                total=total+self.S[i]
                self.selected[i] = 1
        
        return total
    def LocalSearch(self, candidate):
        ind1 = [i for i,x in enumerate(self.selected) if x == 1]
        for i in ind1:
            if candidate == self.t:
                 return candidate
            ind0= [i for i, x in enumerate(self.selected) if (x == 0 and self.t-candidate<=self.S[i])]
            if len(ind0)>0:
                k=max(i for i,x in enumerate(ind0))
                self.selected[k] = 1
                self.selected[i] = 0
                candidate=candidate-self.selected[i]
                candidate=candidate+self.selected[k]
        
        return candidate
n=10     
instance = SSP()
instance.random_yes_instance(n)
p=instance.grasp()

print p
print instance

    

