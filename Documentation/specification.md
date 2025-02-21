# The Project Specification
Last modified: *22.02.2025*

My name is Yuki Yotsumoto. I belong to **Bachelor of Science in Computer Science** (CS) as an exchange student from Japan. All the project's documentation are written in **English markdown** (.md) language.

## Programming language used in this project
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fimg.shields.io%2Fbadge%2F-Python-F2C63C.svg%3Flogo%3Dpython%26style%3Dfor-the-badge?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c17144ccc12f9c19e9dbba2eec5c7980">  

I would like to code with **Python** language in this project this time because it should be easy for many computer engineers to understand, given its easy grammar rule [1] and its popularity.

I would like to mention other language which I am good at to the extent that I can peer review projects. In addition to Python, I can do in **C** as well.

## What problem am I solving?
I focus on program analysis problem to help programmers study a structure of program and clarify errors in code. At first, I will make **spell checker**.  

I would like to name this project **GRASP**, meaning to permit users to grasp what program does.
I define GRASP as the term standing for 
**G**raphically **R**ecognizable **A**nalysis **S**ystem for **P**rogramming. **But in this course, I will only implement spell check function.** 

In general, spell checker is installed in many text editor software. Spell checker improved quality of documents and help users write correctly. With spell checker, you can do:
- write text correctly in important situation
- find possible misspelled phrases
- define user's own expressions (if they do not want to regard as misspelled words)

Especially, the 3rd function is original one in GRASP application. This allows a user to ignore his/her own original phrases, which makes checking documents faster.

Therefore, I would like to make spell-checker.** This can be my practice to code needed fuction.  

## What algorithms and data structures am I implementing?
I would like to apply several technique to spell check function.  
---

#### **Spell checker**
As mentioned in the course page of ideas for project topics, 
> A spell checker can be implemented by comparing the distance from an input string that is NOT in a dictionary to others that are.  

I will apply **Damerau-Levensthein distance** to compare the distance. The vocabulary can be stored in a **Trie** (prefix tree) data structure. And my spell check will consider **keyboard adjacency**, which will improve the quality of correctly-spelled phrases.  

## What inputs does my program take, and how are they used?
My program takes user's program to analyze. And also, it accepts input from the mouse and keyboard, and these operations are used to select applications for the target program, operate the program itself, and view analysis results.

## References
[1] Python Software Foundation, https://docs.python.org/3/reference/grammar.html  
[2] Benjamin Livshits section 7.3 "Static Techniques for Security," Stanford doctoral thesis, 2006., https://dl.acm.org/doi/10.5555/1269235  