from random import randint, sample
from itertools import chain, combinations
from time import time

class SSP():
    def __init__(self, S=[], t=0): #S=[] is the Set, T is the target
        self.S = S #giving S set name self.S
        self.t = t #gives t set name self.t
        self.n = len(S) #self.n gives length S
        #
        self.decision = False #Decision set to False at start
        self.total    = 0
        self.selected = []

    def __repr__(self): #converts everything to a string
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    
    def random_instance(self, n, bitlength=10): #Generates random numbers
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True) #Sorts set highest to lowest
        self.t = randint(0,n*max_n_bit_number) #Target can be any number
        self.n = len( self.S ) #Randomly sets length of Set S

    def random_yes_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = sum( sample(self.S, randint(0,n)) ) 
        self.n = len( self.S )

    ###

    def try_at_random(self): 
        candidate = []
        total = 0 
        while total != self.t: #Whilst the sum of the set doesn't equal the total...
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate) #Works out total sum of set
            print( "Trying: ", candidate, ", sum:", total ) #displays sums being caculated.
            

instance = SSP()
instance.random_yes_instance(4) #Sets S to be length 4
print( instance ) #Displays set

instance.try_at_random() #Displays random set and total
