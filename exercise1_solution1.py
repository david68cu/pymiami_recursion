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

This solution take the state and "thread it" taking to an external entity in this case a class
This is in my opinion the worse implementation out of teh three solutions 
"""
class Counter():

    def __init__(self, c=0):
        self.c = c

    def count(self, x):
        if x>self.c:
            self.c=x

    def get_c(self):
        return self.c


def count_multiples(a, b, c,counter=0):
    if a > 1 and b>a: # recursive Case (no base case as we thread the state)
      if b%a == 0:
          counter += 1
          c.count(counter)
          b= b/a
          count_multiples(a, b,c,counter)



def main():
    c = Counter()
    counter = count_multiples(3, 11664,c)
    print(counter)
    #print(c.get_c())


if __name__ == "__main__":
    main()

