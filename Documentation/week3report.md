# Weekly Report (Week 3)  
I'm Yuki Yotsumoto. This is the 3rd weekly report.
**I newly created the branch to test my coverage.**

## Weekly outcome and advancements  
The time required this week was 15 hours. I made the program which does spell check with Damerau-leveshtein distance. I made the vocabulary which has been named "Programming_vocabulary.csv" to use as correctly-spelled words by myself*.  
When I did coverage test, I can have generated html file which reported coverage rates.  
When I did, I should have did like this:  
```
coverage run --append test_prime.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
takumi@takuminoMacBook-Pro Tests % coverage html
Wrote HTML report to htmlcov/index.html
```  


## Unclear or problematic things  
- Do you know the words (espacially, related to programming terms) of csv, for example 'inf', 'class', and 'return'?  
- I use 'coverage' to generate coverage report. When I install coverage, I cannot avoid using pip. Is it okay? or it'll conflict with Poetry?  
- I grasp we will do peer-review. All I have to do is just making poetry.lock file in my repository for other students?  

## Prospect -- what's next  
