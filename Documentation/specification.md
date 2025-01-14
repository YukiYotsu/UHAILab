# The Project Specification
Last modified: *14.01.2025*

My name is Yuki Yotsumoto. I belong to **Bachelor of Science in Computer Science** (CS) as an exchange student from Japan. All the project's documentation are written in **English markdown** (.md) language.

## Programming language used in this project
I would like to code with **Python** language in this project this time because it should be easy for many computer engineers to understand, given its easy grammar rule [1] and its popularity.

And as mentioned on the page of the course's details on other documentation, I would like to mention other language which I am good at to the extent that I can peer review projects. In addition to Python, I can do in **C** as well.

## What problem am I solving?
I focus on program analysis problem to help programmers study a structure of program and clarify errors in code.　In short, this project is on code analysis tool and spell checker (when there is mistake on spell of program).

I would like to name this project **GRASP**, meaning to permit users to grasp what program does.
I define GRASP as the term standing for 
**G**raphically **R**ecognizable **A**nalysis **S**ystem for **P**rogramming.

In computer science, in general, a growing use of program analysis is in the verification of properties of software used in safety-critical computer systems and locating potentially vulnerable code [2]. But GRASP is *for beginners, rather than for security reasons*.

If the code you have written does not produce expected results, you need to grasp what is wrong.  
For example,  
- how in order program works
- what kind of number each of variables has
- which route is selected in conditioal branching.

Therefore, I focus on the fact that it's difficult for programming beginner to clarify the cause of some errors in program. 

## What algorithms and data structures am I implementing?
I would like to apply several techniques to main two purposes: code analysis tool and spell checker.  

---
#### **Code analysis tool**
I will make both the process logic and the class structure of the target program visible with flowchart

I will apply **Knuth-Morris-Pratt algorithm** (KMP) [3] to find specific string in whole text.  

---

#### **Spell checker**
As mentioned in the course page of ideas for project topics, 
> A spell checker can be implemented by comparing the distance from an input string that is NOT in a dictionary to others that are.  

I will apply **Damerau-Levensthein distance** to compare the distance. The vocabulary can be stored in a **Trie** (prefix tree) data structure.

---
Preferably, I will visualize the flow of variables and which route is selected in conditioal branching.

## References
[1] Python Software Foundation, https://docs.python.org/3/reference/grammar.html  
[2] Benjamin Livshits section 7.3 "Static Techniques for Security," Stanford doctoral thesis, 2006., https://dl.acm.org/doi/10.5555/1269235  
[3] Knuth, Donald; Morris, James H.; Pratt, Vaughan (1977). "Fast pattern matching in strings".
https://doi.org/10.1137/0206024