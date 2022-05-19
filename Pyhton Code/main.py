from InstanceGenerator import InstanceGenerator
from Greedy import Graph
from Greedy import Solver_Greedy
from Grasp import Solver_Grasp
from LocalSearch import Heuristic_LocalSearch
import time


############## Configuration of Instance Generator################
#Number of instances that will be generated
numInstances = 1
# Minimum number of codes 
min_n = 99
#Maximum number of codes
max_n = 100
#number of digits of each code
m = 10

###################CONFIGURATION################
#Bool if you want to generate instances or not
GenerateInstances = False #True generates new instances and overwrites existing ones.
InstancesFolder = "Instances/"
InstanceName = "Instance_1.json" #The name of the instance file you want to load.
runSolver = True #True runs the solver
solver = "GREEDY" #Available: "GREEDY" // "GRASP"
alphaValue = 0.7 #Only usefull if GRASP is selected as solver
doLocalSearch = True #True if you want to apply local search
maxRunningTime = 60 #Only used in grasp+localsearch
reportTime = 10 #when to report current best solution


def main():
    
    InstanceGen = InstanceGenerator(numInstances,min_n, max_n,m)
    if(GenerateInstances):
        InstanceGen.GenerateInstances(randomInstances=True,n1=5,n2=25) #Change this to True if you want random instances between min_n and max_n number of codes
                                                             #False will create instances with numInstances*10 (10,20,30...) number of codes
       
    if runSolver:
        print("--Reading data--")
        #Get the dictionari with the data form the instance
        Instance_data = InstanceGen.ReadInstance(InstancesFolder + InstanceName)
        
        InstanceGraph = Graph(Instance_data)
        InstanceGraph.GenerateGraph()
        start_time = time.time()
        #Call the solver with the Graph data constructed
        print("--Running solver--")
        if solver == "GREEDY":
            Greedy = Solver_Greedy(InstanceGraph)
            greedy_feasibleSolution = Greedy.solve()
            if(doLocalSearch):
                ls = Heuristic_LocalSearch(greedy_feasibleSolution,Greedy.graph.costMatrix)
                ls.doLocalSearch()
                print(f"Greedy + Local Search execution time: {time.time() - start_time}")
                ls.PrintSolution()
            else: 
                print(f"Greedy execution time: {time.time() - start_time}")
                Greedy.PrintSolution()
        elif solver == "GRASP":
            bestFoundCost=float('inf')
            bestSolution=None
            i=0
            while((time.time()-start_time)<maxRunningTime):
                Grasp = Solver_Grasp(InstanceGraph, alphaValue)
                grasp_feasibleSolution = Grasp.solve()
                if(doLocalSearch):
                    ls = Heuristic_LocalSearch(grasp_feasibleSolution,Grasp.graph.costMatrix)
                    ls.doLocalSearch()
                    if(ls.totalCost<bestFoundCost):
                        print("##########- New better Solution found in grasp -##########")
                        ls.PrintSolution()
                        bestFoundCost=ls.totalCost
                        bestSolution=ls
                    #Report every X seconds
                    if(((time.time()-start_time)/reportTime)>i):
                        i=i+1
                        print(f'Time:{int(time.time()-start_time)} - Best solution so far:{bestSolution.totalCost}')

            print("Solution after timeout")
            bestSolution.PrintSolution()

        end_time = time.time()
        print(f'-- Solving time {(end_time - start_time)} seconds ---') #nanosecond precision is dependant on architecture, so solving time can be show as 0.0 sometimes
    
main()