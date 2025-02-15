# Weekly Report (Week 3)  
I'm Yuki Yotsumoto. This is the 5th weekly report.  

## Weekly outcome and advancements
 
Approximately 20 hours required to proceed the project this week.  
I changed the vocabulary file into *Word frequency Top 5000*'s file to check if words are correctly-spelled. You can get access with the link below.  
https://www.wordfrequency.info/  
I have done coverage test newly.  
``` 
Name                                                       Stmts   Miss  Cover
------------------------------------------------------------------------------
/Users/takumi/Documents/GitHub/UHAILab/GRASP/__init__.py       0      0   100%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/core.py         126     36    71%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/ui.py            58     46    21%
test_prime.py                                                 74      1    99%
------------------------------------------------------------------------------
TOTAL                                                        258     83    68%
```  
The coverage rate on core functions got higher, which was quite good news for me, on the other hand, it was **difficult** to implement test on UI. I think this is because inputs and outputs are not representational and difficult to extract them and see on the test code.  

## Unclear or problematic things  
- Do I have to change (re-write) my specification document because the core functions of my projects have been changed?  
- When it comes to make testing document, am I applicable to make the presentation of the empirical testing result of the program function in a graphical form? This is because what I will be able to do for this is making the chart of the coverage rate along days.  
- Haven't demo sessions started yet, right? I would like to be sure that.  

## Prospect -- what's next  
I would like to improve my test's coverage rate to 80% on average and finish to write some documents properly. And some functions have missed docstring. I think docstring is needed for people who check my code.  