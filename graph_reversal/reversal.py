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

    def print_reverse(self):
        print("--- Reverse Printinging ---")
        curr = self._tail
        if curr is None: print("Graph is empty...")
        while (curr):
            print("{}".format(curr._key), end='')
            if (curr._prev):
                if (self._direction == 1): # walk right
                    sys.stdout.write("->")
                elif (self._direction == 0): #walk left
                    sys.stdout.write("<-")
                curr = curr._prev
            else:
                print("\n--- Printing Finished ---")
                return

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
        new_node = Node(key=key) # set up new node with the insertion value
        last = self._tail
        new_node._next = None

        if self._head is None: # verify the graph isn't empty before adding
            new_node._prev = None # if so, define the tail and head nodes
            new_node._next = None
            self._head = new_node
            self._tail = new_node
            return
        # since we have a tail value, just shift to add a new node and update references
        new_node._prev = last
        last._next = new_node
        self._tail = new_node

        print("Adding {} to end of graph".format(key))

def reverse(graph):
    print("reversing graph order")
    rev = Graph() # initialize the reversal graph
    rev._head = graph._tail # set its head node to the tail node of the main graph
    curr = graph._tail._prev # define curr to walk through the graph LL
    rev._head._next = curr # set the reference points for the linked list on rev
    rev._head._prev = None
    step = rev._head._next # define step to walk through the rev graph

    
    while (curr):
        step = curr
        step._next = curr._prev
        step._prev = curr._next
        curr = curr._prev

        if not curr: # we have reached the end of the linked list
            rev._tail = step._next
            rev._tail._next = None
            rev._tail._prev = step
            break
    
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
    g.print_reverse()

    # attempt to reverse the graph
    # r = reverse(g)
    # r.print()
    

if __name__ == "__main__":
    if ((len(sys.argv) - 1) >= 1):
        print("CL argument {}: {}".format(1, sys.argv[1]))
        # intepret user input, attempting to create a graph from the list of nodes
        # globals()[sys.argv[1]]()
    else:
        test() # run the default application
