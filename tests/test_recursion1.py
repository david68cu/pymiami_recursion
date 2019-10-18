import pytest
from appCode.exercise1_solution import count_multiples


# Because pytest is run from /usr/bin The home directory of the program
# This is the directory of your root script. When you are running pytest
# your home directory is where it is installed (/usr/local/bin probably).
# No matter that you are running it from your src directory because the
# location of your pytest determines your home directory.
# That is the reason why it doesn't find the modules

# Solution1 run pytest as module
# python -m pytest


def test_count_multiples():
    # Arrange
    # Loading the module we already did
    # Act
    result = count_multiples(3, 243)
    # Assert
    assert result == 5


def main():
    test_count_multiples()


if __name__ == "__main__":
    main()
