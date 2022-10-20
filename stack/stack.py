import random
import sys
from collections import deque

def Push(stack, val):
    stack.append(val) # appending the val to the end of the deque data structure
    print("StackPush: {}".format(val))

def Pop(stack):
    try: # try except statement to catch any pop calls on an empty stack
        val = stack.pop()
        print("StackPop: {}".format(val))
        return val
    except: # stack empty, notify the user
        print("Error: Empty stack, cannot pop.")

def Peek(stack):
    # leftmost value of a deque is the "top" value, we can return this in O(1) by
    if (Empty(stack)):
        print("Error: Cannot peek an empty stack.")
        return 0
    else:
        return stack[0] # referencing the 0th index of the deque

def Max(stack):
    try:
        return 1
    except:
        return 0

def Size(stack):
    return len(stack) # due to RAM memory management, len() is already O(1)

def Empty(stack):
    if stack: # implicitly convert stack to a boolean value, if true stack is not empty
        return False
    else: # else, if false stack is empty
        return True

def test():
    stack = deque() #initialize deque stack
    print("StackEmpty: {}".format(Empty(stack)))
    Pop(stack)
    Push(stack, 1)
    Push(stack, 0)
    Push(stack, 20)
    print("StackEmpty: {}".format(Empty(stack)))
    print("StackSize: {}".format(Size(stack)))
    val = Pop(stack)
    print("StackSize: {}".format(Size(stack)))
    _val = Peek(stack)
    print("StackPeek: {}".format(_val))
    print("StackSize: {}".format(Size(stack)))
    _max = Max(stack)

def test2():
    stack = deque() # initialize deque stack
    random.seed()
    for i in range(random.randrange(1,1001)):
        Push(stack, random.randrange(1,100))
    print("StackSize: {}".format(Size(stack)))

if __name__ == '__main__':
    if ((len(sys.argv) - 1) >= 1): # user defined function calls
        globals()[sys.argv[1]]()
    else:
        test() # test fundamentals
