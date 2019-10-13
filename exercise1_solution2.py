""" 
Exercise 1: Write a recursive function count_multiples(a, b) that counts 
how many multiples of a are part of the factorization of the number b. 
For example:

 >>> count_multiples(2, 6)     # 2 * 3 = 6
 1
 >>> count_multiples(2, 12)    # 2 * 2 * 3 = 12
 2
 >>> count_multiples(3, 11664)
 6
 >>>

This send the state to any new call
here we print the stack to see how the function s get accumulated there

"""
import traceback

def count_multiples(a, b,counter=0):
    traceback.print_stack()
    # Avoiding 6/1(a>1) or 2/4(b>a)
    if a > 1 and b>a:  
      if b%a == 0:  # Recursive case  
          counter += 1
          b= b/a
          return count_multiples(a, b, counter)
      else: 
        #return (a, b, counter)
        return counter
      

def main():
    c= count_multiples(3, 11664)
    print(c)


if __name__ == "__main__":
    main()

# 1-  11664, 3, 0

# 2-  11664, 3, 0
#      3888, 3, 1

# 3-  11664, 3, 0
#      3888, 3, 1 
#      1296, 3, 2

# 4-  11664, 3, 0
#      3888, 3, 1 
#      1296, 3, 2
#       432, 3, 3

# 5-  11664, 3, 0
#      3888, 3, 1 
#      1296, 3, 2
#       432, 3, 3
#       144, 3, 4


# 6-  11664, 3, 0
#      3888, 3, 1 
#      1296, 3, 2
#       432, 3, 3
#       144, 3, 4
#        48, 3, 5


# 7-  11664, 3, 0
#      3888, 3, 1 
#      1296, 3, 2
#       432, 3, 3
#       144, 3, 4
#        48, 3, 5
#        16, 3, 6
