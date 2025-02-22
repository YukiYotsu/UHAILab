# Weekly Report (Week 3)  
I'm Yuki Yotsumoto. This is the 6th weekly report.  

## Weekly outcome and advancements  
Approximately 30 hours required to proceed the project this week. I have newly made user-definition feature; a user can define a word correctly-spelled OR he/she wants to do however it spells. Those words defined by users are recorded in csv file (cf. `user-defined.csv`) In addition, I have combined this csv with `ver2_vocabulary.csv` so that once a user defines new word (do correction at spelling), they will no longer be judged as misspelled words.  

I have been able to **improve coverage rate*:.  
```
...................
----------------------------------------------------------------------
Ran 27 tests in 0.008s

OK
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

## Unclear or problematic things  
-   

## Prospect -- what's next  
There are some improvements to check correct spell; I have disabled past form lemmatization because it needs to register past expressions dictionary. And it is difficult to do coverage test in UI. I think this is because there are parts of the UI that cannot be checked for correct implementation without our human eyes, which means that there are only a limited number of areas that can be checked by code alone.  