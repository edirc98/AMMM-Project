from pyexpat.errors import codes
import random 


class InstanceGenerator:
    
    def __init__(self, NumInstances,Min_n,Max_n,Min_m,Max_m):
        self.min_n = Min_n
        self.max_n = Max_n
        self.min_m = Min_m
        self.max_m = Max_m
        
        self.numInstances = NumInstances
        self.codes = []
        self.code = []
    
    def GenerateInstance(self,n,m):
        #Make sure firts code is 0...0
        for i in range(0,m):
            self.code.append(0)
        self.codes.append(self.code.copy())
        self.code.clear()
        #Generate the rest of the codes
        for i in range(1,n):
            valid = False
            self.code.clear()
            while valid == False:
                tmpCode = []
                for j in range (0,m):
                    #Gerate Code of 0s and 1s
                    digit = random.randint(0,1)
                    self.code.append(digit)
                    
                if not self.code in self.codes:
                    #valid code
                    self.codes.append(self.code.copy())
                    self.code.clear()
                    valid = True
              
    def GenerateInstances(numInstances,min_n, max_n,min_m,max_m):
        for i in range(0,numInstances):
            #create combinations of n and m
            n = random.randint(min_n,max_n)
            m = random.randint(min_m,max_m)
            if (2^m < n):
                InstanceGenerator.GenerateInstance(n,m)
                #Put the instance to a .json file
                #TODO