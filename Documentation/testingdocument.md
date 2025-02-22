# The Testing Document
Last modified: *22.02.2025*

## unittest coverage report
The unittest has used ```unittest``` Python library in ```test_prime.py``` in Tests directory. Basically, all the test methods is designed in this Python file, but this directory is for test-only. Instead, programs which actually control GRASP application are written on Python files in GRASP directory.

```
takumi@takuminoMacBook-Pro tests % poetry run coverage report
Name                                                       Stmts   Miss  Cover
------------------------------------------------------------------------------
/Users/takumi/Documents/GitHub/UHAILab/GRASP/__init__.py       0      0   100%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/config.py         6      0   100%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/core.py         167     16    90%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/ui.py            80     65    19%
test_prime.py                                                123      0   100%
------------------------------------------------------------------------------
TOTAL                                                        376     81    78%
```
##