# Weekly Report (Week 3)  
I'm Yuki Yotsumoto. This is the 4th weekly report.  

## Weekly outcome and advancements   
I think I have correctly installed coverage and prepared for using poetry finally. The respond from terminal was following.  
```
takumi@takuminoMacBook-Pro tests % poetry run coverage run test_prime.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
takumi@takuminoMacBook-Pro tests % poetry run coverage report
Name                                                       Stmts   Miss  Cover
------------------------------------------------------------------------------
/Users/takumi/Documents/GitHub/UHAILab/GRASP/__init__.py       0      0   100%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/__main__.py      96     51    47%
test_prime.py                                                 24      0   100%
------------------------------------------------------------------------------
TOTAL                                                        120     51    58%
```  
I made ```ui.py``` to generate GUI on a user's display and modulize some .py files into ```__main__.py```, ```core.py```, and ```ui.py```. ```core.py``` has core functions like KMP method and Damerau-levenshtein distance to implement **spell-check**. And I put (on the directory) ```ver1_Programming_vocabulary.csv```, which has been made by myself, referring to some official Python-terms' page https://docs.python.org/ja/3.13/library/functions.html.  
I successfully installed *CustomTkinter* to generate modern UI so that everyone can use my App far more easily.  
Approximately 30 hours required to proceed the project this week.  

## Unclear or problematic things  
- Do you know the way to get specific CSV file (or TXT file) which has vocabulary (espacially related to programming terms, for example 'inf', 'class', and 'return')?  

## Prospect -- what's next  