import traceback

def count_multiples(a, b):
    traceback.print_stack()
    if b % a: # base case will look when b%a is not zero 
        #breakpoint()
        return 0
    return 1 + count_multiples(a, b / a)  # recursive case .Every time it is zero , we will have a recursive case

def main():
    c= count_multiples(3, 11664)
    print(c)


if __name__ == "__main__":
    main()