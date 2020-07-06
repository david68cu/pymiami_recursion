import pytest
import pycodestyle
import sys

# We need to pass the path to each file we want our linter to check 
# during this test
path_to_file = '../appCode/exercise1_solution.py'


def test_conformance():
    """Test that we conform to PEP-8."""
    style = pycodestyle.StyleGuide(quiet=True)
    result = style.check_files([path_to_file])
    print(result.print_statistics())
    assert(result.total_errors == 0)


def main():
    test_conformance()


if __name__ == "__main__":
    main()
