
class Heuristic_LocalSearch:
    def __init__(self,Feasible_Solution,Cost_Matrix):
        self.solution = Feasible_Solution
        self.costMatrix = Cost_Matrix
        self.totalCost = self.getCost(self.solution)
        self.bestSolution = []
    
    
    #2-edge exchange or (2-opt) heuristic
    def doLocalSearch(self):
        #print (self.costMatrix)
        #Check all posible combinations of two nodes( going from node i to node j)
        for i in range(len(self.solution)):
            for j in range(len(self.solution)):
                #First avoid combinations of node with itself, as cost is 0
                if i != j:
                    #Check if the combination of nodes to exchange is usefull or not
                    #If the cost of the actual path is lower that the new path, it is NOT usefull
                    #Special cases when i is 0 or j is len
                    if i == 0:
                        if j == (len(self.solution)-1):
                            self.computeExchange(i,j,-1,0)
                        else:
                            self.computeExchange(i,j,-1,j+1) #What happens here
                    elif j == (len(self.solution)-1):
                        if i == 0: 
                            self.computeExchange(i,j,-1,0)
                        else: 
                            self.computeExchange(i,j,i-1,0)
                    else: 
                        self.computeExchange(i,j,i-1,j+1)
                        
        print("Ended local search. ")
        print("Best solution founded is: ")
        self.PrintSolution()
                            

    def computeExchange(self, i,j,mi,pj):
        actualCost = self.costMatrix[self.solution[mi].id][self.solution[i].id] + self.costMatrix[self.solution[j].id][self.solution[pj].id] 
        exchangeCost = self.costMatrix[self.solution[mi].id][self.solution[j].id] + self.costMatrix[self.solution[i].id][self.solution[pj].id]
        if actualCost > exchangeCost: 
            self.checkSolution(i,j)
        
    def checkSolution(self,i,j):
        testingSolution = self.solution
        #Get the part of the solution between i and j and reverse it
        if i < j:
            testingSolution[i:j] = reversed(testingSolution[i:j])
        elif j < i: 
            testingSolution[j:i] = reversed(testingSolution[j:i])
        
        #relink ToId of the nodes
        for i in range(len(testingSolution)):
            if i == (len(testingSolution)-1):
                testingSolution[i].ToId = testingSolution[0].id
            else: 
                testingSolution[i].ToId = testingSolution[i+1].id
        
        
        testingSolutionCost = self.getCost(testingSolution)
        if(testingSolutionCost < self.totalCost):
            print("New Solution found")    
            self.totalCost = testingSolutionCost
            self.solution = testingSolution
            #self.PrintSolution()
    
    
    def getCost(self,solution):
        tourCost = 0
        for i in range(len(solution)):
            tourCost += self.costMatrix[solution[i].id][solution[i].ToId]
        return tourCost
       
       
    def PrintSolution(self):
        print("Cost: " + str(self.totalCost))
        for i in range(len(self.solution)):
            print(self.solution[i])
                           
                        