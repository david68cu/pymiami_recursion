# Recursion Review with pytest and github actions

```python
 def count(start, stop):
     if start >= stop:
         return
     else:
         print(start)
         count(start+1, stop)
```

Count from 0 to 9

```python
count(0, 10)
```

Here is a classic example that computes factorials:

```python
 def factorial(n):
     if n <= 1:
         return 1
     else:
         return n * factorial(n - 1)
```

Exercise
Do this exercise with Python .

Exercise 1: Write a recursive function count_multiples(a, b) that counts how many multiples of a are part of the factorization of the number b. For example:

```python
 >>> count_multiples(2, 6)     # 2 * 3 = 6
 1
 >>> count_multiples(2, 12)    # 2 * 2 * 3 = 12
 2
 >>> count_multiples(3, 243)   
 5
 >>>
 ```
