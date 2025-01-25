import subprocess
import os
from pathlib import Path

def main():
    """
    """
    current_directory = Path(__file__).resolve().parent

def connectiontest(arg1: int, arg2: int):
    """ Test stable relations between some files in different python programs

    Keyword arguments:
        arg1 (int): The number of candidate number decided by the programmer
        arg2 (int): The other number of candidate number decided by the programmer

    Returns:
        int: The sum of arg1 and arg2
    """
    return arg1 + arg2

if __name__ == "__main__":
    # this is implemented only when this python file is selected directly.
    main()