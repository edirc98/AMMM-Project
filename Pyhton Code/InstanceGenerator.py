import json
import random 
import os

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
                for j in range (0,m):
                    #Gerate Code of 0s and 1s
                    digit = random.randint(0,1)
                    self.code.append(digit)
                    
                if not self.code in self.codes:
                    #valid code
                    self.codes.append(self.code.copy())
                    self.code.clear()
                    valid = True
                else: self.code.clear()
              
    def GenerateInstances(self):
        for i in range(0,self.numInstances):
            #create combinations of n and m
            validCombination = False
            
            while validCombination == False:
                n = random.randint(self.min_n,self.max_n)
                m = random.randint(self.min_m,self.max_m)
                #Number of posible combinations of binary digits of lenght m > that n codes that can be generated
                if ((2^m) > n):
                    print("Generating instance with: n = " + str(n) + " m = " + str(m))
                    validCombination = True
                    InstanceGenerator.GenerateInstance(self,n,m)
                    filename = "Instance_" + str(i)
                    self.SaveInstanceToJson(n,m,filename)
                    self.SaveInstanceToDat(n,m,filename)
                    # clear the codes that just generated for the next one
                    self.codes.clear()
                    
    def SaveInstanceToJson(self,n,m,filename):
        #Put the instance to a .json file
        instanceDict = {
            "n": n,
            "m": m,
            "codes": self.codes
        }
        #Create the dictionari with the instance data
        json_data = json.dumps(instanceDict)
        
        #Create the path where the files will be stored if do not exists
        path = 'Instances/'
        if not os.path.exists(path):
            os.makedirs(path)

        #Create the file and write it to the corresponding.json
        filename = filename + ".json"
        with open(path+filename, 'w') as outfile:
            json.dump(json_data, outfile)

    def SaveInstanceToDat(self,n,m,filename):
        # Create the path where the files will be stored if do not exists
        path = 'Instances/'
        if not os.path.exists(path):
            os.makedirs(path)

        # Create the file and write it to the corresponding.dat
        filename = filename + ".dat"
        with open(path + filename, 'w') as outfile:
            outfile.write("m = %s;\n" % str(m))
            outfile.write("n = %s;\n" % str(n))
            outfile.write("S = \n[\n")
            for code in self.codes:
                outfile.write("\t[")
                for value in code:
                    outfile.write(" %s" % str(value))
                outfile.write(" ]\n")
            outfile.write("];\n")


    def ReadInstance(self, InstanceFile):
        with open(InstanceFile) as json_file:
            json_string = json.load(json_file)
            data_dict = json.loads(json_string)
            return data_dict
          
    def PrintCodes(self):
        print(self.codes)
            
                    
                    