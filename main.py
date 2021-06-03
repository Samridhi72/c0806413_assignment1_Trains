import partA
import partB
#these are routes defined in a list
edges = [
    ['A','B',1],['A','D',2],['A','E',7],
         ['B','C',3],
         ['C','D',1],['C','E',4] ,
         ['D','C',1],['D','E',2],
         ['E','B',3]
        ]

#these are routes defined in a dictionary
graph = {
    'A': {'B': 1, 'D': 2, 'E': 7},
    'B': {'C': 3},
    'C': {'D': 1, 'E': 4},
    'D': {'C': 1, 'E': 2},
    'E': {'B': 3}
}
#menu function to list options available
def menu():
    print("---------------select one option to choose-----------")
    print(" 1. Calculate distance b/w A-B-C(using list)")
    print(" 2. The number of trips starting at C and ending at C with a maximum of 3 stops(using dictionary)")

def  main():
    menu()
    choice = int (input("Enter the choice 1 or 2: " ))
    if choice ==1:
        partA.cal_distance(edges)
    else :
        print(f"number of trips starting and ending at C ", partB.cal_trips(graph, 'C', [], []))


main()