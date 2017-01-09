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

    def exhaustive(self):
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
instance.exhaustive()
print( instance )
       

start_time = time.time()

print instance.exhaustive()
print("--- %s seconds ---" % (time.time() - start_time))
