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

We added a simple test just to exemplify the use of Pytest
Note that we had to run pytest as:

```python
python -m pytest
```

## GitHub actions for CI

After deploying to GitHUb we want to double check that any new commit is free of errors.So any new pull request must first pass aGitHub actions that:

* Run the new pycodestyle (old pep8)  lynter
* Execute the unit test

### References

[1][Test Driven Development Python by  Harry J.W. Percival]
