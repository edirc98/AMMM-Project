from InstanceGenerator import InstanceGenerator
from Greedy import Graph
from Greedy import Solver_Greedy

############## Configuration of Instance Generator################
#Number of instances that will be generated
numInstances = 5
# Minimum number of codes 
min_n = 10
#Maximum number of codes
max_n = 20
#Minumum lenght of each code
min_m = 5
#Maximum lenght of each code
max_m = 10

###################CONFIGURATION################
#Bool if you want to generate instances or not
GenerateInstanes = True
InstancesFolder = "Instances/"
InstanceName = "Instance_0.json"
runSolver = False #Change this if you only want to generate instances and do not run the solver
solver = "GREEDY" #Available: "GREEDY" // "GRASP"

def main():
    if(GenerateInstanes):
        InstanceGen = InstanceGenerator(numInstances,min_n, max_n, min_m,max_m)
        InstanceGen.GenerateInstances()
       
    if runSolver: 
        #Get the dictionari with the data form the instance
        Instance_data = InstanceGen.ReadInstance(InstancesFolder + InstanceName)
        
        InstanceGraph = Graph(Instance_data)
        InstanceGraph.GenerateGraph()
        
        #Call the solver with the Graph data constructed
        if solver == "GREEDY":
            Greedy = Solver_Greedy(InstanceGraph)
            Greedy.solve()
        elif solver == "GRASP":
            #TODO Implement GRASP
            pass
    
    


main()