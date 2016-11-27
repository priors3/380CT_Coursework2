from random import randint, sample
from itertools import chain, combinations
from time import time
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

    def positiveSubsetSum(self):
    # preliminary
        if self.t < 0 or self.t > sum(self.S): # T = sum(S)
          return False
 
        # algorithm
        sub_sum = [False] * (self.t + 1 )
        sub_sum[0] = True
        p = 0
        while not sub_sum[self.t] and p < self.n:
          a = self.S[p]
          q = self.t
          while not sub_sum[self.t] and q >= a:
            if not sub_sum[q] and sub_sum[q - a]:
              sub_sum[q] = True
            q -= 1
          p += 1
        return sub_sum[self.t]        

    def subset(self):
        result = []
        def find(arr,t, path=()):
            if not arr:
                return
            if arr[0] == t:
                result.append(path + (arr[0],))
            else:
                find(arr[1:], t - arr[0], path + (arr[0],))
                find(arr[1:], t, path)
        find(self.S, self.t)
        return result
instance = SSP()
instance.random_yes_instance(5)
instance.subset()
print( instance )
       

start_time = time.time()

print instance.positiveSubsetSum()
print("--- %s seconds ---" % (time.time() - start_time))
print "----------------------------------------------------"
print instance.subset()
print("--- %s seconds ---" % (time.time() - start_time))
