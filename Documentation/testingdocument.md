# The Testing Document
Last modified: *23.02.2025*

## unittest coverage report
The unittest has used ```unittest``` Python library in ```test_prime.py``` in Tests directory. Basically, all the test methods is designed in this Python file, but this directory is for test-only. Instead, programs which actually control GRASP application are written on Python files in GRASP directory.

```
Name                                                       Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------------------
/Users/takumi/Documents/GitHub/UHAILab/GRASP/__init__.py       0      0   100%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/config.py         6      0   100%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/core.py         134      2    99%   274, 278
/Users/takumi/Documents/GitHub/UHAILab/GRASP/ui.py            80     65    19%   17-53, 65-69, 74-76, 87-113, 118-131
test_prime.py                                                155      0   100%
----------------------------------------------------------------------------------------
TOTAL                                                        375     67    82%
``` 

*Test was done on 23 Feb.*

## Structure of test code
Basically, ```test_prime.py``` is composed of three classes: `class TestDamerauLevenshtein`, `class TestUI`,and `class TestCoreFunctions`. This GRASP is also suitable for checking the spelling of longer texts. In the application, `split_code` method has the role to split sentences into words to simplify the calculation of Damerau-Levenshtein distance.  
### Testing Damerau-Levenshtein distance
In `class TestDamerauLevenshtein`, there are many methods to test various occasions.  
- **Testing basic edit against letters**  
When testing same strings, the distance should be 0.  
``` 
def test_same_strings(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("hello", "hello"), 0)
``` 
And in other cases, the distance test is done for each of functions to edit phrases: *insertion*, *deletion*, *substitution*,and *transportation*.  
- **Testing multiple operations**  
The test must check the distance is correct if it needs to edit for multiple times.   
```
def test_multiple_operations(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("kitten", "sitting"), 3)
```  
- **Others**  
Other tests were carried out within the same class to see if the edit distance was calculated correctly for empty strings, different case letters, special characters, Japanese characters, etc.  

### Testing UI
In `class TestUI`, there are only two methods to check that the UI is working correctly. It is difficult to do coverage test in UI. I think this is because there are parts of the UI that cannot be checked for correct implementation without our human eyes, which means that there are only a limited number of areas that can be checked by code alone. The two methods check if the application receives user's input correctly and it shows the result correctly.  

### Testing Trie tree and keyboard distance
In `class TestCoreFunctions`, it tests whether Trie tree is working well, they can get accurate keyboard distance, it gets surely the closest word, and it loads CSV and saves one(process of CSV).  
- **Testing Trie tree**  
A method `test_trie_operations` checks if `test_prime.py` can insert a word surely with Trie's `search` method. Of course, at the same time, it is checking `insert` method. There is no other methods in Trie class because it does not have to remove an element from tree.
- **Testing keyboard distance mechanism**  
This is about my original mechanism: `get_keyboard_distance` method: it returns; 0: those characters are the same; 0.2: those characters are not the same but adjacent; 0.45: those characters are not adjacent and different.  
```
def test_get_keyboard_distance(self):
        self.assertEqual(core.get_keyboard_distance('a', 'a'), 0)
        self.assertEqual(core.get_keyboard_distance('a', 's'), 0.2)
        self.assertEqual(core.get_keyboard_distance('a', 'g'), 0.45)
```
It is designed seperately from Damerau-Levenshtein distance because they should not be mixed even when testing.　　
- **Testing the method getting the closest word**  
Arrays are available that are used only for testing.
```
def test_get_closest_word(self):
        vocabulary = ["hello", "world", "help", "held"]
        self.assertEqual(core.get_closest_word("hellp", vocabulary), "hello")
        self.assertEqual(core.get_closest_word("xyz", vocabulary), "❓UNIQUE")
```
**My programme intentionally tends to give priority to those whose character counts are matched.**  
The distance between "hello" and "hellp" is originally 1.0 when applying Damerau-Levenshtein distance. This is the same value for the case where comparing "help" and "hellp". However, because I believe a user can notice misspelled words more easily if they have the same number of characters, priority is given by penalizing differences in the number of characters in `get_closest_word` method in `core.py` below.
```
# if the lengths are not matched
        else:
            length_difference_penalty = abs(len(word) - len(dict_word)) * 0.5
            distance += length_difference_penalty
```  
- **Others**  
Other methods for word normalisation (lemmatize) and lly form transformations are also tested.  

## Execution time
I have measured execution time. This is done to ensure that the long text spell-checking works as expected. To check efficiency by graphing the processing speed, the text of `text_general.txt` was repeated in input box (increasing exponentially by a factor of 10 from 1). The text has 354 characters.   

x1: 0.5363881587982178 sec  
x10: 2.547447919845581 sec  
x100: 33.829548835754395 sec  
x1000: 507.8054449558258 sec  
x10000: 5137.369160890579 sec  

*This test was done on 22 Feb.*  

It has revealed it is a serious problem to use this application on extremely long text file. However, I have a good solution against this problem. I implemented *C* program which calculates Damerau-Levenshtein distance. **For *C* language is compiled language, the calculation is far faster** than Python. For example, when I tested with x10000 text file, the execution time was only *283.49342799186707* sec. This means a calculation speed-up of **1800**%.  

x1: 0.05860114097595215 sec  
x10: 0.3188469409942627 sec  
x100: 3.0657098293304443 sec  
x1000: 30.738240003585815 sec  
x10000: 283.49342799186707 sec  

![Comparison among Execution Time of GRASP Application ](https://github.com/user-attachments/assets/6e2e8b19-e8e1-4364-9ce1-10ba6928e5bb)  

*This test was done on 23 Feb.*  

## Spell check accuracy
I calculated the accuracy (graph below) of spell-checking (**without user-defined words CSV).  Before keyboard distance (for instance, keyboard distance has been newly changed into shorter one), lemmatization function are renewed, the version is determined GRASP v1.2, and after that, the version is GRASP v1.3.  
![percentage of exact correction v1-3](https://github.com/user-attachments/assets/83c22e01-487e-4dc5-b06f-e6c04229c8f0)  

Theoretically, with user-defined CSVs, spell checking becomes as close to 100% as possible.
