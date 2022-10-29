import sys, math

def test(a):
    n = len(a)
    start = -1
    end = 0

    for i in range(n):
        if (n - i > 1): #ensure we have at least 1 more index to visit
            if (a[i] % a[i+1] == 0) or (a[i+1] % a[i] == 0):
                if (start == -1): start = i
            else:
                if (start != -1): end = i+1
    
    if (end == 0):
        end = n

    n = end - start
    subset = [None] * n
    index = 0
    for i in range(start, end):
        subset[index] = a[i]
        index += 1

    print(subset)


if __name__ == "__main__":
    args = len(sys.argv) - 1

    if args == 0:
        arr = [3,5,10,20,21]
        arr1 = [1,3,6,24]
        test(arr)
        test(arr1)
    else:
        try:
            nums = sys.argv[1].split(',')
            ints = [0] * len(nums) # initialize the int list of size nums
            for i in range(0, len(nums)):
                ints[i] = int(nums[i]) # convert the current index string to int
            print("Intepreted integer list from CLI: {}".format(nums))
            test(ints)
        except:
            print("CLI argv[{}] was not formatted as a list of integers".format(1))

    
