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

## Unit testing with Pytest

We added two  tests to  just exemplify how to  use Pytest
Note that we had to run pytest as module as under:

```python
python -m pytest
```

* Test #1  Unit testing a file, in thie case exercise1_solution.py
* Test #2  Run a test where we check that the 

## GitHub actions for Continous Integration

After deploying to GitHub we want to double check that any new commit is free of errors. Code comming from other developers , will need correctly satisfy these action before being merged.

So any new pull request must first pass a GitHub action that:

* Install dependencies in requirements.txt
* Run the new pycodestyle (old pep8)  lynter and check there is no style errors
* Execute the unit tests  we have defined for this application

### References

[1][Test Driven Development Python by  Harry J.W. Percival]
