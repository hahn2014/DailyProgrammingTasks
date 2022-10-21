import sys

class Node(object):
    def __init__(self, key):
        self._key = key
        self._next = None
        self._prev = None

class Graph(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._direction = 1 # 1 for right, default
    
    def print(self):
        print("--- Printing Graph ---")
        curr = self._head
        if curr is None: print("Graph is empty...")
        while (curr): # continue through LL until we reach last node
            print("{}".format(curr._key), end='')
            if (curr._next): # there exists another node, prep direction arrow
                if (self._direction == 1): # walk right
                    sys.stdout.write("->")
                elif (self._direction == 0): # walk left
                    sys.stdout.write("<-")
                curr = curr._next
            else:
                print("\n--- Printing Finished ---")
                return

    # insert a new node to the graph at the end of the linked list (append)
    def insert(self, key):
        new_node = Node(key) # set up new node with the insertion value
        print("Adding {} to end of graph".format(key))
        if self._head is None: # make sure the graph isn't empty
            self._head = new_node # start the graph with a new head node
            self._head._prev = None
            self._tail = new_node # since there is only one value, head and tail are the same
            return
        else:
            last = self._tail # insert new node at end of list in O(1) time by keeping track of
            last._next = new_node # the tail of the linked list, and updating once a new node is
            last._next._prev = last
            self._tail = new_node # added, keeping insertion constant time.
            self._tail._prev = last

def reverse(graph):
    rev = Graph()
    rev._head = graph._tail
    curr = graph._tail._prev

    while (curr):
        rev._next = curr
        curr = curr._prev
        if curr is None:
            break
    
    rev._tail = graph._head
    return rev

def test():
    print("No graph provided as CL input. Using default")
    g = Graph()
    
    g.insert("A")
    g.insert("B")
    g.insert("C")
    g.insert("D")
    g.insert("E")

    g.print() # print the graph
    r = reverse(g) # reverse the graph
    r.print() # print the new reserved graph
    

if __name__ == "__main__":
    if ((len(sys.argv) - 1) >= 1):
        print("CL argument {}: {}".format(1, sys.argv[1]))
        # intepret user input, attempting to create a graph from the list of nodes
        # globals()[sys.argv[1]]()
    else:
        test() # run the default application
