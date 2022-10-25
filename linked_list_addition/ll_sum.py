import sys

class Node(object):
    def __init__(self, key):
        self._key = key
        self._next = None

class LL(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def print(self):
        curr = self._head
        if  curr is None: print("LL is empty")
        while (curr):
            print("{}".format(curr._key), end = '')
            if curr._next:
                print(" -> ", end = '')
                curr = curr._next
            else:
                return

    def insert(self, key):
        new_node = Node(key)
        last = self._tail
        new_node._next = None

        if self._head is None:
            new_node._next = None
            self._head = new_node
            self._tail = new_node
            return
        # shift tail and add to end
        last._next = new_node
        self._tail = new_node
        self._size += 1
        #print("Adding {} to LL".format(key))
    
    def get_str(self):
        k = ''
        curr = self._head
        while (curr):
            k += '{}'.format(curr._key)
            if curr._next:
                curr = curr._next
            else:
                break
        return k

def int_to_ll(a):
    digits = [int(digit) for digit in str(a)] # convert int to a list of digits (in order)
    digits.reverse() # flip the list of digits to be in reverse order

    ll = LL()

    for i in range(0, len(digits)):
        ll.insert(digits[i])

   # ll.print()
    return ll

def ll_to_int(ll):
    try: #convert ll to list of digits
        strings = ll.get_str()
        return int(strings) # try to convert string to int
    except:
        print("Failed to convert int_ll to int")
        return None

def sum_ll(ll_a, ll_b):
    int_from_ll_a = ll_to_int(ll_a)
    int_from_ll_b = ll_to_int(ll_b)
    ll_sum = int_from_ll_a + int_from_ll_b
    return int_to_ll(ll_sum) # convert new int summation into the ll format
    
def test(a, b):
    # linked list a
    ll_a = int_to_ll(a)
    print("ll_a: ", end='')
    ll_a.print()
    print("\n", end='')

    # linked list b
    ll_b = int_to_ll(b)
    print("ll_b: ", end='')
    ll_b.print()
    print("\n", end='')
        
    # linked list a and b summation
    ll_sum = sum_ll(ll_a, ll_b)
    print("ll_a + ll_b = ", end='')
    ll_sum.print()
    print("\n",end='')
    return ll_sum

if __name__ == "__main__":
    if len(sys.argv) - 1 == 2: # user defined ll_a and ll_b
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            test(a, b)
        except:
            print("Error: Invalid input type. ex: Python3 ll_sum.py <ll_a> <ll_b>".format(sys.argv[1], sys.argv[2]))
    else: # no CLI definitions, use default test case
        test(21741, 273486)
