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
    def random_instance(self, n, bitlength=8):
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

    def subsetsum(self):
        def sum1 (array,n, num):
            if (num == 0):
                 return True
            if (n == 0 and num != 0):
                 return False
            if array[n-1] > num:
                    return sum1(array, n-1, num)
            return sum1(array, n-1, num) or sum1(array,n-1, num- array[n-1])
        return sum1(self.S, self.n, self.t)

    def try_at_random(self):
        candidate = []
        total = 0
        while total != self.t:
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )

    def greedy(self):
        for j in range (0, self.n):
            sum=0
            for i in range (j,self.n):
                if self.t==0:
                    return False
                if self.S[i]==self.t:
                    return True          
                if (self.S[i]<=self.t-sum):
                    sum=sum+self.S[i]
                    if sum == self.t:
                          return True  
                                   
        return False
          
instance = SSP()


for n in range(10,20):
    
    instance.random_instance(n)
    start_time = time.time()
    #print instance.subsetsum()
    print instance.greedy()
    for i in range(1):
        ("%d\t%6f" % (n,(time.time() - start_time)/100))
    print "----------------------------------------------------"
    
    print("--- %s seconds ---" % (time.time() - start_time))
