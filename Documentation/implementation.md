# The Implementation document
Last modified: *16.02.2025*

## Program structure  
All the documents are stored in the same directory named "Documentation".  
All the files should not be changed for stable implementing.

UHAILab/  
&emsp;┣━━━━ README.md (this file)  
&emsp;┣━━━━ ver2_vocabulary.csv  
&emsp;┣━┳━━ GRASP/  
&emsp;┃&emsp;┣━━━━ ```__init__.py```  
&emsp;┃&emsp;┣━━━━ core.py  
&emsp;┃&emsp;┣━━━━ ui.py  
&emsp;┃&emsp;┗━━━━ ```__main__.py```  
&emsp;┣━┳━━ Data/  
&emsp;┃&emsp;┣━━━━ text_general.txt  
&emsp;┃&emsp;┣━━━━ correctly_general.txt  
&emsp;┃&emsp;┣━━━━ text_technical.txt  
&emsp;┃&emsp;┣━━━━ text_slang.txt  
&emsp;┃&emsp;┗━━━━ text_noise.txt  
&emsp;┣━┳━━ Tests/  
&emsp;┃&emsp;┣━━━━ ```__init__.py```  
&emsp;┃&emsp;┗━━━━ test_prime.py    
&emsp;┗━┳━━ Documentation/  
&emsp;&emsp;&emsp;┣━━━━ implementation.md  
&emsp;&emsp;&emsp;┣━━━━ specification.md  
&emsp;&emsp;&emsp;┣━━━━ userguide.md  
&emsp;&emsp;&emsp;┣━━━━ testing_report.md  
&emsp;&emsp;&emsp;┣━━━━ week1report.md  
&emsp;&emsp;&emsp;┣━━━━ week2report.md  
&emsp;&emsp;&emsp;┣━━━━ week3report.md  
&emsp;&emsp;&emsp;┣━━━━ week4report.md  
&emsp;&emsp;&emsp;┣━━━━ week5report.md  
&emsp;&emsp;&emsp;┗━━━━ week6report.md   

The application is a spell-checker that takes keyboard input and a file as input. Using Damerau-Levenshtein distance, the application judges how far different input words are from certain dictionary where correctly-spelled words are stored. Importantly, it considers keyboard adjacency, for example, the word 'apple' can be much more possibly misspelled 'applr' than 'applt' or 'applg', given that 'e' has 'w', 's', 'd', and 'r' as adjacent keys. When searching a word, Trie tree has been applied to this application, which makes it easier to search things far faster, for instance, binary search tree. You scarcely remove words from dictionary, so I have not implemented removing function from data structure.  

In addition, I have implemented a new feature which converts words into lemma in ```lemmatize``` function. Improvements were observed in the detection rate of spelling errors in all sample texts. **Ver 1.1** is the application without lemmatization function, and **ver 1.2** is the one after lemmarization function implemented.  
![Image](https://github.com/user-attachments/assets/85adbb85-5437-458b-9fca-08010956fcbf)

## The time and space complexities achieved
### spell_check_code
```spell_check_code```'s pseudocode:  
```
function spell_check_code(code, dictionary):
    identifiers = extract_identifiers(code) O(N)
    initialize Trie
    insert all dictionary words into Trie O(W*L)
    initialize suggestions dictionary
    for each identifier:
        if identifier is not in Trie:
            compute closest word O(N * L * M)
            add suggestion to dictionary
    return suggestions
```  
Time Complexity: O(W✖️L + N + N ✖️ L ✖️ M), where W is the number of words in the dictionary, L is the average length of words, N is the number of identifiers in the code, and M is the average word length in vocabulary.  
Space Complexity: O(W✖️L) for Trie + O(N) for identifiers.  
### unrestricted_damerau_levenshtein_distance
Referring to the ideas of Lowrance and Wagner [4], although the straightforward implementation of this idea gives an algorithm of cubic complexity, explicitly incorporating the ‘exchange of adjacent characters’ into the Damelau-Levenstein distance yields the following computational quantities.  
Time Complexity: O(M✖️N), where M and N are the lengths of the input strings.  
Space Complexity: O(M✖️N)  

### get_closest_word
Time Complexity: O(N ✖️ L ✖️ M), where: N is the vocabulary size, L is the length of word, M is the average length of words in the vocabulary.  
Space Complexity: O(1) (stores only a few variables).  

## Improvements
These are improvement for the future. I think these can be the theme to do experiment. 
1. The value of *adaptive_threshold* is defined by my sense for this time. 
```
def get_closest_word(word, vocabulary):
    .
    .
    .
        adaptive_threshold = max(3, len(word) // 2 + 1)

        if distance < min_distance:
            min_distance = distance
            closest_word = dict_word
    
    return closest_word if min_distance < adaptive_threshold else "❓UNIQUE"
```  
2. The influence of ```get_keyboard_distance``` should be tuned to more appropriate value. There're some ways: to multiply the application by a small factor, e.g. 0.1, to adjust for the impact of get_keyboard_distance and to relax the conditions for application based on the score of damerau_levenshtein_distance.  
3. The new function to choose more frequently-used word. This feature can be realized with appending word frequency data to dictionary ```.csv``` file. And given some other kinds of Trie data structure, there are other technique called `bit slicing` and `Radix tree`.  

## Use of LLMs
I used LLMs for these following reasons.
- To check my mistakes in English grammar and to improve it.  
- To find reliable reference to reinforce my opinion and explanation in specification documents.  
- To translate the results and outputs which are responded by terminal into Japanese.  
- To generate sample ```.txt``` file written in slang and text which has noise.  

## References
[1] https://github.com/sari-bee/tieteellinen_laskin?tab=readme-ov-file  
[2] https://python-poetry.org/docs/cli/#script-project  
[3] https://www.wordfrequency.info/  
[4] https://dl.acm.org/doi/10.1145/321879.321880  