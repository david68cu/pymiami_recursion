import traceback

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Solution # 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Counter():

    def __init__(self, c=0):
        self.c = c

    def count(self, x):
        if x > self.c:
            self.c = x

    def get_c(self):
        return self.c


def count_multiples1(a, b, c, counter=0):
    if a > 1 and b > a:  # recursive Case (no base case as we thread the state)
        if b % a == 0:
            counter += 1
            c.count(counter)
            b = b/a
            count_multiples(a, b, c, counter)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Solution # 2
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def count_multiples2(a, b, counter=0):
    traceback.print_stack()
    # Avoiding 6/1(a>1) or 2/4(b>a)
    if a > 1 and b > a:
        if b % a == 0:  # Recursive case
            counter += 1
            b = b/a
            return count_multiples(a, b, counter)
        else:
            # return (a, b, counter)
            return counter

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Solution # 3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def count_multiples(a, b):
    traceback.print_stack()
    if b % a:  # base case will look when b%a is not zero
        # breakpoint()
        return 0
    return 1 + count_multiples(a, b / a)
    # recursive case .Every time it is zero, we will have a recursive case


def main():
    c = count_multiples(3, 11664)
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
