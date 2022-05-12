class Graph: 
    def __init__(self,Instance_dict):
        self.data = Instance_dict
        self.nodes = []
        self.costMatrix = []
        
    def GenerateGraph(self):
        #Generate the "n" nodes, empty, without conections
        #print("Generating nodes...")
        for i in range(0,self.data["n"]):
            node = Node(i,self.data["codes"][i])
            self.nodes.append(node)
        
        #Generate the cost matrix of each code
        for i in range(len(self.data["codes"])):
            costforI = []
            for j in range(len(self.data["codes"])):
                cost = 0
                for z in range(len(self.data["codes"][i])):
                    if self.data["codes"][i][z] != self.data["codes"][j][z]:
                        cost+=1
                costforI.append(cost)
            self.costMatrix.append(costforI.copy())
        
        #Print graph
        #self.PrintGraph()
    
    def PrintGraph(self):
        for i in range(len(self.nodes)):
            print(self.nodes[i])
            
        for i in range(len(self.costMatrix)):
            print(self.costMatrix[i]) 

class Node:
    def __init__(self,ID,OriginalCode):
        self.id = ID
        self.code = OriginalCode
        self.ToId = -1
        self.conections = 0
    
    def __str__(self):
        return "Node id: " + str(self.id) +  " To Node: " + str(self.ToId) + " Conections: " + str(self.conections) + " with code: " + str(self.code)
    

class Solver_Greedy:
    def __init__(self, graphData):
        self.graph = graphData
        self.solution = []
        self.totalCost = 0
    def solve(self):
        #Start form an arbitrary node (first node)
        self.solution.append(self.graph.nodes[0])
        
        totalCost = 0
        #self.getFeasibleLinks()
        
        while len(self.solution) != len(self.graph.nodes): #while the solution is different from the candidate set
            #Print partial solution
            #self.PrintSolution()
            #Get the Feasible links for the current solution
            candidates = self.getFeasibleLinks()
            self.UpdateSolution(candidates[0],False)
            
        
        #Update solution with the last node that have 1 conection
        for i in range(len(self.graph.nodes)):
            if(self.graph.nodes[i].conections == 1): 
                firstNode = self.graph.nodes[i]
                for j in range(len(self.graph.nodes)):
                    if(self.graph.nodes[j].conections == 1 and self.graph.nodes[j] != firstNode):
                        secondNode = self.graph.nodes[j]
                        lastCandidate = (self.graph.costMatrix[self.graph.nodes[i].id][self.graph.nodes[j].id],self.graph.nodes[i].id,self.graph.nodes[j])
                        self.UpdateSolution(lastCandidate,True)
                        break

        #Return the solution 
        print("FINAL SOLUTION FOUND:")
        self.PrintSolution()    
        return self.solution    
    
    def getFeasibleLinks(self):
        candidates = []
        #For each node inside the solution, check to whivh nodes we can move                     
        for i in range(len(self.solution)):
            if(self.solution[i].conections < 2): #check only the nodes in solution that have less than 2 conections
                for j in range(len(self.graph.nodes)):
                    #You can not move from the node i in the solution to the same node
                    if(self.solution[i].id != self.graph.nodes[j].id):
                        #Add Nodes that there are not conected to any other node conections = 0
                        if(self.graph.nodes[j].conections == 0):
                            #cadidate = (cost,i(fromID),j(toID),node)
                            candidateNode = (self.graph.costMatrix[self.solution[i].id][self.graph.nodes[j].id],self.solution[i].id,self.graph.nodes[j])
                            if not candidateNode in candidates:
                                candidates.append(candidateNode)
                        #Check the nodes that have 1 conection to other node
                    
                    
                    
        
        #Sort the candidates by the cost, puting the minimun cost at the beguining
        candidates.sort(key=lambda x:x[0])
        
        #Visualization porpouses
        for i in range(len(candidates)):
            print("Candidate From: " + str(candidates[i][1]) + " To: " + str(candidates[i][2].id) + " Cost: " + str(candidates[i][0]))
        #print(candidates)
        #Return the sorted list
        
        return candidates


    def UpdateSolution(self,SelectedCandidate,IslastCandidate):
        #Get the first candidate node (it is the best as far as the list is sorted)and update node links
        
        for i in range(len(self.graph.nodes)):
            if(self.graph.nodes[i].id == SelectedCandidate[1]):
                self.graph.nodes[i].conections += 1
                SelectedCandidate[2].conections += 1
                #Update Links
                #If solution node (ToId) is -1 -> Update it to the selected graph node
                if(self.graph.nodes[i].ToId == -1):
                    self.graph.nodes[i].ToId = SelectedCandidate[2].id
                #if solution node (toId) != -1 (so it is conected with some other node) -> graph node (toID) is updated to the solution node
                elif(self.graph.nodes[i].ToId != -1):
                    SelectedCandidate[2].ToId = self.graph.nodes[i].id
        
        
        self.totalCost += SelectedCandidate[0]
        #Put the node in the solution
        if(not IslastCandidate):
            self.solution.append(SelectedCandidate[2])
        self.PrintSolution()
        
        
    def PrintSolution(self):
        print("Cost: " + str(self.totalCost))
        for i in range(len(self.solution)):
            print(self.solution[i])
            
            
            
            
            
       
       
       
#LA PRUEBA DE QUE CAMBIANDO UNO DE UNA LISTA SE ACTUALIZA EN LA OTRA TAMBIEN     
#print("Before change:")
#print("Graph: " + str(self.graph.nodes[0]))
#print("Solution: " + str(self.solution[0]))

#self.graph.nodes[0].FromId = 2525
#self.graph.nodes[0].ToId = 2525
#print("After change:")
#print("Graph: " + str(self.graph.nodes[0]))
#print("Solution: " + str(self.solution[0]))
        