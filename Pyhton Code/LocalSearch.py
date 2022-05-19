
import copy


class Heuristic_LocalSearch:
    def __init__(self,Feasible_Solution,Cost_Matrix):
        self.solution = Feasible_Solution
        self.costMatrix = Cost_Matrix
        self.totalCost = self.getCost(self.solution)
        self.i = 0
        self.j = 0
    
    
    #2-edge exchange or (2-opt) heuristic
    def doLocalSearch(self):
        #Check all posible combinations of two nodes( going from node i to node j)
        while self.i < len(self.solution):
            while self.j < len(self.solution):
                #First avoid combinations of node with itself, as cost is 0
                if self.i != self.j:
                    #Check if the combination of nodes to exchange is usefull or not
                    #If the cost of the actual path is lower that the new path, it is NOT usefull
                    #Special cases when i is 0 or j is len
                    if self.i == 0:
                        if self.j == (len(self.solution)-1):
                            self.computeExchange(self.i,self.j,-1,0)
                        else:
                            self.computeExchange(self.i,self.j,-1,self.j+1) #What happens here
                    elif self.j == (len(self.solution)-1):
                        if self.i == 0: 
                            self.computeExchange(self.i,self.j,-1,0)
                        else: 
                            self.computeExchange(self.i,self.j,self.i-1,0)
                    else: 
                        self.computeExchange(self.i,self.j,self.i-1,self.j+1)
                self.j += 1
            self.j = 0
            self.i += 1
            
        #print("Ended local search. ")
        #print("Best solution founded is: ")
        #self.PrintSolution()
        #for self.i in range(len(self.solution)):
            #for self.j in range(len(self.solution)):
                
    def computeExchange(self, i,j,mi,pj):
        actualCost = self.costMatrix[self.solution[mi].id][self.solution[i].id] + self.costMatrix[self.solution[j].id][self.solution[pj].id] 
        exchangeCost = self.costMatrix[self.solution[mi].id][self.solution[j].id] + self.costMatrix[self.solution[i].id][self.solution[pj].id]
        if actualCost > exchangeCost: 
            self.checkSolution(i,j)
        
    def checkSolution(self,i,j):
        #print("Testing posible better solution...")
        #testingSolution = copy.deepcopy(self.solution)
        #Get the part of the solution between i and j and reverse it
        if i < j:
            self.solution[i:j] = reversed(self.solution[i:j])
        elif j < i: 
            self.solution[j:i] = reversed(self.solution[j:i])
        
        #relink ToId of the nodes
        for i in range(len(self.solution)):
            if i == (len(self.solution)-1):
                self.solution[i].ToId = self.solution[0].id
            else: 
                self.solution[i].ToId = self.solution[i+1].id        
        testingSolutionCost = self.getCost(self.solution)
        
        #First improvement procedure
        if(testingSolutionCost < self.totalCost):
            self.totalCost = testingSolutionCost
            #self.solution = testingSolution
            #print(f'##########- New better Solution found in localsearch with cost {self.totalCost}-##########')
            #Restart the while loops for start searching again
            self.i = 0
            self.j = 0  
        else:
            if i < j:
                self.solution[i:j] = reversed(self.solution[i:j])
            elif j < i: 
                self.solution[j:i] = reversed(self.solution[j:i])
        
            #relink ToId of the nodes
            for i in range(len(self.solution)):
                if i == (len(self.solution)-1):
                    self.solution[i].ToId = self.solution[0].id
                else: 
                    self.solution[i].ToId = self.solution[i+1].id        
            testingSolutionCost = self.getCost(self.solution)
            
    
    def getCost(self,solution):
        tourCost = 0
        for i in range(len(solution)):
            tourCost += self.costMatrix[solution[i].id][solution[i].ToId]
        return tourCost
       
    def PrintSolution(self):
        print("Cost: " + str(self.totalCost))
        for i in range(len(self.solution)):
            print(self.solution[i])
                           
                        