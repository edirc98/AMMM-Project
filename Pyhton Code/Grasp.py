from Greedy import Node
from Greedy import Graph
import random

class Solver_Grasp:
    def __init__(self,graphData,AlphaValue):
        self.graph = graphData
        self.alpha = AlphaValue
        self.solution = []
        self.totalCost = 0
    def solve(self):
        #Start form an arbitrary node (first node)
        self.solution.append(self.graph.nodes[0])
    
        while len(self.solution) != len(self.graph.nodes): #while the solution is different from the candidate set
            #Print partial solution
            #self.PrintSolution()
            #Get the Feasible links for the current solution
            candidates = self.getFeasibleLinks()
            #Compute the posible random candidates to be chosen
            q_min = candidates[0][0]
            q_max = candidates[-1][0]
            q_candidate = int(q_min + self.alpha*(q_max-q_min))
            stopIndex = 0
            for i in range(len(candidates)):
                if candidates[i][0]>q_candidate:
                    stopIndex = i
                    break
            #To make sure that at least gets the first element in the slicing and do not happens [0:0]
            if stopIndex == 0: 
                stopIndex = 1
            candidates = candidates[0:stopIndex]
                
            #print("Max Q: " + str(q_candidate))
            #print("Sliced Candidates: ")
            #print(candidates)
                        
            #Chose the random candidate
            selectedCandidate = random.choice(candidates)
            self.UpdateSolution(selectedCandidate,False)
            
        
        #Update solution with the last node that have 1 conection
        for i in range(len(self.graph.nodes)):
            if(self.graph.nodes[i].conections == 1): 
                firstNode = self.graph.nodes[i]
                for j in range(len(self.graph.nodes)):
                    if(self.graph.nodes[j].conections == 1 and self.graph.nodes[j] != firstNode):
                        #secondNode = self.graph.nodes[j]
                        lastCandidate = (self.graph.costMatrix[self.graph.nodes[i].id][self.graph.nodes[j].id],self.graph.nodes[i].id,self.graph.nodes[j])
                        self.UpdateSolution(lastCandidate,True)
                        break
        #Compute the cost of the solution
        self.totalCost = self.getCost()
        #Return the solution 
        print("FINAL SOLUTION FOUND:")
        orderedSolution = self.SortSolution()
        self.solution = orderedSolution
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
                            
        #Sort the candidates by the cost, puting the minimun cost at the beguining
        candidates.sort(key=lambda x:x[0])
        
        #Visualization porpouses
        #for i in range(len(candidates)):
            #print("Candidate From: " + str(candidates[i][1]) + " To: " + str(candidates[i][2].id) + " Cost: " + str(candidates[i][0]))
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
        
        #Put the node in the solution
        if(not IslastCandidate):
            self.solution.append(SelectedCandidate[2])
        #self.PrintSolution()
        
        
    def getCost(self):
        totalCost = 0
        for i in range(len(self.solution)):
            totalCost += self.graph.costMatrix[self.solution[i].id][self.solution[i].ToId]
        return totalCost
        
    def SortSolution(self):
        OrderedSolution = []
        OrderedSolution.append(self.solution[0])
        
        for node in OrderedSolution:
            for i in range(len(self.solution)):
                if len(self.solution) == len(OrderedSolution):
                    break
                if self.solution[i].id == node.ToId:
                    OrderedSolution.append(self.solution[i])
        
        return OrderedSolution
    
    def PrintSolution(self):
        print("Cost: " + str(self.totalCost))
        for i in range(len(self.solution)):
            print(self.solution[i])



        