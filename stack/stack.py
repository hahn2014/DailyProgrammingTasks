from collections import deque

def Push(stack, val):
    stack.append(val)
    print("StackPush: {}".format(val))

def Pop(stack):
    try: # try except statement to catch any pop calls on an empty stack
        val = stack.pop()
        print("StackPop: {}".format(val))
        return val
    except: # stack empty, notify the user
        print("Error: Empty stack, cannot pop.")

def Max(stack):
    try:
        return 1
    except:
        return 0

def empty(stack):
    if stack: # implicitly convert stack to a boolean value, if true stack is not empty
        return False
    else: # else, if false stack is empty
        return True

def test():
    stack = deque() #initialize deque stack
    print("StackEmpty: {}".format(empty(stack)))
    Pop(stack)
    Push(stack, 1)
    Push(stack, 0)
    Push(stack, 20)
    print("StackEmpty: {}".format(empty(stack)))
    val = Pop(stack)
    _max = Max(stack)

if __name__ == '__main__':
    # globals()[sys.argv[1]]()
    test()
