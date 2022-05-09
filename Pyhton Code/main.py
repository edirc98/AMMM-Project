from InstanceGenerator import InstanceGenerator

numInstances = 4
n = 4 #Number of codes
m = 3 #Lenght of each code


def main():
    Instance = InstanceGenerator(numInstances,n,m)
    Instance.GenerateInstance(n,m)
    print(Instance.codes)
    #print(Instance)
    # TODO


main()