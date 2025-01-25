# Weekly Report (Week 2)  
I'm Yuki Yotsumoto. This is the 2nd weekly report.

## Weekly outcome and advancements  
The time required this week was 20 hours. It took about 10 hours to understand Poetry and unittest. I made the demo programs of main project called GRASP and the directory for tests (unittest). I referred to Mr. Kenneth Reitz's recommendation [1].

I learned what is docstring, which tells what my classes and methods do. And also, I understood how to write docstring appropriately along PEP 257.

```
# this is a comment.
""" this is docstring
"""
```
I'm not sure what is clearly different between comments and docstring, but as long as I look up, it is quite efficient and convenient to leave docstring when you need to documents generated automatically by Sphinx.

And I installed Poetry with no problem to handle automated tests and test coverage calculations. I have practiced the code examples on the page [2].    

I newly created the program named "test_prime.py" for testing __main__.py placed at GRASP directory. And I confirmed that test_prime.py succeeded in importing __main__.py and also successfully tested.  

For this week, test_func function which is in Tests directory has easy test model in order to test connectiontest function which belongs GRASP directory. I will remove these functions, which will be used only for ensuring these files can transmit their function to each other.  

When succeeding and failing, the results of each cases are following in order.  
```
takumi@takuminoMacBook-Pro Tests % python3 -m test_prime
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```  
and  
```
takumi@takuminoMacBook-Pro Tests % python3 -m test_prime
F
======================================================================
FAIL: test_func (__main__.TestFunc.test_func)
Implement test.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/takumi/Documents/GitHub/UHAILab/Tests/test_prime.py", line 28, in test_func
    self.assertEqual(expected, actual)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
AssertionError: 3 != 5

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```  

## Unclear or problematic things  
- May I ask what is 'tab completion'? When I installed Poetry, the instruction page [3] for installing has also the section named 'Enable tab completion for Bash, Fish, or Zsh' Do I have to do setting this as well?  
- According to "Poetry and dependency management" written by this course, I'll probably do something wrong by using pip. Is just avoiding the use of pip fine? because I have installed pip.  
- Should I place poetry directory at the same directory for my project? Or is it fine to place it anywhere?

[1] "Structuring Your Project", https://docs.python-guide.org/writing/structure/
[2] Poetry, https://python-poetry.org/docs/  
[3] Algorithms and Artificail Intelligence Training, https://algolabra-hy.github.io/poetry-fi  

## Prospect -- what's next  
Hopefully, I could have started to design the structure of my project. I would like to search for the way to design UI coming week. I'm thinking Tkinter which belongs Python UI library and CustomTkinter, which looks more modern.