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
        self.FromId = -1
        self.ToId = -1
    
    def __str__(self):
        return "Node id: " + str(self.id) + " with code: " + str(self.code) +  "From Node: " + str(self.FromId) + " To Node: " + str(self.ToId)
    

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
        
        while self.solution != self.graph.nodes: #while the solution is different from the candidate set
        #Get the Feasible links for the current solution
            candidates = self.getFeasibleLinks()
            self.UpdateSolution(candidates[0])
            
            #Print partial solution
            self.PrintSolution()
        
        #Return the solution     
        return self.solution
    
    
    def getFeasibleLinks(self):
        candidates = []
        #For each node inside the solution, check to whivh nodes we can move        
        for i in range(len(self.solution)):
            for j in range(len(self.graph.nodes)):
                #You can not move from the node i in the solution to the same node
                if(self.solution[i].id != self.graph.nodes[j].id):
                    #Add Nodes that there are not conected to any other node
                    if(self.graph.nodes[j].FromId == -1 and self.graph.nodes[j].ToId == -1):
                        #cadidate = (cost,i(fromID),j(toID),node)
                        candidateNode = (self.graph.costMatrix[self.solution[i].id][self.graph.nodes[j].id],self.solution[i].id,self.graph.nodes[j].id,self.graph.nodes[j])
                        candidates.append(candidateNode)
                    #Check the nodes that have 1 conection to other node
                    
                    
        
        #Sort the candidates by the cost, puting the minimun cost at the beguining
        candidates.sort(key=lambda x:x[0])
        #Return the sorted list
        print(candidates)
        return candidates


    def UpdateSolution(self,SelectedCandidate):
        #Get the first candidate node (it is the best as far as the list is sorted)and update node links
        self.graph.nodes[SelectedCandidate[1]].ToId = SelectedCandidate[2]
        self.graph.nodes[SelectedCandidate[2]].FromId = SelectedCandidate[1]
        self.totalCost += SelectedCandidate[0]
        #Put the node in the solution
        self.solution.append(SelectedCandidate[3])
        
        
    def PrintSolution(self):
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
        