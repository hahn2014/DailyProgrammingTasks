import math, sys

def gcd(nums):
    return math.gcd(*nums)

def test():
    nums = [42,56,14]
    print("List of Numbers: {}".format(nums))
    print("Greatest Common Denominator: {}".format(gcd(nums)))

if __name__ == "__main__":
    args = len(sys.argv) - 1
    if args == 0:
        test()
    else:
        try:
            ints = []
            nums = sys.argv[1].split(',')
            print("string split: {}".format(nums))
            for i in range(0, len(nums)):
                print("list[{}]: {}".format(i, nums[i]))
                ints[i] = int(nums[i])
            
            print("Intepreted integer list: {}".format(nums))
        except:
            print("CLI argv[{}] was not formatted as a list of integers".format(1))
