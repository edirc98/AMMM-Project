class Graph: 
    def __init__(self,Instance_dict):
        self.data = Instance_dict
        self.nodes = []
        self.costMatrix = []
        
    def GenerateGraph(self):
        #Generate the "n" nodes, empty, without conections
        print("Generating nodes...")
        for i in range(0,self.data["n"]):
            node = Node(i)
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
        self.PrintGraph()
    
    def PrintGraph(self):
        for i in range(len(self.nodes)):
            print(self.nodes[i])
            
        for i in range(len(self.costMatrix)):
            print(self.costMatrix[i]) 
class Node:
    def __init__(self,ID):
        self.id = ID
        self.From = ""
        self.To = ""
    
    def __str__(self):
        return "Node id: " + str(self.id)
    

class Solver_Greedy:
    def __init__(self):
        pass