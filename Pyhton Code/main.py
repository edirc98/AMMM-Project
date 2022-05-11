from InstanceGenerator import InstanceGenerator

############## Configuration of Instance Generator################
#Number of instances that will be generated
numInstances = 4
# Minimum number of codes 
min_n = 3
#Maximum number of codes
max_n = 5
#Minumum lenght of each code
min_m = 2
#Maximum lenght of each code
max_m = 5

###################CONFIGURATION################
#Bool if you want to generate instances or not
GenerateInstanes = False
InstancesFolder = "Instances/"
InstanceName = "Instance_0.json"
solver = "GREEDY" #Available: "GREEDY" // "GRASP"

def main():
    InstanceGen = InstanceGenerator(numInstances,min_n, max_n, min_m,max_m)
    if(GenerateInstanes):
        InstanceGen.GenerateInstances()
    
    InstanceGen.ReadInstance(InstancesFolder + InstanceName)
    
    


main()